'''Performance comparison of the two implementations for the Knapsack problem'''

import timeit

# code snippet to be executed only once
mysetup = '''
import numpy as np
file = open(f'/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/knapsack1.txt', 'r')
data = file.readlines()
capacity, n_items = map(int, data[0].split())
values = [int(item.split()[0]) for item in data[1:]]
weights = [int(item.split()[1]) for item in data[1:]]
weights.insert(0, 0)
values.insert(0, 0)
'''

# code snippet whose execution time is to be measured
mycode = '''
def knapsack(capacity, n_items, values, weights):
    K_array = np.zeros((2, capacity + 1))
    for i in range(n_items+1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K_array[i % 2, w] = 0
            elif w< weights[i]:
                K_array[i % 2, w] = K_array[(i-1) % 2, w]
            else:
                K_array[i % 2, w] = max(K_array[(i-1) % 2, w], K_array[(i-1) % 2, w-weights[i]]+values[i])

    return K_array[n_items % 2, capacity]
'''
mycode2 = '''
A = np.empty((n_items+1, capacity+1))
#Intialize first row of 'A' matrix to be equal to zero
A[0, :] = 0

for i in range(1,n_items+1):
    for x in range(capacity+1):
        A[i, x] = max(A[i-1, x], A[i-1, max(x-weights[i], 0)]+(values[i]*(x >= weights[i])))
'''
mycode3 = '''
def knapSack(capacity, weights, values, n_items):
    dp = [0 for i in range(capacity + 1)]  # Making the dp array

    for i in range(1, n_items + 1):  # taking first i elements
        for w in range(capacity, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if weights[i] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[W] 
'''
# timeit statement
print(timeit.timeit(setup=mysetup,
                    stmt=mycode,
                    number=2))
print(timeit.timeit(setup=mysetup,
                    stmt=mycode2,
                    number=2))
print(timeit.timeit(setup=mysetup,
                    stmt=mycode3,
                    number=2))