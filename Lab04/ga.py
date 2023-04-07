from chromosome import Chromosome
from random import randint
from random import sample
from utils import insertCh
import threading

class GA:
    def __init__(self, param) -> None:
        self.__param = param;
        self.__noThreads = 4;
        self.__population = [Chromosome(self.__param['chromosome_param']) for _ in range(param['pop_size'])]

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
            if (c.fitness < best.fitness):
                best = c
        return best
        
    def worstChromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if (c.fitness > worst.fitness):
                worst = c
        return worst
    
    def averageFitness(self):
        avg = 0.0
        for c in self.__population:
            avg += c.fitness
        return avg/self.__param['pop_size']

    def chromosomeSelection(self):
        pos1 = randint(0, self.__param['pop_size'] - 1)
        pos2 = randint(0, self.__param['pop_size'] - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2 
        
    def tournament_selection(self, tournament_size = 100):
        parents = []
        for i in range(2):
            tournament = sample(self.__population, tournament_size)
            winner = min(tournament, key=lambda x: x.fitness)
            parents.append(winner)
        return parents
    
    def __reproduce(self):
        for _ in range(self.__param['pop_size']*10):
            p1, p2 = self.tournament_selection()
            off1, off2 = p1.order_crossover(p2)
            off1.mutate()
            off2.mutate()
            off1.fitness = self.__param['function'](self.__param['network'], off1.repres)
            off2.fitness = self.__param['function'](self.__param['network'], off2.repres)

            self.__population.append(off1)
            self.__population.append(off2)


    def __reproduce_steady(self):
        for _ in range(self.__param['pop_size']*10):
            p1, p2 = self.tournament_selection()
            off1, off2 = p1.order_crossover(p2)
            off1.mutate()
            off2.mutate()
            off1.fitness = self.__param['function'](self.__param['network'], off1.repres)
            off2.fitness = self.__param['function'](self.__param['network'], off2.repres)

            worst = self.worstChromosome()

            if (off1.fitness > worst.fitness):
                self.__population.remove(worst)
                self.__population.append(off1)
                worst = self.worstChromosome()

            if (off2.fitness > worst.fitness):
                self.__population.remove(worst)
                self.__population.append(off2)

    def __reproduceThd(self, offsprings):
        newPop = []
        for _ in range(self.__param['pop_size']*20//self.__noThreads):
            p1 = self.__population[self.tournament_selection()]
            p2 = self.__population[self.tournament_selection()]
            off = p1.crossover(p2)
            newPop.append(off)
        offsprings.append(off)

    def __mutate(self, rate = 0.9):
        for c in self.__population:
            if randint(1,10)/10 <= rate:
                c.mutate()

    def __mutateThd(self):
        for _ in range(len(self.population)):
            pass

    def __natSelection(self):
        new_pop = []
        for ch in self.__population:
            insertCh(new_pop, self.__param['pop_size'], ch)
        self.__population = new_pop

    def nextGeneration(self):
        # threads = []
        # offsprings = []
        # for i in range(self.__noThreads):
        #     thd = threading.Thread(target=self.__reproduceThd, args=(offsprings))
        #     threads.append(thd)
        # for thd in threads:
        #     thd.start()
        # for thd in threads:
        #     thd.join()

        # for off in offsprings:
        #     for ch in off:
        #         self.__population.append(ch)
        self.__reproduce()
        self.__mutate()
        self.__natSelection()
        self.evaluatePopulation()

    def oneGen(self):
        self.__reproduce_steady()