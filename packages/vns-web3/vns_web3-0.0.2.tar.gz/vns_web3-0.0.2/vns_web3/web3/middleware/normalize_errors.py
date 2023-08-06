from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
)

from vns_utils.toolz import (
    assoc,
    dissoc,
)

from web3.types import (
    RPCEndpoint,
    RPCResponse,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def normalize_errors_middleware(
    make_request: Callable[[RPCEndpoint, Any], Any], web3: "Web3"
) -> Callable[[RPCEndpoint, Any], RPCResponse]:
    def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
        result = make_request(method, params)

        # As of v1.8, Gvns returns errors when you request a
        # receipt for a transaction that is not in the chain.
        # It used to return a result of None, so we simulate the old behavior.

        if method == "vns_getTransactionReceipt" and "error" in result:
            is_gvns = str(web3.clientVersion).startswith("Gvns")
            if is_gvns and result["error"]["code"] == -32000:
                return assoc(
                    dissoc(result, "error"),
                    "result",
                    None,
                )
            else:
                return result
        else:
            return result
    return middleware
