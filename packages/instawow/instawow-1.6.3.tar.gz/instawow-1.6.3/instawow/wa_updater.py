from __future__ import annotations

import asyncio
from itertools import chain
from pathlib import Path
from typing import TYPE_CHECKING, Dict, List, NamedTuple, Optional, Sequence

from loguru import logger
from pydantic import BaseModel, Extra, validator
from yarl import URL

from .config import BaseConfig
from .utils import ManagerAttrAccessMixin, bucketise, run_in_thread as t

if TYPE_CHECKING:
    from .manager import Manager


metadata_api = URL('https://data.wago.io/api/check/weakauras')
raw_api = URL('https://data.wago.io/api/raw/encoded')


class BuilderConfig(BaseConfig):
    account: str

    class Config:
        env_prefix = 'WAC_'


class AuraEntry(BaseModel):
    id: str
    uid: str
    parent: Optional[str]
    url: URL
    version: int
    semver: Optional[str]
    ignore_wago_update: bool = False

    class Config:
        arbitrary_types_allowed = True
        fields = {'ignore_wago_update': {'alias': 'ignoreWagoUpdate'}}

    @validator('url', pre=True)
    def _convert_url(cls, value: str) -> URL:
        return URL(value)


class ApiMetadata__Changelog(BaseModel):
    format: Optional[str]
    text: str = ''

    class Config:
        extra = Extra.forbid


class ApiMetadata(BaseModel):
    id: str
    name: str
    slug: str
    url: str
    created: str
    modified: str
    game: str
    fork_of: Optional[str]
    username: str
    version: int
    version_string: str
    changelog: ApiMetadata__Changelog
    region_type: Optional[str]

    class Config:
        extra = Extra.forbid
        fields = {'id': {'alias': '_id'},
                  'fork_of': {'alias': 'forkOf'},
                  'version_string': {'alias': 'versionString'},
                  'region_type': {'alias': 'regionType'}}


class _OutdatedAura(NamedTuple):
    slug: str
    existing_auras: List[AuraEntry]
    metadata: ApiMetadata
    import_string: str


class WaCompanionBuilder(ManagerAttrAccessMixin):
    """A WeakAuras Companion port for shellfolk."""

    def __init__(self, manager: Manager) -> None:
        self.manager = manager
        self.builder_dir = self.manager.config.plugin_dir / __name__
        self.file_out = self.builder_dir / 'WeakAurasCompanion.zip'

    @staticmethod
    def extract_auras(source: str) -> Dict[str, List[AuraEntry]]:
        from lupa import LuaRuntime

        lua_runtime = LuaRuntime()

        table = lua_runtime.eval(source[source.find('= ') + 1 :])
        raw_auras = map(dict, table['displays'].values())
        auras = (AuraEntry(**a) for a in raw_auras if a.get('url'))
        aura_groups = {k: v
                       for k, v in bucketise(auras, key=lambda a: a.url.parts[1]).items()
                       if not any(i.ignore_wago_update for i in v)}
        return aura_groups

    def extract_installed_auras(self, account: str) -> Dict[str, List[AuraEntry]]:
        import time

        accounts = self.config.addon_dir.parents[1] / 'WTF/Account'
        saved_vars = accounts / account / 'SavedVariables/WeakAuras.lua'

        start = time.perf_counter()
        aura_groups = self.extract_auras(saved_vars.read_text(encoding='utf-8'))
        logger.debug(f'auras extracted in {time.perf_counter() - start}s')
        return aura_groups

    async def get_wago_aura_metadata(self, aura_ids: Sequence[str]) -> List[ApiMetadata]:
        url = metadata_api.with_query({'ids': ','.join(aura_ids)})
        async with self.web_client.get(url) as response:
            metadata = await response.json()

        results = dict.fromkeys(aura_ids)
        for item in (ApiMetadata(**i) for i in metadata):
            if item.slug in results:
                results[item.slug] = item
            else:
                logger.info(f'extraneous {item.slug!r} slug in metadata')
        return list(results.values())

    async def get_wago_aura_import_string(self, aura_id: str) -> str:
        url = raw_api.with_query({'id': aura_id})
        async with self.web_client.get(url) as response:
            return await response.text()

    async def get_outdated(self, aura_groups: Dict[str, List[AuraEntry]]) -> List[_OutdatedAura]:
        if not aura_groups:
            return []

        aura_metadata = await self.get_wago_aura_metadata(list(aura_groups))
        auras_with_metadata = filter(lambda v: v[1], zip(aura_groups.items(), aura_metadata))
        outdated_auras = [((s, w), r)
                          for (s, w), r in auras_with_metadata
                          if r.version > next(chain((a for a in w if not a.parent), w)).version]
        new_auras = await asyncio.gather(*(self.get_wago_aura_import_string(r.id)
                                           for _, r in outdated_auras))
        return [_OutdatedAura(s, w, r, p)
                for ((s, w), r), p in zip(outdated_auras, new_auras)]

    def make_addon(self, outdated: List[_OutdatedAura]) -> None:
        from jinja2 import Environment, FileSystemLoader
        from zipfile import ZipFile, ZipInfo

        tpl_dir = Path(__file__).parent / 'wa_templates'
        jinja_env = Environment(loader=FileSystemLoader(str(tpl_dir)),
                                trim_blocks=True, lstrip_blocks=True)

        with ZipFile(self.file_out, 'w') as addon_zip:
            def write_tpl(filename: str, ctx: dict) -> None:
                # Not using a plain string as the first argument to ``writestr``
                # 'cause the timestamp is set dynamically by default, which
                # renders the build rather - shall we say - unreproducible
                zip_info = ZipInfo(filename=f'WeakAurasCompanion/{filename}')
                tpl = jinja_env.get_template(filename)
                addon_zip.writestr(zip_info, tpl.render(**ctx))

            write_tpl('data.lua',
                      {'was': [(o.metadata.slug,
                                {'name': o.metadata.name,
                                 'author': o.metadata.username,
                                 'encoded': o.import_string,
                                 'wagoVersion': o.metadata.version,
                                 'wagoSemver': o.metadata.version_string,
                                 'versionNote': o.metadata.changelog.text})
                               for o in outdated],
                       'uids': [(a.uid, a.url.parts[1])
                                for o in outdated
                                for a in o.existing_auras],
                       'ids':  [(a.id, a.url.parts[1])
                                for o in outdated
                                for a in o.existing_auras],
                       'stash': []})    # Send to WAC not supported - always empty
            write_tpl('init.lua', {})
            write_tpl('WeakAurasCompanion.toc',
                      {'interface': '11303' if self.config.is_classic else '80205'})

    async def build(self, account: Optional[str] = None) -> None:
        config = BuilderConfig(account=account)
        auras = await t(self.extract_installed_auras)(config.account)
        outdated_auras = await self.get_outdated(auras)

        await t(self.builder_dir.mkdir)(exist_ok=True)
        await t(self.make_addon)(outdated_auras)

    def checksum(self) -> str:
        from hashlib import sha256
        return sha256(self.file_out.read_bytes()).hexdigest()
