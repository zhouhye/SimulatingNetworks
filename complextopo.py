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
        ethernetConfig = {'bw': 25, 'delay': '2ms', 'loss': 0}
        wifiConfig = {'bw': 10, 'delay': '6ms', 'loss': 3}
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

        #add links
        self.addLink("h1", "s1", **ethernetConfig)
        self.addLink("s1", "s2", **ethernetConfig)
        self.addLink("s2", "s3", **ethernetConfig)
        self.addLink("s2", "s4", **ethernetConfig)
        self.addLink("s3", "h2", **g3Config)
        self.addLink("s4", "h3", **wifiConfig)


