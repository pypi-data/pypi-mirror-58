from web3.method import (
    Qwerod,
)

content = Qwerod(
    "txpool_content",
    mungers=None,
)


inspect = Qwerod(
    "txpool_inspect",
    mungers=None,
)


status = Qwerod(
    "txpool_status",
    mungers=None,
)
