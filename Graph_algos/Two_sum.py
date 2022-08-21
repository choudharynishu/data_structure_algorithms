'''This script is used to implement the solution for two-sum problem using Hash Tables
   Nishu Choudhary
'''

# Import Required packages
import numpy as np


def convert_int(x):
    x = x.strip("\n")
    return int(x)


def two_sum(numlist, numdict):
    start = -10000
    end = 10000
    target_count = 0
    for target in range(start - 1, end + 1):
        for num in numlist:
            if (not None == numdict.get(target - num)) & (not target-num == num):
                target_count += 1
                break

    return target_count


file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/2sum_prob.txt", "r")
data = file.readlines()
num_list = list(map(convert_int, data))

# Assuming that Python's dictionary data structure is a hash table
num_dict = {}
for index, item in enumerate(num_list):
    num_dict[item] = index

count = two_sum(num_list, num_dict)
print(count)
