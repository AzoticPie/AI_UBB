    # prerequisites
import os
import warnings 
from readnplot import *
from identify import *

warnings.simplefilter('ignore')

def testExample():
    filePath = 'net.in'
    network = readNet(filePath)
    plotNetwork(network, greedyCommunitiesDetection(network.copy(), 7))


def test1():
    filePath = os.path.join('real', 'dolphins', 'dolphins.gml')
    network = nx.read_gml(filePath, destringizer=int)
    plotNetwork(network, greedyCommunitiesDetection(network.copy()))

def test2():
    filePath = os.path.join('real', 'football', 'football.gml')
    network = nx.read_gml(filePath, destringizer=int)
    plotNetwork(network, greedyCommunitiesDetection(network.copy()))

def test3():
    filePath = os.path.join('real', 'karate', 'karate.gml')
    network = nx.read_gml(filePath, destringizer=int, label="id")
    plotNetwork(network, greedyCommunitiesDetection(network.copy()))

def test4():
    filePath = os.path.join('real', 'krebs', 'krebs.gml')
    network = nx.read_gml(filePath, destringizer=int)
    plotNetwork(network, greedyCommunitiesDetection(network.copy()))

def test5():
    filePath = os.path.join('real', 'polbooks', 'polbooks.gml')
    network = nx.read_gml(filePath, destringizer=int)
    plotNetwork(network, greedyCommunitiesDetection(network.copy()))

def test6():
    filePath = os.path.join('real', 'lesmis', 'lesmis.gml')
    network = nx.read_gml(filePath, destringizer=int)
    plotNetwork(network, greedyCommunitiesDetection(network.copy()))

def test7():
    filePath = os.path.join('real', 'adjnoun', 'adjnoun.gml')
    network = nx.read_gml(filePath, destringizer=int)
    plotNetwork(network, greedyCommunitiesDetection(network.copy(), 5))

def test8():
    filePath = os.path.join('real', 'celegansneural', 'celegansneural.gml')
    network = nx.read_gml(filePath, destringizer=int)
    plotNetwork(network, greedyCommunitiesDetection(network.copy(), 10))

def test9():
    filePath = os.path.join('real', 'netscience.gml')
    network = nx.read_gml(filePath, destringizer=int)
    plotNetwork(network, greedyCommunitiesDetection(network.copy(), 10))

def test0():
    filePath = os.path.join('real', 'power.gml')
    network = nx.read_gml(filePath, destringizer=int, label='id')
    plotNetwork(network, greedyCommunitiesDetection(network.copy(), 10))

test0()