'''
Script for solving the Knapsack problem using Memoization and Recursion
Time complexity = O(N*W)
Space complexity = O(2*W)
'''

# Import Required Packages
import numpy as np

# Knapsack-iterative solution
def knapsack(capacity, items, values, weights):
    K_array = np.zeros((2, capacity + 1))
    for i in range(items+1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K_array[i % 2, w] = 0
            elif w< weights[i]:
                K_array[i % 2, w] = K_array[(i-1) % 2, w]
            else:
                K_array[i % 2, w] = max(K_array[(i-1) % 2, w], K_array[(i-1) % 2, w-weights[i]]+values[i])

    return K_array[items % 2, capacity]


# Read the input file
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/knapsack_big.txt", "r")
data = file.readlines()

capacity, n_items = map(int, data[0].split())

values = [int(item.split()[0]) for item in data[1:]]
weights = [int(item.split()[1]) for item in data[1:]]
weights.insert(0, 0)
values.insert(0, 0)

optimal_value = knapsack(capacity, n_items, values, weights)
print(f"Optimal Value is: {optimal_value}")

