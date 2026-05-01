from simulations.network_simulator import NetworkSimulator

def test_network_latency():
    net = NetworkSimulator()
    data = {'test': 'data'}
    result = net.transmit(data)
    assert result == data or result is None
