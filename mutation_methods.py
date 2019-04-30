'''
Created on April 18, 2019

@author: Zoya Samsonov
'''

import numpy as np
import random as r
from ind import individual

def gaussian(ind, Pm, std, x_min, x_max):
    '''Gaussian mutation with rate of success Pm. If the mutation results in
        genes outside the specified bounds, they are set equal to the nearest
        bound.
    
    Arguments:
        ind {'individual' object} -- The individual.
        Pm {float} -- The rate of mutation as a decimal probability.
        std {float} -- Standard deviation for the gaussian function.
        x_min {float} -- Minimum bound on gene values.
        x_max {float} -- Maximum bound on gene values.
    
    Returns:
        'individual' object -- The mutated individual, or None.
    '''

    if ind:
        values = []
        for x in ind.values:
            if r.random() < Pm:
                values.append(x + np.random.normal(0, std))
            else:
                values.append(x)

            #stay within bounds    
            if values[-1] < x_min:
                values[-1] = x_min
            if values[-1] > x_max:
                values[-1] = x_max

        return individual(values)
    return None

def uniform(ind, Pm, x_min, x_max):
    '''Uniform random mutation method.
        Replaces gene values regardless of current value.
    
    Arguments:
        ind {'individual' object} -- The individual.
        Pm {float} -- The rate of mutation as a decimal probability.
        x_min {float} -- Minimum bound on gene values.
        x_max {float} -- Maximum bound on gene values.
    
    Returns:
        'individual' object -- The mutated individual, or None.
    '''

    if ind:
        values = []
        for _ in ind.values:
            values.append(r.uniform(x_min, x_max))
        return individual(values)
    return None