from random import uniform
from random import randint

def generateNewValue(lim1, lim2):
    return int(uniform(lim1, lim2+1))

class Chromosome:
    def __init__(self, problParam = None) -> None:
        self.__param = problParam
        self.__repres = [generateNewValue(1, problParam['max']) for _ in range(self.__param['noDim'])]
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
        if self.__param['seedcrossover'] == 1:
            r = randint(0, len(self.__repres) - 1)
            newrepres = []
            for i in range(r):
                newrepres.append(self.__repres[i])
            for i in range(r, len(self.__repres)):
                newrepres.append(c.__repres[i])
            offspring = Chromosome(c.__param)
            offspring.repres = newrepres
            return offspring
        
        elif self.__param['seedcrossover'] == 2:
            newrepres = []
            for i in range(self.__param['noDim']):
                if(randint(1,2)%2 == 0):
                    newrepres.append(self.__repres[i])
                else:
                    newrepres.append(c.__repres[i])
            offspring = Chromosome(c.__param)
            offspring.repres = newrepres
            return offspring

    def mutation(self):
        if self.__param['seedmutation'] == 1:
            pos = randint(0, self.__param['noDim'] - 1)
            self.__repres[pos] = generateNewValue(1, self.__param['max'])

        elif self.__param['seedmutation'] == 2:
            for _ in range(self.__param['noDim']//5+1):
                pos = randint(0, self.__param['noDim'] - 1)
                self.__repres[pos] = generateNewValue(1, self.__param['max'])

        elif self.__param['seedmutation'] == 3:
            n1 = generateNewValue(1, self.__param['max'])
            n2 = generateNewValue(1, self.__param['max'])
            aux = self.__repres[n1]
            self.__repres[n1] = self.__repres[n2]
            self.__repres[n2] = aux
            
        elif self.__param['seedmutation'] == 4:
            for _ in range(self.__param['noDim']//5+1):
                n1 = generateNewValue(1, self.__param['max'])
                n2 = generateNewValue(1, self.__param['max'])
                aux = self.__repres[n1]
                self.__repres[n1] = self.__repres[n2]
                self.__repres[n2] = aux
        
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
    