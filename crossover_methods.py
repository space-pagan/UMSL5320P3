'''
Created on April 18, 2019

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

def arithmatic(Parents, n, Pc, weight):
    '''Arithmatic crossover. Each gene is calculated as ax[i] + (1-a)y[i].
    
    Arguments:
        Parents {2-tuple of class 'individual'} -- The parents.
        n {int} -- The genome length
        Pc {float} -- The rate of success as a decimal propbability.
        weight {float} -- The weight that the first parent's genes have.
            0.5 will result in each parent contributing equally.
    
    Returns:
        'individual' object -- The child, or None.
    '''

    if r.random() < Pc:
        child_values = []
        for i in range(n):
            child_values.append( (weight * Parents[0].values[i]) + \
                ((1-weight) * Parents[1].values[i]) )
        return individual(child_values)
    return None