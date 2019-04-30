'''
Created on April 30, 2019

@author: Zoya Samsonov
'''

import sample_methods as sm
import crossover_methods as cm
import mutation_methods as mm
import ind
from ind import individual
import statistics
import sys

#global variables:

#Population size:
N = 10
#value bounds:
x_min = 0
x_max = 1
n = 20
ind.W = 50
ind.weights = [1,1,2,2,3,4,4,4,4,5,5,7,7,8,8,8,9,9,10,10]
ind.kvalues = [18,29,7,2,6,15,25,21,14,19,3,16,28,9,1,10,17,27,11,12]
#crossover:
Pc = 0.8
#mutation:
Pm = 0.05
#ranking minimum expectation:
rank_min = 0.1
#truncate n elements:
loss = 2
#other:
max_generations = 50

def distr(P, method):
    '''Select different distribution methods to apply to the population, P.
    Strings that will be parsed:
        'RWS' - Roulette Wheel Selection. Use with 'p_sample'
        'rank' - Rank selection as controlled by rank_min. Use with 'p_sample'
        'truncate' - Discard the worst n individuals as controlled by loss.
            No proportional value is calculated, only use with 'tournament'
        '*' - any method not listed above will not perform distribution,
            and therefore not calculate a p value. Use only w/ 'tournament'
    
    Arguments:
        P {iterable of class individual} -- The population collection object
        method {str} -- A selector string for specific distribution methods.
    '''
    
    if method == 'RWS':
        sm.RWS(P)
    elif method == 'rank':
        sm.rank(P, rank_min)
    elif method == 'truncate':
        sm.truncate(P, loss)

def sample(P, method):
    '''Selects different sampling methods to apply to the population, P.
    Strings that will be parsed:
        'tournament' - tournament sampling with two random individuals.
        'p_sample' - proportional sampling using calculated p values.
            Only works with distribution methods RWS and rank
    
    Arguments:
        P {iterable of class individual} -- The population collection object
        method {str} -- A selector string for the specific sampling methods.
    
    Returns:
        individual -- An object of class individual, as determined by the
            sampling method.
    '''

    if method == 'tournament':
        return sm.tournament_sample2(P)
    elif method == 'p_sample':
        return sm.p_sample(P)
    else:
        return

def cross(P, method):
    '''Selects different crossover methods to apply to a two-individual tuple.
    All crossover methods succeed with a rate of Pc, and return None otherwise.
    Strings that will be parsed:
        'single_point' - Crossover point randomly selected
        'two_point' - Two crossover points randomly selected.
    
    Arguments:
        P {'individual' tuple} -- Two 'individual' objects passed as a tuple.
        method {str} -- A selector string for the specific crossover methods.
    
    Returns:
        individual -- An object of class individual, as determined by the
            crossover method.
    '''

    if method == 'single_point':
        return cm.single_point(P, n, Pc)
    elif method == 'two_point':
        return cm.two_point(P, n, Pc)
    else:
        return None

def mut(P, method):
    '''Selects different mutation methods to apply to the population, P.
    All mutation methods have a Pm rate of success, and return None otherwise.
    Strings that will be parsed:
        'uniform' - sets x to a unifrom random value from x_min to x_max.
    
    Arguments:
        P {'individual' object} -- An 'individual' object.
        method {str} -- A selector string for the specific mutation methods.
    
    Returns:
        individual -- An object of class individual, as determined by the
            mutation method.
    '''

    if method == 'uniform':
        return mm.uniform(P, Pm, x_min, x_max)
    else:
        return None

def single_run(fdistr='RWS', fsamp='p_sample', fcross='single_point', fmut='uniform'):
    '''Driver for a single run of the GA. Genetic manipulation methods can be
        left blank or supplied for varying outcomes.
    
    Arguments:
        fdistr {str} -- RWS or distribution method if provided.
        fsamp {str} -- Proportional or sampling method if provided.
        fcross {str} -- Single-Point or crossover method if provided.
        fmut {str} -- Uniform or mutation method if provided.
    
    Returns:
        'individual' object -- The best-of-run individual.
    '''

    #initialize
    best_of_run = individual([0]*n) #start with worst
    gen_count = 1
    P = []
    while len(P) < N:
        P.append(individual(None, n))

    while gen_count <= max_generations:
        print('GENERATION', gen_count)
        distr(P, fdistr) #calculate distribution
        for i in P: #check if any are better than current BOR.
            print(i)
            if i.f > best_of_run.f:
                best_of_run = i
        print('\n\n')
        P_next = []
        while len(P_next) < N: #build next generation
            i = mut(cross( (sample(P, fsamp), sample(P, fsamp)), fcross), fmut)
            if i: #if not None
                P_next.append(i)

        gen_count += 1
        P = P_next

    print('Total evaluations:', ind.evals)
    return best_of_run

if __name__ == "__main__":
    dmethod = 'RWS'
    smethod = 'p_sample'
    cmethod = 'single_point'
    mmethod = 'uniform'
    multi_run = 0

    if len(sys.argv) > 1:
        multi_run = int(sys.argv[1])
    if len(sys.argv) > 2:
        dmethod = sys.argv[2]
    if len(sys.argv) > 3:
        smethod = sys.argv[3]
    if len(sys.argv) > 4:
        cmethod = sys.argv[4]
    if len(sys.argv) > 5:
        mmethod = sys.argv[5]

    if multi_run:
        best_of_run_data = []
        for _ in range(multi_run):
            best_of_run_data.append(single_run(dmethod, smethod, cmethod, mmethod))
            ind.evals = 0 #reset eval counter
        for i in best_of_run_data:
            print(i)
        best_of_run_fit = [i.pure_fit for i in best_of_run_data]
        print('Average of BORs is', sum(best_of_run_fit)/len(best_of_run_fit))
        print('Standard Deviation of BORs is', statistics.pstdev(best_of_run_fit))
    else:
        bor = single_run(dmethod, smethod, cmethod, mmethod)
        print('Best individual in run is', bor)
    print('Best possible solution is', '[1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0]\tw: 50\tv: 221\tf: 4.420')