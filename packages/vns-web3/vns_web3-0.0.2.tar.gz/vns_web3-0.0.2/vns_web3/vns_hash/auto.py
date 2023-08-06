from vns_hash.backends.auto import (
    AutoBackend,
)
from vns_hash.main import (
    Keccak256,
)

keccak = Keccak256(AutoBackend())
