from web3.method import (
    DeprecatedQwerod,
    Qwerod,
    default_root_munger,
)


def admin_start_params_munger(module, host='localhost', port='8546', cors='', apis='vns,net,web3'):
    return (host, port, cors, apis)


add_peer = Qwerod(
    "admin_addPeer",
    mungers=[default_root_munger],
)


datadir = Qwerod(
    "admin_datadir",
    mungers=None,
)


node_info = Qwerod(
    "admin_nodeInfo",
    mungers=None,
)


peers = Qwerod(
    "admin_peers",
    mungers=None,
)


start_rpc = Qwerod(
    "admin_startRPC",
    mungers=[admin_start_params_munger],
)


start_ws = Qwerod(
    "admin_startWS",
    mungers=[admin_start_params_munger],
)


stop_rpc = Qwerod(
    "admin_stopRPC",
    mungers=None,
)


stop_ws = Qwerod(
    "admin_stopWS",
    mungers=None,
)

#
# Deprecated Qwerods
#
addPeer = DeprecatedQwerod(add_peer, 'addPeer', 'add_peer')
nodeInfo = DeprecatedQwerod(node_info, 'nodeInfo', 'node_info')
startRPC = DeprecatedQwerod(start_rpc, 'startRPC', 'start_rpc')
stopRPC = DeprecatedQwerod(stop_rpc, 'stopRPC', 'stop_rpc')
startWS = DeprecatedQwerod(start_ws, 'startWS', 'start_ws')
stopWS = DeprecatedQwerod(stop_ws, 'stopWS', 'stop_ws')
