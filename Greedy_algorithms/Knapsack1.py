'''
   Script for solving the Knapsack problem using Dynamic Programming
   Data Structure & Algorithms: Greedy algorithms and Dynamic Programming (Iterative version)
   Time complexity = O(N*W)
   Space complexity = O(N*W)
'''

#Import Required Packages
import numpy as np
#Read the input file
#Reading the number of characters and their respective weights
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/knapsack_big.txt", "r")
data = file.readlines()

capacity, n_items = map(int, data[0].split())

values = [int(item.split()[0]) for item in data[1:]]
weights = [int(item.split()[1]) for item in data[1:]]
weights.insert(0, 0)
values.insert(0, 0)

A = np.empty((n_items+1, capacity+1))
#Intialize first row of 'A' matrix to be equal to zero
A[0, :] = 0

for i in range(1,n_items+1):
    for x in range(capacity+1):
        A[i, x] = max(A[i-1, x], A[i-1, max(x-weights[i], 0)]+(values[i]*(x >= weights[i])))
print(f"Optimal value is {np.amax(A)}")