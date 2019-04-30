'''
Created on April 18, 2019

@author: Zoya Samsonov
'''

import random as r

def RWS(Population):
    '''Roulette Wheel Selection, calculates the proportional fitness for each
        individual in the population.
    
    Arguments:
        Population {iterable of class 'individual'} -- The population.
    '''

    fsum = sum([i.f for i in Population])
    for i in Population:
        i.p = i.f / fsum

def p_sample(Population):
    '''Samples any population where proportional fitness has been calculated.
        Every individual's chance of being selected is equal to its
        proportional fitness value.
    
    Arguments:
        Population {iterable of class 'individual'} -- The population.
    
    Returns:
        'individual' object -- The sampled individual.
    '''

    rand = r.random()
    s = 0
    i = 0
    while s < rand:
        s += Population[i].p
        i += 1
    return Population[i-1] if i > 0 else Population[0]

def tournament_sample2(Population):
    '''Samples any population by selecting two random individuals and returning
        the one with better fitness.
    
    Arguments:
        Population {iterabe of class 'individual'} -- The population.
    
    Returns:
        'individual' object -- The sampled individual.
    '''

    i1 = Population[r.randint(0, len(Population)-1)]
    i2 = Population[r.randint(0, len(Population)-1)]
    return i1 if i1.f > i2.f else i2

def rank(Population, min_occurance):
    '''Calculates each individual's proportional fitness as a linear function
        of its rank.
    
    Arguments:
        Population {iterable of class 'individual'} -- The population.
        min_occurance {float} -- The expected occurence of the worst rank.
    '''

    max_occurence = 2-min_occurance
    N = len(Population)
    Population.sort(key = lambda x: x.f)
    for i, j in enumerate(Population):
        j.p = (((max_occurence-min_occurance)/(N-1))*i + min_occurance)/N

def truncate(Population, loss):
    '''Sorts and discards the worst loss individuals.
    
    Arguments:
        Population {iterable of class 'individual'} -- The population.
        loss {int} -- The number of individuals to truncate.
    '''

    Population.sort(key = lambda x: x.f)
    while loss > 0:
        Population.pop(0)
        loss -= 1