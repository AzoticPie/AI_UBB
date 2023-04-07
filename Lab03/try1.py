from plot import *
from genes import *
import time
import matplotlib.pyplot as plt
import identify
from try1.ga import GA

stTime = time.time()

def main(file='karate', seedMutation = 1, seeCrossover = 1):
    network = readGML(file)
    noDim = nx.number_of_nodes(network)
    seedMutation = seedMutation
    seedCrossover = seeCrossover
    noGenerations = 2000

    # Chromosome params
    chromosomeParam = {'max': 2, 'noDim':noDim, 'seedmutation':seedMutation, 'seedcrossover':seedCrossover}
    # Genetic algorithm params
    param = {'network': network, 'netSize': 500,'chromosomeParam': chromosomeParam, 'function': modularityFromNX}

    ga = GA(param)
    ga.evaluatePopulation()

    # Plotting params
    plotParam = {'file': file, 'allBestFitnesses' : [], 'allWorstFitnesses' : [], 'allAvgFitnesses' : [], 'generations': [], 'bestChromosome':ga.bestChromosome().__copy__(), 'greedyFitness': 0, 'seedMutation':seedMutation, 'seedCrossover': seedCrossover, 'noGenerations':noGenerations, 'multiplicationSeed' : 1}

    plotParam['allBestFitnesses'].append(ga.bestChromosome().fitness)
    plotParam['allWorstFitnesses'].append(ga.worstChromosome().fitness)
    plotParam['allAvgFitnesses'].append(ga.averageFitness())
    plotParam['generations'].append(0)

    for gen in range(noGenerations):
        ga.nextGeneration()
        ga.evaluatePopulation()
        plotParam['allBestFitnesses'].append(ga.bestChromosome().fitness)
        plotParam['allWorstFitnesses'].append(ga.worstChromosome().fitness)
        plotParam['allAvgFitnesses'].append(ga.averageFitness())
        plotParam['generations'].append(gen)
        if plotParam['bestChromosome'] < ga.bestChromosome():
            plotParam['bestChromosome'] = ga.bestChromosome().__copy__()



    ncopy = network.copy()
    com = identify.greedyCommunitiesDetection(ncopy)
    com = list(com.values())

    plotParam['greedyFitness'] = modularityFromNX(network,com)
    
    print("--- TOTAL %s seconds ---" % (time.time() - stTime))

    printAndSavePlot(plotParam=plotParam)
    plotNetwork(ncopy, plotParam['bestChromosome'].repres, labels=True)

# for i in range(1, 5):
#     for _ in range(10):
#         startTime = time.time()
#         main(i)
#         print("--- %s seconds ---" % (time.time() - startTime))
files = ['dolphins', 'karate', 'football', 'krebs', 'polbooks', 'lesmis',  'star', 'shell', 'lobster', 'adjnoun', 'celegansneural','netscience', 'power']
main(file='lesmis', seedMutation=1, seeCrossover=1)