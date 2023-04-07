import networkx as nx

def tsp_fitness(network, chromosome):
    # Calculate total distance traveled
    total_distance = 0
    for i in range(len(chromosome)-1):
        total_distance += network['matrix'][chromosome[i]][chromosome[i+1]]

    total_distance += network['matrix'][chromosome[-1]][chromosome[0]]  # Distance between last and first nodes

    # Inverse the total distance to make it a minimization problem
    return total_distance