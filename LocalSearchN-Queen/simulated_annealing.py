"""
IMPORT REQUIRED LIBRARIES
"""
import random
import math
import sys

# You've got to tune these parameters carefully before you can make it work
def schedule(t):
    # Parameters must be tuned according to the size of the input
	# k decides the time span of random walk
	# lambda decides how steep does the probability converges to zero
	# limit decides the number of iterations
    #return lambda t:
    """
    #y=mx+c slope is negative coz the schedule is mapping of time to temperature
    #so as time goes on the temperature should decrease
    #limit can be the intercept 
    #let slope be lam ,(can try it being -1 for uniformity)
    #k can be the input time??
    
    ////
    k decides the strides of the ccurve
    lambda defines the shape of the temperature decay
    limit defines number of iterations
    
    YOUR CODE HERE
    """ 
    k=3
    lam=-1
    limit=4000
    
    return ((lam*t)+limit)

def simulated_annealing(problem):
    # To return comma sepated tuple of positions on queens
    #Example: for 4 queens your algorithm returns (2,0,1,3)
    """
    YOUR CODE HERE
    """
    current = problem.initial()
    if(problem.goal_test(current)):
        print("Simulated Annealing value = ", problem.value(current))
        return current
    t=1
    while 1:
        currentValue = problem.value(current)
        T=schedule(t)
        t=t+1
        if T==0:
            print("Simulated Annealing value = ", problem.value(current))
            return current
        successor = problem.random_child(current)
        if(len(successor)==0):
            print("Simulated Annealing value = ", problem.value(current))
            return current
        succ_Value= problem.value(successor)
        delta = succ_Value-currentValue
        if delta > 0 or math.exp(delta / T) > random.uniform(0.0, 1.0):
            current = successor
      
    
