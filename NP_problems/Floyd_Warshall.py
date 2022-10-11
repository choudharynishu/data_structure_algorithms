'''This script is an implementation of Floyd-Warshall Algorithm to compute All Pairs Shortest Path
   Running Time = O(n^3)
'''

import numpy as np
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = {}  #revisit this - if we don't ever end up using non-existent edge maynot need this

    #Function to define an edge using u,v where the edge is point from u to v
    def addEdge(self, u, v, c):
        self.graph[u, v] = c

#Imput file
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/graph1.txt", "r")
data = file.readlines()

n_vertices, n_edges = map(int, data[0].split())
g = Graph()

for index, line in enumerate(data[1:]):

    head, tail, cost = map(int, line.split()) #Keeping it as a string for now
    g.addEdge(head, tail, cost)

#Initialize the A matrix
A = np.zeros((n_vertices, n_vertices, n_vertices)) #Dimension should be (n_vertices , n_vertices, n_vertices+1)

#Define base case for k =0

for i in range(n_vertices):
    for j in range(n_vertices):

        #Check if a direct edge (i,j) exists
        if i ==j :
            A[i, j, 0] = 0
        else:
            try:
                A[i, j, 0] = g.graph[(i+1,j+1)]
            except KeyError:
                A[i, j, 0] = np.inf

#Loop through all values of (i,j,k)
for k in range(1, n_vertices):
    for i in range(n_vertices):
        for j in range(n_vertices):
                A[i, j, k] = min(A[i, j, k-1], A[i, k, k-1]+A[k, j, k-1])

print(f"Does negative cost cycle exists: { not all(np.diagonal(A[:, :, n_vertices-1])>0)}")
print(np.min(A[:, :, n_vertices-1]))


