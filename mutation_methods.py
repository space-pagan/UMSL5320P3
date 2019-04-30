'''
Created on April 30, 2019

@author: Zoya Samsonov
'''

import random as r
from ind import individual

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
        for v in ind.values:
            if r.random() < Pm:
                values.append(r.choice([0,1]))
            else:
                values.append(v)
        return individual(values)
    return None