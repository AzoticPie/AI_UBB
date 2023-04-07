from plot import *
from genes import *
from random import uniform, randint
from fcOptimisation.utils import generateNewValue
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from identify import *
import math
import pandas as pd
import json

network = readGML('karate')
noDim = nx.number_of_nodes(network)

xref =  [[generateNewValue(1, 3)  for _ in range(noDim)] for _ in range(0, 1000)]
yref = [modularityFromNX(network, xi) for xi in xref]  
#y2ref = [nx.modularity_matrix(network, xi) for xi in xref]  

communities = [1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1]

ncopy = network.copy()
com = greedyCommunitiesDetection(ncopy)
plotNetwork(ncopy, communities=communities, labels=True)

path = os.path.join('runData.json')
with open(path, "r") as f:
    data = json.load(f)
k = {'a': 1, 'b':2}
data['networks']['karate'].append(k)
print(data['networks']['karate'])

# json{
# 	id: 
# 	file:
# 	noGenerations: 
# 	bestCommunity:
# 	fitness:
# 	MutationSeed:
# 	CrossoverSeed:
# 	MultiplicationSeed:
# }