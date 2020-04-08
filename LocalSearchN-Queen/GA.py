"""
IMPORT REQUIRED LIBRARIES
"""
#our fitness function gives number of queens attacking each other in negative
#The function testlocalSearch in file TestLocalSearch run each part 10 times and give the last output as the result only
import random
from random import randint
import math
mutation_probability= 0.5      
population_size = 400

def random_selection(problem,population):
    value = randint(0, len(population)-1)
    #sum=0
    #for k in population:
    #    sum = sum+problem.value(k)
        
    #for i in population:
    #    if ((problem.value(i))/sum) <= random.uniform(0.0, 1.0):
    #        return i
    return population[value]

def reproduce(x,y):
    child=[]
    value = randint(0, len(x)-1)
    for i in range(len(x)):
        if i<=value:
            child.append(x[i])
        else:
            child.append(y[i])
    return child

def mutate(child):
    position = randint(0, len(child)-1)
    value = randint(0, len(child)-1)
    child[position]=value
    return child
    
    
def GA(problem):
    population=[]
    for i in range(population_size):   #generating population
        population.append(problem.initial())
    # To return comma sepated tuple of positions on queens
    #Example: for 4 queens your algorithm returns (2,0,1,3)
    #limit on number of generation to end the while loop
    lim=20   
    while 1:
        #until some individual is fit enough, or enough time has elapsed
        if lim==0:
            break        
        new_population=[]
        for i in range(len(population)):
            x = random_selection(problem,population)
            y = random_selection(problem,population)
            child = reproduce(x,y)
            if mutation_probability >= random.uniform(0.0, 1.0):  #mutate probability is .3
                child = mutate(child)
            if problem.value(child)==0: #if the value of the child is perfect or some value -1 works pretty well
                print("GA value = ", problem.value(child))
                return child
            new_population.append(child)
        population.clear()
        population = new_population
        lim=lim-1
        
    best_individual=population[0]
    best_value = problem.value(best_individual)
    for j in population:
        if problem.value(j) > best_value:
            best_individual.clear()
            best_individual = j
            best_value = problem.value(j)
    print("GA value = ", problem.value(best_individual)) 
    return best_individual
        
            
        
        
    
    
    
