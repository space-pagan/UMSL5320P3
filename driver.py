'''
Created on April 18, 2019

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
x_min = -1.0
x_max = 5.0
n = 3
#crossover:
Pc = 0.8
#mutation:
Pm = 0.1
std = 0.02
#ranking minimum expectation:
rank_min = 0.1
#truncate n elements:
loss = 2
#arithmetic weight:
weight = 0.3
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
        'arithmatic' - ax1 + (1-a)y1 where a is controlled by weight.
    
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
    elif method == 'arithmatic':
        return cm.arithmatic(P, n, Pc, weight)
    else:
        return None

def mut(P, method):
    '''Selects different mutation methods to apply to the population, P.
    All mutation methods have a Pm rate of success, and return None otherwise.
    Strings that will be parsed:
        'gaussian' - x = x + gaussian(0, std)
        'uniform' - sets x to a unifrom random value from x_min to x_max.
    
    Arguments:
        P {'individual' object} -- An 'individual' object.
        method {str} -- A selector string for the specific mutation methods.
    
    Returns:
        individual -- An object of class individual, as determined by the
            mutation method.
    '''

    if method == 'gaussian':
        return mm.gaussian(P, Pm, std, x_min, x_max)
    elif method == 'uniform':
        return mm.uniform(P, Pm, x_min, x_max)
    else:
        return None

def single_run(fdistr='RWS', fsamp='p_sample', fcross='single_point', fmut='gaussian'):
    '''Driver for a single run of the GA. Genetic manipulation methods can be
        left blank or supplied for varying outcomes.
    
    Arguments:
        fdistr {str} -- RWS or distribution method if provided.
        fsamp {str} -- Proportional or sampling method if provided.
        fcross {str} -- Single-Point or crossover method if provided.
        fmut {str} -- Gaussian or mutation method if provided.
    
    Returns:
        'individual' object -- The best-of-run individual.
    '''

    #initialize
    best_of_run = individual([x_max, x_max, x_max]) #start with worst
    gen_count = 1
    P = []
    while len(P) < N:
        P.append(individual(None, n, x_min, x_max))

    while gen_count < max_generations:
        distr(P, fdistr) #calculate distribution
        for i in P: #check if any are better than current BOR.
            if i.f > best_of_run.f:
                best_of_run = i
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
    mmethod = 'gaussian'
    mutli_run = 0
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