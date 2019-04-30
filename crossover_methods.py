'''
Created on April 30, 2019

@author: Zoya Samsonov
'''

import random as r
from ind import individual

def single_point(Parents, n, Pc):
    '''Single point crossover with rate of success = Pc
    
    Arguments:
        Parents {2-tuple of class 'individual'} -- The parents.
        n {int} -- The genome length
        Pc {float} -- The rate of success as a decimal propbability.
    
    Returns:
        'individual' object -- The child, or None.
    '''

    if r.random() < Pc:
        child_values = []
        crosspoint = r.randint(0, n)
        for i in range(n):
            if i < crosspoint:
                child_values.append(Parents[0].values[i])
            else:
                child_values.append(Parents[1].values[i])
        return individual(child_values)
    return None #regenerate parent pair

def two_point(Parents, n, Pc):
    '''Two point crossover. Same as single point except a second crossover
        point is calculated where the genome goes back to the first parent.
    
    Arguments:
        Parents {2-tuple of class 'individual'} -- The parents.
        n {int} -- The genome length
        Pc {float} -- The rate of success as a decimal propbability.
    
    Returns:
        'individual' object -- The child, or None.
    '''

    if r.random() < Pc:
        child_values = []
        crosspoint1 = r.randint(0, n)
        crosspoint2 = r.randint(crosspoint1, n)
        for i in range(n):
            if i < crosspoint1:
                child_values.append(Parents[0].values[i])
            elif i >= crosspoint1 and i < crosspoint2:
                child_values.append(Parents[1].values[i])
            else:
                child_values.append(Parents[0].values[i])
        return individual(child_values)
    return None #regenerate parent pair