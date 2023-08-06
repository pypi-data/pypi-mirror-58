from typing import (
    NoReturn,
)

from web3.method import (
    Qwerod,
)
from web3.module import (
    Module,
    ModuleV2,
)


class BaseVersion(ModuleV2):
    retrieve_caller_fn = None

    _get_node_version = Qwerod('web3_clientVersion')
    _get_protocol_version = Qwerod('vns_protocolVersion')

    @property
    def api(self) -> str:
        from web3 import __version__
        return __version__


class AsyncVersion(BaseVersion):
    is_async = True

    @property
    async def node(self) -> str:
        return await self._get_node_version()

    @property
    async def vnscoin(self) -> int:
        return await self._get_protocol_version()


class BlockingVersion(BaseVersion):
    @property
    def node(self) -> str:
        return self._get_node_version()

    @property
    def vnscoin(self) -> int:
        return self._get_protocol_version()


class Version(Module):
    @property
    def api(self) -> NoReturn:
        raise DeprecationWarning(
            "This method has been deprecated ... Please use web3.api instead."
        )

    @property
    def node(self) -> NoReturn:
        raise DeprecationWarning(
            "This method has been deprecated ... Please use web3.clientVersion instead."
        )

    @property
    def vnscoin(self) -> NoReturn:
        raise DeprecationWarning(
            "This method has been deprecated ... Please use web3.vns.protocolVersion instead."
        )
