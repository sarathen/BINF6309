#!/usr/bin/env python3
# fibonacci.py

def population(k,n):
    '''Find the population size at day, n given reproduction rate, k.'''
    #Initialize array to store population size for each reproduction rate
    pop_by_rate = [0] * (n + 1)
    
    for i in range(1, n + 1):
        population = -1*float('Inf')

        for j in range(i):
            population = max(population, k[j] + pop_by_rate[i-j-1])
            
            pop_by_rate[i] = population
        return pop_by_rate[n]

if __name__ == "__main__":
    print("{}\t{}".format(n, population[n]))

