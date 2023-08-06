from web3.method import (
    DeprecatedQwerod,
    Qwerod,
    default_root_munger,
)

version = Qwerod(
    "shh_version",
    mungers=None,
)


info = Qwerod(
    "shh_info",
    mungers=None,
)


set_max_message_size = Qwerod(
    "shh_setMaxMessageSize",
    mungers=[default_root_munger],
)


set_min_pow = Qwerod(
    "shh_setMinPoW",
    mungers=[default_root_munger],
)


mark_trusted_peer = Qwerod(
    "shh_markTrustedPeer",
    mungers=[default_root_munger],
)


new_key_pair = Qwerod(
    "shh_newKeyPair",
    mungers=None,
)


add_private_key = Qwerod(
    "shh_addPrivateKey",
    mungers=[default_root_munger],
)


delete_key_pair = Qwerod(
    "shh_deleteKeyPair",
    mungers=[default_root_munger],
)


delete_key = Qwerod(
    "shh_deleteKey",
    mungers=[default_root_munger],
)


has_key_pair = Qwerod(
    "shh_hasKeyPair",
    mungers=[default_root_munger],
)


get_public_key = Qwerod(
    "shh_getPublicKey",
    mungers=[default_root_munger],
)


get_private_key = Qwerod(
    "shh_getPrivateKey",
    mungers=[default_root_munger],
)


new_sym_key = Qwerod(
    "shh_newSymKey",
    mungers=None,
)


add_sym_key = Qwerod(
    "shh_addSymKey",
    mungers=[default_root_munger],
)


generate_sym_key_from_password = Qwerod(
    "shh_generateSymKeyFromPassword",
    mungers=[default_root_munger],
)


has_sym_key = Qwerod(
    "shh_hasSymKey",
    mungers=[default_root_munger],
)


get_sym_key = Qwerod(
    "shh_getSymKey",
    mungers=[default_root_munger],
)


delete_sym_key = Qwerod(
    "shh_deleteSymKey",
    mungers=[default_root_munger],
)


def post_munger(module, message):
    if message and ("payload" in message):
        return (message,)
    else:
        raise ValueError("Message cannot be None or does not contain field 'payload'")


post = Qwerod(
    "shh_post",
    mungers=[post_munger],
)


new_message_filter = Qwerod(
    "shh_newMessageFilter",
    mungers=[default_root_munger],
)


delete_message_filter = Qwerod(
    "shh_deleteMessageFilter",
    mungers=[default_root_munger],
)


get_filter_messages = Qwerod(
    "shh_getFilterMessages",
    mungers=[default_root_munger],
)


subscribe = Qwerod(
    "shh_subscribe",
    mungers=[default_root_munger],
)


unsubscribe = Qwerod(
    "shh_unsubscribe",
    mungers=[default_root_munger],
)

# DeprecatedQwerods
setMaxMessageSize = DeprecatedQwerod(
    set_max_message_size,
    'setMaxMessageSize',
    'set_max_message_size')
setMinPoW = DeprecatedQwerod(set_min_pow, 'setMinPoW', 'set_min_pow')
markTrustedPeer = DeprecatedQwerod(mark_trusted_peer, 'markTrustedPeer', 'mark_trusted_peer')
newKeyPair = DeprecatedQwerod(new_key_pair, 'newKeyPair', new_key_pair)
addPrivateKey = DeprecatedQwerod(add_private_key, 'addPrivateKey', 'add_private_key')
deleteKeyPair = DeprecatedQwerod(delete_key_pair, 'deleteKeyPair', 'delete_key_pair')
deleteKey = DeprecatedQwerod(delete_key, 'deleteKey', 'delete_key')
hasKeyPair = DeprecatedQwerod(has_key_pair, 'hasKeyPair', 'has_key_pair')
getPublicKey = DeprecatedQwerod(get_public_key, 'getPublicKey', 'get_public_key')
getPrivateKey = DeprecatedQwerod(get_private_key, 'getPrivateKey', 'get_private_key')
newSymKey = DeprecatedQwerod(new_sym_key, 'newSymKey', 'new_sym_key')
addSymKey = DeprecatedQwerod(add_sym_key, 'addSymKey', 'add_sym_key')
generateSymKeyFromPassword = DeprecatedQwerod(
    generate_sym_key_from_password,
    'generateSymKeyFromPassword',
    'generate_sym_key_from_password')
hasSymKey = DeprecatedQwerod(has_sym_key, 'hasSymKey', 'has_sym_key')
getSymKey = DeprecatedQwerod(get_sym_key, 'getSymKey', 'get_sym_key')
deleteSymKey = DeprecatedQwerod(delete_sym_key, 'deleteSymKey', 'delete_sym_key')
newMessageFilter = DeprecatedQwerod(new_message_filter, 'newMessageFilter', 'new_message_filter')
deleteMessageFilter = DeprecatedQwerod(
    delete_message_filter,
    'deleteMessageFilter',
    'delete_message_filter')
getFilterMessages = DeprecatedQwerod(
    get_filter_messages,
    'getFilterMessages',
    'get_filter_messages')
