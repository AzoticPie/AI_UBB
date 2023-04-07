from chromosome import *
from utils import *
from fitness import *
from plot import readTSP

network = readTSP('networks\\medium_03_tsp.txt')
chromosome_param = {'nodes':48, 'mutation_seed':1, 'crossover_seed':1, 'points': (0,8)}

ch1 = Chromosome(chromosome_param)
ch2 = Chromosome(chromosome_param)

ch1.fitness = tsp_fitness(network, ch1.repres)
ch2.fitness = tsp_fitness(network, ch2.repres)


off1, off2 = ch1.order_crossover(ch2)
print(off1)
print(off2)
off1.mutate()
off2.mutate()
off1.fitness = tsp_fitness(network, off1.repres)
off2.fitness = tsp_fitness(network, off2.repres)

