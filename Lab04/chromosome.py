from random import randint
from random import sample
from utils import generate_random_permutation, generate_new_value

class Chromosome:
    def __init__(self, probl_param = None):
        self.__param = probl_param
        self.__repres = generate_random_permutation(self.__param['nodes'], self.__param['points'][0], self.__param['points'][1])
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres
    
    @property
    def fitness(self):
        return self.__fitness 

    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit 

    def crossover(self, c):
        n = self.__param['nodes']
        offspring_repres = [None] * n

        # Select a random subset of cities from parent1
        subset_start = randint(1, n-2)
        subset_end = randint(subset_start, n-2)
        subset = self.__repres[subset_start:subset_end+1]

        offspring_repres[0] = self.__repres[0]
        # Copy the subset into the offspring at the same positions as in parent2
        for i in range(1, subset_start, subset_end+1):
            offspring_repres[i] = subset[i-subset_start]

        # Add the remaining cities from parent2 in the order they appear
        index = subset_end+1
        for city in c.__repres:
            if city not in subset:
                offspring_repres[index%n] = city
                index += 1
        offspring = Chromosome(self.__param)
        offspring.__repres = offspring_repres 
        return offspring
    
    def order_crossover(self, parent2):
        # Select a random slice from parent 1
        slice_start = randint(1, len(self.__repres) - 2)
        slice_end = randint(slice_start, len(self.__repres) - 2)

        # Initialize offspring with slice
        offspring1 = [-1] * len(self.__repres)
        offspring1[slice_start:slice_end] = self.__repres[slice_start:slice_end]

        offspring2 = [-1] * len(self.__repres)
        offspring2[slice_start:slice_end] = parent2.__repres[slice_start:slice_end]

        # Fill in remaining cities from parent 2
        parent2_index = 0
        parent1_index = 0
        for i in range(len(self.__repres)):
            while offspring1[i] == -1:
                if parent2.__repres[parent2_index] not in offspring1:
                    offspring1[i] = parent2.__repres[parent2_index]
                parent2_index += 1

            while offspring2[i] == -1:
                if self.__repres[parent1_index] not in offspring2:
                    offspring2[i] = self.__repres[parent1_index]
                parent1_index += 1

        off1 = Chromosome(self.__param)
        off2 = Chromosome(self.__param)
        off1.__repres = offspring1 
        off2.__repres = offspring2

        return off1, off2
    

    def mutate(self):
        i = randint(0, self.__param['nodes']-1)
        j = randint(0, self.__param['nodes']-1)
        self.__repres[i], self.__repres[j] = self.__repres[j], self.__repres[i]
        
    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
    
    def __lt__(self, c):
        return self.__fitness < c.__fitness
    
    def __copy__(self):
        newchromosome = Chromosome(self.__param)
        newchromosome.fitness = self.fitness
        newchromosome.repres = self.repres
        return newchromosome
    