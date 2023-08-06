import pytest

from web3.datastructures import (
    AttributeDict,
)


class GoVnscoinAdminModuleTest:
    def test_add_peer(self, web3):
        result = web3.gvns.admin.add_peer(
                'enode://f1a6b0bdbf014355587c3018454d070ac57801f05d3b39fe85da574f002a32e929f683d72aa5a8318382e4d3c7a05c9b91687b0d997a39619fb8a6e7ad88e512@1.1.1.1:30303',  # noqa: E501
                )
        assert result is True

    def test_admin_datadir(self, web3, datadir):
        result = web3.gvns.admin.datadir()
        assert result == datadir

    def test_admin_node_info(self, web3):
        result = web3.gvns.admin.node_info()
        expected = AttributeDict({
            'id': '',
            'name': '',
            'enode': '',
            'ip': '',
            'ports': AttributeDict({}),
            'listenAddr': '',
            'protocols': AttributeDict({})
        })
        # Test that result gives at least the keys that are listed in `expected`
        assert not set(expected.keys()).difference(result.keys())

    def test_admin_peers(self, web3):
        enode = web3.gvns.admin.node_info()['enode']
        web3.gvns.admin.add_peer(enode)
        result = web3.gvns.admin.peers()
        assert len(result) == 1

    def test_admin_start_stop_rpc(self, web3):
        start = web3.gvns.admin.start_rpc("localhost", 8545)
        assert start

        stop = web3.gvns.admin.stop_rpc()
        assert stop

    def test_admin_start_stop_ws(self, web3):
        start = web3.gvns.admin.start_ws("localhost", 8546)
        assert start

        stop = web3.gvns.admin.stop_ws()
        assert stop

    #
    # Deprecated
    #
    def test_admin_addPeer(self, web3):
        with pytest.warns(DeprecationWarning):
            result = web3.gvns.admin.addPeer(
                'enode://f1a6b0bdbf014355587c3018454d070ac57801f05d3b39fe85da574f002a32e929f683d72aa5a8318382e4d3c7a05c9b91687b0d997a39619fb8a6e7ad88e512@1.1.1.1:30303',  # noqa: E501
            )
            assert result is True

    def test_admin_nodeInfo(self, web3):
        with pytest.warns(DeprecationWarning):
            result = web3.gvns.admin.nodeInfo()
            expected = AttributeDict({
                'id': '',
                'name': '',
                'enode': '',
                'ip': '',
                'ports': AttributeDict({}),
                'listenAddr': '',
                'protocols': AttributeDict({})
            })
            # Test that result gives at least the keys that are listed in `expected`
            assert not set(expected.keys()).difference(result.keys())

    def test_admin_startRPC(self, web3):
        with pytest.warns(DeprecationWarning):
            start = web3.gvns.admin.startRPC('localhost', 8545)
            assert start

        stop = web3.gvns.admin.stop_rpc()
        assert stop

    def test_admin_stopRPC(self, web3):
        start = web3.gvns.admin.start_rpc('localhost', 8545)
        assert start

        with pytest.warns(DeprecationWarning):
            stop = web3.gvns.admin.stopRPC()
            assert stop

    def test_admin_startWS(self, web3):
        with pytest.warns(DeprecationWarning):
            start = web3.gvns.admin.startWS('localhost', 8546)
            assert start

        stop = web3.gvns.admin.stop_ws()
        assert stop

    def test_admin_stopWS(self, web3):
        start = web3.gvns.admin.start_ws('localhost', 8546)
        assert start

        with pytest.warns(DeprecationWarning):
            stop = web3.gvns.admin.stopWS()
            assert stop
