from functools import (
    singledispatch,
)
import operator
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    Iterable,
    NoReturn,
    TypeVar,
    Union,
)

from vns_account import (
    Account,
)
from vns_account.signers.local import (
    LocalAccount,
)
from vns_keys.datatypes import (
    PrivateKey,
)
from vns_typing import (
    ChecksumAddress,
    HexStr,
)
from vns_utils import (
    to_dict,
)
from vns_utils.curried import (
    apply_formatter_if,
)
from vns_utils.toolz import (
    compose,
)

from web3._utils.method_formatters import (
    STANDARD_NORMALIZERS,
)
from web3._utils.rpc_abi import (
    TRANSACTION_PARAMS_ABIS,
    apply_abi_formatters_to_dict,
)
from web3._utils.transactions import (
    fill_nonce,
    fill_transaction_defaults,
)
from web3.types import (
    Middleware,
    RPCEndpoint,
    RPCResponse,
    TxParams,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401

T = TypeVar("T")

to_hexstr_from_vns_key = operator.methodcaller('to_hex')


def is_vns_key(value: Any) -> bool:
    return isinstance(value, PrivateKey)


key_normalizer = compose(
    # ignore Too few arguments error b/c to_hexstr... returns callable,
    apply_formatter_if(is_vns_key, to_hexstr_from_vns_key),  # type: ignore
)

_PrivateKey = Union[LocalAccount, PrivateKey, HexStr, bytes]


@to_dict
def gen_normalized_accounts(
    val: Union[_PrivateKey, Collection[_PrivateKey]]
) -> Iterable[Dict[ChecksumAddress, Account]]:
    if isinstance(val, (list, tuple, set,)):
        for i in val:
            account: Account = to_account(i)
            yield account.address, account
    else:
        account = to_account(val)
        yield account.address, account
        return


@singledispatch
def to_account(val: Any) -> NoReturn:
    raise TypeError(
        "key must be one of the types: "
        "vns_keys.datatype.PrivateKey, vns_account.signers.local.LocalAccount, "
        "or raw private key as a hex string or byte string. "
        "Was of type {0}".format(type(val)))


@to_account.register(LocalAccount)
def _(val: T) -> T:
    return val


def private_key_to_account(val: _PrivateKey) -> Account:
    normalized_key = key_normalizer(val)
    return Account.from_key(normalized_key)


to_account.register(PrivateKey, private_key_to_account)
to_account.register(str, private_key_to_account)
to_account.register(bytes, private_key_to_account)


def format_transaction(transaction: TxParams) -> TxParams:
    """Format transaction so that it can be used correctly in the signing middleware.

    Converts bytes to hex strings and other types that can be passed to the underlying layers.
    Also has the effect of normalizing 'from' for easier comparisons.
    """
    return apply_abi_formatters_to_dict(STANDARD_NORMALIZERS, TRANSACTION_PARAMS_ABIS, transaction)


def construct_sign_and_send_raw_middleware(
    private_key_or_account: Union[_PrivateKey, Collection[_PrivateKey]]
) -> Middleware:
    """Capture transactions sign and send as raw transactions


    Keyword arguments:
    private_key_or_account -- A single private key or a tuple,
    list or set of private keys. Keys can be any of the following formats:
      - An vns_account.LocalAccount object
      - An vns_keys.PrivateKey object
      - A raw private key as a hex string or byte string
    """

    accounts = gen_normalized_accounts(private_key_or_account)

    def sign_and_send_raw_middleware(
        make_request: Callable[[RPCEndpoint, Any], Any], w3: "Web3"
    ) -> Callable[[RPCEndpoint, Any], RPCResponse]:
        format_and_fill_tx = compose(
            format_transaction,
            fill_transaction_defaults(w3),
            fill_nonce(w3))

        def middleware(method: RPCEndpoint, params: Any) -> RPCResponse:
            if method != "vns_sendTransaction":
                return make_request(method, params)
            else:
                transaction = format_and_fill_tx(params[0])

            if 'from' not in transaction:
                return make_request(method, params)
            elif transaction.get('from') not in accounts:
                return make_request(method, params)

            account = accounts[transaction['from']]
            raw_tx = account.sign_transaction(transaction).rawTransaction

            return make_request(
                RPCEndpoint("vns_sendRawTransaction"),
                [raw_tx])

        return middleware

    return sign_and_send_raw_middleware
