'''
Script for solving the Knapsack problem using Memoization and Recursion
Time complexity = O(N*W)
Space complexity = O(W)
'''


def knapSack(W, wt, val, n):
    dp = [0 for i in range(W + 1)]  # Making the dp array

    for i in range(1, n + 1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i - 1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

    return dp[W]  # returning the maximum value of knapsack

# Read the input file
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/knapsack_big.txt", "r")
data = file.readlines()

capacity, n_items = map(int, data[0].split())

values = [int(item.split()[0]) for item in data[1:]]
weights = [int(item.split()[1]) for item in data[1:]]

print(knapSack(capacity, weights, values, n_items))