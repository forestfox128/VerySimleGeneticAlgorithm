import random as random
import numpy as np

def createInitialPopulation(populationSize):
    population = []

    for i in range(populationSize):
        individual = -10+20*random.random()
        population.append(individual)
    
    return population


def fitnessFunction(individual):
    f = pow((individual - 5),2) + 10
    return f


def sortPopulation(population):
    newPopul = [population[0]]
    for i in range(1,len(population)):
        ff = fitnessFunction(population[i])
        for j in range(len(newPopul)):
            pos = len(newPopul)
            if ff < fitnessFunction(newPopul[j]):
                pos = j
                break
        newPopul.insert(pos, population[i])
    return newPopul

def parentSelection(population):
    weights = []
    for i in range(len(population)):
        weights.append((len(population)-i)*random.random())

    if(weights[0] >= weights[1]):
        maxInd1 = 0
        maxInd2 = 1
    else:
        maxInd1 = 1
        maxInd2 = 2
    
    for i in range(2,len(population)):
        if weights[i] > weights[maxInd1]:
            maxInd2 = maxInd1
            maxInd1 = i
        elif weights[i] < weights[maxInd2]:
            maxInd2 = i
    
    return population[maxInd1], population[maxInd2]

def crossOver(x1,x2):
    r = np.random.random(1)
    
    y1 = r*x1 + (1-r)*x2
    y2 = (1-r)*x1 + r * x2

    return y1, y2

def mutate(x,b):
    rand = random.random()
    
    if rand < 0.25:
        x1 = x - 0.25
    else:
        x1 = x + 0.25
    return x1

def oneStep(population):
    b = 0.5
    newPopulation = []
    population = sortPopulation(population)

    for i in range(int(round(len(population))/2)):
        par1, par2 = parentSelection(population)
        ch1, ch2 = crossOver(par1, par2)
        ch1 = mutate(ch1,b)
        ch2 = mutate(ch2,b)
        newPopulation.append(ch1)
        newPopulation.append(ch2)
    newPopulation1 = sortPopulation(newPopulation)
    return newPopulation1

maxIter = 100
populationSize = 100
individualSize = 7
population = createInitialPopulation(populationSize)
# print("population")
# print(population)

for i in range(0, maxIter):
    newPopulation = oneStep(population)
    population = newPopulation

print("minimum = " + str(population[0]))

