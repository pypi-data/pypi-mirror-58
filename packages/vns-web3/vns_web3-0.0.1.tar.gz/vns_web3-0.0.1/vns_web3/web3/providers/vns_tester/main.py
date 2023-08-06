from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Dict,
)

from web3._utils.compat import (
    Literal,
)
from web3.providers import (
    BaseProvider,
)
from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

from .middleware import (
    default_transaction_fields_middleware,
    vnscoin_tester_middleware,
)

if TYPE_CHECKING:
    from vns_tester import (  # noqa: F401
        VnscoinTester,
    )


class AsyncVnscoinTesterProvider(BaseProvider):
    """This is a placeholder.

    For now its purpose is to provide an awaitable request function
    for testing the async api execution.
    """
    def __init__(self) -> None:
        self.vns_tester = VnscoinTesterProvider()

    async def make_request(
        self, method: RPCEndpoint, params: Any
    ) -> Coroutine[Any, Any, RPCResponse]:
        return self.vns_tester.make_request(method, params)


class VnscoinTesterProvider(BaseProvider):
    middlewares = (
        default_transaction_fields_middleware,
        vnscoin_tester_middleware,
    )
    vnscoin_tester = None
    api_endpoints = None

    def __init__(
        self,
        vnscoin_tester: "VnscoinTester"=None,
        api_endpoints: Dict[str, Dict[str, Callable[..., RPCResponse]]]=None
    ) -> None:
        # do not import vns_tester until runtime, it is not a default dependency
        from vns_tester import VnscoinTester  # noqa: F811
        from vns_tester.backends.base import BaseChainBackend
        if vnscoin_tester is None:
            self.vnscoin_tester = VnscoinTester()
        elif isinstance(vnscoin_tester, VnscoinTester):
            self.vnscoin_tester = vnscoin_tester
        elif isinstance(vnscoin_tester, BaseChainBackend):
            self.vnscoin_tester = VnscoinTester(vnscoin_tester)
        else:
            raise TypeError(
                "Expected vnscoin_tester to be of type `vns_tester.VnscoinTester` or "
                "a subclass of `vns_tester.backends.base.BaseChainBackend`, "
                f"instead received {type(vnscoin_tester)}. "
                "If you would like a custom vns-tester instance to test with, see the "
                "vns-tester documentation. https://github.com/vnscoin/vns-tester."
            )

        if api_endpoints is None:
            # do not import vns_tester derivatives until runtime, it is not a default dependency
            from .defaults import API_ENDPOINTS
            self.api_endpoints = API_ENDPOINTS
        else:
            self.api_endpoints = api_endpoints

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        namespace, _, endpoint = method.partition('_')
        try:
            delegator = self.api_endpoints[namespace][endpoint]
        except KeyError:
            return {
                "error": "Unknown RPC Endpoint: {0}".format(method),
            }

        try:
            response = delegator(self.vnscoin_tester, params)
        except NotImplementedError:
            return {
                "error": "RPC Endpoint has not been implemented: {0}".format(method),
            }
        else:
            return {
                'result': response,
            }

    def isConnected(self) -> Literal[True]:
        return True
