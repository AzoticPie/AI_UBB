import os
import re
import json
import matplotlib.pyplot as plt 
import networkx as nx
import numpy as np

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

readNet('net.in')

def readGML(filename):
    filePath = os.path.join('real', filename, filename+'.gml')
    try:
        network = nx.read_gml(filePath, destringizer=int)
    except:
        network = nx.read_gml(filePath, destringizer=int, label='id')
    return network

def plotNetwork(network, communities = None, labels=False):
    """Plots a networkx network

    Args:
        network (networkx.Graph): network to plot
        labels (bool, optional): True to show labels on nodes. Defaults to False.
    """
    pos = nx.spring_layout(network)
    if communities:
        nx.draw_networkx_nodes(network, pos, node_size=600, node_color = communities)
    else:
        nx.draw_networkx_nodes(network, pos)
    nx.draw_networkx_edges(network, pos, alpha=0.3)
    if labels:
        nx.draw_networkx_labels(network, pos)

    plt.show()

def savePlot(plt, path):
    # Find the largest integer in the existing filenames
    existing_ints = []
    for filename in os.listdir(path):
        match = re.match(r"#(\d+)\.png", filename)
        if match:
           existing_ints.append(int(match.group(1)))
    if existing_ints:
        next_int = max(existing_ints) + 1
    else:
        next_int = 1

    return next_int

def printMetrics(index, bestChromosome, seedMutation, seedCrossover, noGenerations):
    sourceFile = open('docs_AI_LAB3.txt', 'a')
    print('', file = sourceFile)
    print(f"#{index}", file = sourceFile)
    print('best ' + bestChromosome.__str__(), file = sourceFile)
    print(f'mutation seed: {seedMutation}', file = sourceFile)
    print(f'crossover seed: {seedCrossover}', file = sourceFile)
    print(f'number of generations: {noGenerations}', file = sourceFile)

    sourceFile.close()

def printAndSavePlot(plotParam):
    best, = plt.plot(plotParam['generations'], plotParam['allBestFitnesses'], 'g-', label = 'best')
    mean, = plt.plot(plotParam['generations'], plotParam['allAvgFitnesses'], 'b-', label = 'mean')
    worst, = plt.plot(plotParam['generations'], plotParam['allWorstFitnesses'], 'r-', label = 'worst')

    greedy, = plt.plot([0], plotParam['greedyFitness'], 'ko', label = 'greedy')

    plt.legend([best, mean, worst, greedy], ['Best', 'Mean', 'Worst', 'Greedy'])

    path = "./plots"
    index = savePlot(plt, path = path)
    plt.title(plotParam['file'] + 'Network' + f"#{index}")
    plt.xlabel("Number of generations")
    plt.ylabel("Modularity value")
    saveRunData(index, plotParams=plotParam)
    plt.savefig(os.path.join(path, f"#{index}.png"))

    plt.show()

def saveRunData(index, plotParams):
    path = os.path.join('runData.json')
    with open(path, "r") as f:
        data = json.load(f)

    newRun = {}
    newRun['id'] = f"#{index}"
    newRun['noGenerations'] = plotParams['noGenerations']
    newRun['bestCommunity'] = plotParams['bestChromosome'].repres
    newRun['fitness'] = plotParams['bestChromosome'].fitness
    newRun['mutationSeed'] = plotParams['seedMutation']
    newRun['crossoverSeed'] = plotParams['seedCrossover']
    newRun['multiplicationSeed'] = plotParams['multiplicationSeed']

    data['networks'][plotParams['file']].append(newRun)
    # Convert the updated data to JSON format
    json_data = json.dumps(data)
    # Write the updated JSON data back to the file
    with open(path, "w") as f:
        f.write(json_data)