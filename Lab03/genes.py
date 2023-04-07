import networkx as nx

def modularity(param, communities):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']  
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if (communities[i] == communities[j]):
               Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M

def modularityFromNX(network, communities):
    M = 2 * network.number_of_edges()
    Q = 0.0
    mat = nx.adjacency_matrix(network).todense()
    degrees = [node[1] for node in nx.degree(network)]
    for i in range(nx.number_of_nodes(network)):
        for j in range(nx.number_of_nodes(network)):
            if(communities[i] == communities[j]):
                Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M

def generateCommunities(nodesNumber, communitiesNumber=2):
    pass