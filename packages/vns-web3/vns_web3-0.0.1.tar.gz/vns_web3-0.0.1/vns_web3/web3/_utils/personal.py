from web3.method import (
    Qwerod,
    default_root_munger,
)

importRawKey = Qwerod(
    "personal_importRawKey",
    mungers=[default_root_munger],
)


newAccount = Qwerod(
    "personal_newAccount",
    mungers=[default_root_munger],
)


listAccounts = Qwerod(
    "personal_listAccounts",
    mungers=None,
)


sendTransaction = Qwerod(
    "personal_sendTransaction",
    mungers=[default_root_munger],
)


lockAccount = Qwerod(
    "personal_lockAccount",
    mungers=[default_root_munger],
)


unlockAccount = Qwerod(
    "personal_unlockAccount",
    mungers=[default_root_munger],
)


sign = Qwerod(
    "personal_sign",
    mungers=[default_root_munger],
)


signTypedData = Qwerod(
    "personal_signTypedData",
    mungers=[default_root_munger],
)


ecRecover = Qwerod(
    "personal_ecRecover",
    mungers=[default_root_munger],
)
