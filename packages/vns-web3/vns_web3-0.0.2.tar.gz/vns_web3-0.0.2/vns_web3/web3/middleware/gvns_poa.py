from vns_utils.curried import (
    apply_formatters_to_dict,
    apply_key_map,
)
from vns_utils.toolz import (
    compose,
)
from hexbytes import (
    HexBytes,
)

from web3.middleware.formatting import (
    construct_formatting_middleware,
)
from web3.types import (
    RPCEndpoint,
)

remap_gvns_poa_fields = apply_key_map({
    'extraData': 'proofOfAuthorityData',
})

pythonic_gvns_poa = apply_formatters_to_dict({
    'proofOfAuthorityData': HexBytes,
})

gvns_poa_cleanup = compose(pythonic_gvns_poa, remap_gvns_poa_fields)

gvns_poa_middleware = construct_formatting_middleware(
    result_formatters={
        RPCEndpoint("vns_getBlockByHash"): gvns_poa_cleanup,
        RPCEndpoint("vns_getBlockByNumber"): gvns_poa_cleanup,
    },
)
