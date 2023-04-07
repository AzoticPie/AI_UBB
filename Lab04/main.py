from plot import *
from fitness import *
import time
import matplotlib.pyplot as plt
from ga import GA

def main(filename = 'karate', mutation_seed = 1, crossover_seed = 1, nr_generations = 100, pop_size = 200):
    network = readTSP(filename)
    nr_nodes = network['nr_nodes']

    # Chromosome params
    chromosome_param = {'nodes':nr_nodes, 'mutation_seed':mutation_seed, 'crossover_seed':crossover_seed, 'points': (network['source'], network['destination'])}
    # Genetic algorithm params
    param = {'network': network, 'pop_size': pop_size,'chromosome_param': chromosome_param, 'function': tsp_fitness}

    ga = GA(param)
    ga.evaluatePopulation()

    # Plotting params
    plot_param = {'file': filename, 'all_best_fitnesses' : [], 'all_worst_fitnesses' : [], 'all_avg_fitnesses' : [], 'generations': [], 'best_chromosome':ga.bestChromosome().__copy__(), 'mutation_seed':mutation_seed, 'crossover_seed': crossover_seed, 'nr_generations':nr_generations}

    plot_param['all_best_fitnesses'].append(ga.bestChromosome().fitness)
    plot_param['all_worst_fitnesses'].append(ga.worstChromosome().fitness)
    plot_param['all_avg_fitnesses'].append(ga.averageFitness())
    plot_param['generations'].append(0)

    for gen in range(1, nr_generations+1):
        print(gen)
        ga.nextGeneration()
        plot_param['all_best_fitnesses'].append(ga.bestChromosome().fitness)
        plot_param['all_worst_fitnesses'].append(ga.worstChromosome().fitness)
        plot_param['all_avg_fitnesses'].append(ga.averageFitness())
        plot_param['generations'].append(gen)
        if plot_param['best_chromosome'].fitness > ga.bestChromosome().fitness:
            plot_param['best_chromosome'] = ga.bestChromosome().__copy__()
        if gen%10 == 0:
            print(plot_param['best_chromosome'])

    print(plot_param['best_chromosome'])
    printAndSavePlot(plotParam=plot_param)
    
    #plotNetwork(network, plot_param['best_chromosome'].repres, labels=True)

stTime = time.time()
# for i in range(1, 5):
#     for _ in range(10):
#         startTime = time.time()
#         main(i)
#         print("--- %s seconds ---" % (time.time() - startTime))
files = ['networks\\easy_01_tsp.txt', 'networks\\medium_02_tsp.txt']

main(filename='networks\\berlin52_tsp.txt', mutation_seed=1, crossover_seed=1, nr_generations=50, pop_size=500)