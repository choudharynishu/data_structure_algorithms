'''
   Script for solving the Knapsack problem using pure recursion
   Time complexity = O(2^n)
   Space complexity =  O(n)
'''

#Import Required Packages
import numpy as np

def knapsack(residual_capacity, items):
    #print(f"For this call residual capacity = {residual_capacity}, items = {items}")
    #Base case
    if items == 0 or residual_capacity == 0:
        return 0
    elif residual_capacity < weights[items]:
        return knapsack(residual_capacity, items-1)
    else:
        return max(knapsack(residual_capacity, items-1),
                   knapsack(residual_capacity-weights[items], items-1)+values[items])


#Read the input file
#Reading the number of characters and their respective weights
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/knapsack1.txt", "r")
data = file.readlines()

capacity, n_items = map(int, data[0].split())

values = [int(item.split()[0]) for item in data[1:]]
weights = [int(item.split()[1]) for item in data[1:]]
weights.insert(0, 0)
values.insert(0, 0)
optimal_value = knapsack(capacity, n_items)
print(optimal_value)

