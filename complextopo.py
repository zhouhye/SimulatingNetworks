from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.util import custom


# Topology to be instantiated in Mininet
class ComplexTopo(Topo):
    """Mininet Complex Topology"""

    def __init__(self, cpu=.1, max_queue_size=None, **params):

        # Initialize topo
        Topo.__init__(self, **params)

        # TODO: Create your Mininet Topology here!
        # add host and link config
        hostConfig = {'cpu': cpu}
        wifiConfig = {'bw': 25, 'delay': '2ms', 'loss': 0}
        ethernetConfig = {'bw': 10, 'delay': '6ms', 'loss': 3}
        g3Config = {'bw': 3, 'delay': "10ms", 'loss': 8}

        # add 3 hosts
        self.addHost("h1", **hostConfig)
        self.addHost("h2", **hostConfig)
        self.addHost("h3", **hostConfig)

        # add 4 switches
        self.addSwitch("s1")
        self.addSwitch("s2")
        self.addSwitch("s3")
        self.addSwitch("s4")


