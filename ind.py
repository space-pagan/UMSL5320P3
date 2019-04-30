'''
Created on April 30, 2019

@author: Zoya Samsonov
'''

import random as r

class individual:
    '''Implements an individual in a genetic algorithm using binary coding
    
    Arguments:
        values {binary interable} -- Initial values for the individual.
        If None, provide the desired value list length.
        Ex: individual([1, 0, 1]) or individual(None, 3)
    '''
    def __init__(self, values, *args):
        #params should be (x_len)
        if values == None:
            values = []
            for _ in range(args[0]):
                values.append(r.choice([0,1]))

        self.values = values
        self.p = 0
        self.w = self.v = self.__f = 0

    @property
    def f(self):
        if self.__f:
            return self.__f
        self.w, self.v, self.__f = fitness(self.values)
        return self.__f

    def __repr__(self):
        return str(self.values) + '\tw: '+str(self.w)+'\tv: '+str(self.v)+'\tf: '+'%5.3f' % self.f

evals = 0
weights = []
kvalues = []
W = 0

def penalty(weight):
    if weight > W:
        dif = weight - W
        return 2**dif
    else:
        return 0

def fitness(values):
    '''Calculates an adjusted fitness value such that if minimizing,
        the best fitness has a greater absolute value than the worst.
    
    Arguments:
        values {numerical iterable} -- The geneone of the individual for which
            to compute a fitness.
    
    Returns:
        float -- The fitness value
    '''

    global evals
    evals += 1

    wtotal = 0
    vtotal = 0
    
    for i, j in enumerate(values):
        if j:
            wtotal += weights[i]
            vtotal += kvalues[i]

    w2 = wtotal + penalty(wtotal)
    w2 = W if w2 < W else w2 #there should be no benefit for not including the entire weight
    return wtotal, vtotal, vtotal / w2 #maximize values, minimize weight