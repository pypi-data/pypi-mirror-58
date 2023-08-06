import pkg_resources

from vns_abi.abi import (  # NOQA
    decode_abi,
    decode_single,
    encode_abi,
    encode_single,
    is_encodable,
    is_encodable_type,
)

__version__ = pkg_resources.get_distribution('vns-abi').version
