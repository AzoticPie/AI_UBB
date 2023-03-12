import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt 

from networkx.algorithms import community

# read the network details
def readNet(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(" ")
        for j in range(n):
            mat[-1].append(int(elems[j]))
    net["mat"] = mat 
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += mat[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    A=np.matrix(net["mat"])
    G=nx.Graph(np.array(A))
    
    return G


# plot a network 
def plotNetwork(G, communities):
    #np.random.seed(123) #to freeze the graph's view (networks uses a random view)
    #A=np.matrix(network["mat"])
    #G=nx.Graph(np.array(A))
    pos = nx.spring_layout(G)  # compute graph layout
    plt.figure(figsize=(4, 4))  # image is 8 x 8 inches 
    nx.draw_networkx_nodes(G, pos, node_size=600, node_color = list(communities.values()), label=True)
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    #nx.draw_networkx_labels(G, pos)
    plt.show()
