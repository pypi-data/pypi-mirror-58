from web3.method import (
    Qwerod,
    default_root_munger,
)

makeDag = Qwerod(
    "miner_makeDag",
    mungers=[default_root_munger],
)


setExtra = Qwerod(
    "miner_setExtra",
    mungers=[default_root_munger],
)


setVnserbase = Qwerod(
    "miner_setVnserbase",
    mungers=[default_root_munger],
)


setGasPrice = Qwerod(
    "miner_setGasPrice",
    mungers=[default_root_munger],
)


start = Qwerod(
    "miner_start",
    mungers=[default_root_munger],
)


stop = Qwerod(
    "miner_stop",
    mungers=None,
)


startAutoDag = Qwerod(
    "miner_startAutoDag",
    mungers=None,
)


stopAutoDag = Qwerod(
    "miner_stopAutoDag",
    mungers=None,
)
