"""
IMPORT REQUIRED LIBRARIES
"""

def hill_climbing(problem):
    # To return comma sepated tuple of positions on queens
    #Example: for 4 queens your algorithm returns (2,0,1,3)
    """
    YOUR CODE HERE
    """
    current=problem.initial()
    while 1:
        successor = problem.children(current)            
        if(len(successor)==0):
            print("HillClimbing value = ", problem.value(current))
            return current
       
        largest = successor[0]
        largestValue= problem.value(largest)
        for statess in successor:
            if problem.value(statess)>largestValue:
                largest = statess
                largestValue = problem.value(statess)
                
        if largestValue <= problem.value(current):
            print("HillClimbing value = ", problem.value(current))
            return current
        else:
            current = largest
        
    

