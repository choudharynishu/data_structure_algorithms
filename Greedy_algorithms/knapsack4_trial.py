'''
Script for solving the Knapsack problem using Memoization and Recursion
Time complexity = O(N*W)
Space complexity = O(W)
'''


def knapSack(capacity, weights, values, n_items):
    current_col = [0 for i in range(capacity + 1)]  # Making the dp array
    #By this we are implicitly copying last column's value into the next column
    #Both columns are not reserved
    for i in range(1, n_items + 1):  # taking first i elements
        for x in range(capacity, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if weights[i] <= x:
                # finding the maximum value
                current_col[x] = max(current_col[x], current_col[x - weights[i]] + values[i])
    return current_col[capacity]  # returning the maximum value of knapsack

# Read the input file
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/knapsack1_testcase2.txt", "r")
data = file.readlines()

capacity, n_items = map(int, data[0].split())

values = [int(item.split()[0]) for item in data[1:]]
weights = [int(item.split()[1]) for item in data[1:]]
values.insert(0, 0)
weights.insert(0, 0)
print(knapSack(capacity, weights, values, n_items))