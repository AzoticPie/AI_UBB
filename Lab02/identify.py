import numpy as np 
import networkx as nx

def greedyCommunitiesDetectionByTool(network):
    # Input: a graph
    # Output: list of comunity index (for every node)

    from networkx.algorithms import community

    A=np.matrix(network["mat"])
    G=nx.DiGraph(np.array(A))
    communities_generator = community.girvan_newman(G)
    top_level_communities = next(communities_generator)
    sorted(map(sorted, top_level_communities))
    communities = [0 for node in range(network['noNodes'])]
    index = 1
    for community in sorted(map(sorted, top_level_communities)):
        for node in community:
            communities[node] = index
        index += 1
    return communities


def greedyCommunitiesDetection(G, no_of_components_to_split=2):
    #A=np.matrix(network["mat"])
    #G=nx.Graph(np.array(A))
    communities = dict.fromkeys(G.nodes, 0)

    conex_components = nx.algorithms.components.number_connected_components(G)

    while(no_of_components_to_split > conex_components and conex_components < G.number_of_nodes()):
        # Calculate the betweenness centrality
        btw_centrality = nx.algorithms.centrality.edge_betweenness_centrality(G)
        # sort based on betweenness centrality
        sorted_edges = sorted(btw_centrality.items(), key = lambda item:item[1], reverse = True)[0]
        #print('Removing the edge', sorted_edges)
        # remove edge which has highest centrality
        G.remove_edge(*sorted_edges[0])
        conex_components = nx.algorithms.components.number_connected_components(G)

    #@print(sorted(nx.connected_components(G), key=len, reverse=True))
    index = 1
    for community in [c for c in sorted(nx.connected_components(G), key=len, reverse=True)]:
        for node in community:
            communities[node] = index
        index += 1

    return communities