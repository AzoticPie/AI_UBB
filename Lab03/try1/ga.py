from .chromosome import Chromosome
from random import randint

# netSize(int)
class GA:
    def __init__(self, param) -> None:
        self.__param = param
        self.__size = param['netSize']//10
        self.__population = [Chromosome(self.__param['chromosomeParam']) for _ in range(self.__size)]

    @property
    def population(self):
        return self.__population
    
    @population.setter 
    def population(self, pop):
        self.__population = pop 
    
    def evaluatePopulation(self):
        for c in self.__population:
            c.fitness = self.__param['function'](self.__param['network'], c.repres)

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best
        
    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best
    
    def averageFitness(self):
        avg = 0.0
        for c in self.__population:
            avg += c.fitness
        return avg/self.self.__size

    def chromosomeSelection(self):
        pos1 = randint(0, self.self.__size - 1)
        pos2 = randint(0, self.self.__size - 1)
        if (self.__population[pos1] < self.__population[pos2]):
            return pos1
        else:
            return pos2 

    def __reproduce(self):
        for _ in range(self.self.__size):
            p1 = self.__population[self.chromosomeSelection()]
            p2 = self.__population[self.chromosomeSelection()]
            off = p1.crossover(p2)
            self.population.append(off)

    def __mutate(self):
        for c in self.__population:
            c.mutation()

    def __natSelection(self):
        self.population = sorted(self.population)[self.__size:]

    def nextGeneration(self):
        self.__reproduce()
        self.__mutate()
        self.__natSelection()