'''This script is an implementation for the solution of the Traveling Salesman Problem
   Running Time = O(n^2*2^)
'''

#Import Required Packages
import time
import math
import itertools
import numpy as np


def euclidean_dist(x,y):
    x1, x2 = x
    y1, y2 = y
    return np.sqrt((x1-y1)**2+(x2-y2)**2)

# Import and read the input file
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/TSP.txt", "r")
data = file.readlines()

location = {}

for index, item in enumerate(data):
    if index == 0:
        n_cities = int(data[index])
    else:
        location[index] = tuple(map(float, data[index].split()))

# Create a distance matrix for each pair of cities
city_list = range(1, n_cities+1)
# *This is creating directional edges, waste of space
pairwise_combinations = list(itertools.combinations(city_list, 2))

start = time.perf_counter()
distance = {}
for i, j in pairwise_combinations:
    distance[(i, j)] = euclidean_dist(location[i], location[j])


# Create the basecase of j=1, set object S = [1] and otherwise
base_sizes = list(range(1, n_cities+1))
A = {}
for s in base_sizes:
    set_S = list(filter(lambda x: 1 in x, itertools.combinations(city_list, s)))
    A.update({(key, 1): np.inf for key in set_S})
A[(1,), 1] = 0

# Iterate through all possible set S memberships and final destination j combinations
s_sizes = list(range(2,n_cities+1))     #Variable that controls the size of set S
for s in s_sizes:
    set_S = list(filter(lambda x: 1 in x, itertools.combinations(city_list, s)))
    for S in set_S:
        set_j = list(filter(lambda x: not x ==1, itertools.chain(*itertools.combinations(S, 1))))
        for j in set_j:
            S_notj = S[:S.index(j)] + S[S.index(j) + 1:]
            A[S, j] = min([A[S_notj, k] + distance[tuple(sorted((j, k)))] for k in S_notj])
        


complete_S = tuple(range(1, n_cities+1))
# Return the minimum length tour
min_tour_value = min([A[complete_S, j]+distance[1,j] for j in range(2,n_cities+1)])
print(math.floor(min_tour_value))

