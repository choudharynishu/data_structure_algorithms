'''This is a naïve implmentation of Prim's Algorithm to compute the Minimum Spanning Tree(MST) for a given graph
   Runtime: O(mn)
   Nishu Choudhary
   06/27/2022
'''
#Import Required packages
from collections import defaultdict

class Graph:
    def __init__(self, vertices=None):
        self.vertices = vertices #Initialize this but add value to this later
        self.graph = defaultdict(list)  #default dictionary to store graph

    #Function to define an edge using u,v where the edge is point from u to v
    def addEdge(self, u, v):
        self.graph[u].append(v)

#Implementation of Prim's algorithm
def prims(g):
    #Initialize cost to a very high number
    mst_cost = 0
    n_vertices = g.vertices
    mst = Graph(n_vertices)

    visited = [False] * n_vertices
    visited[0] = True
    frontier_nodes = [1]

    while not all(visited):
        potential_outgoing_arcs = [(node, end, cost) for node in frontier_nodes for end, cost in g.graph[node] if
                         not visited[end - 1]]

        next_arc = min(potential_outgoing_arcs, key=lambda t: t[2])
        mst_cost += next_arc[2]
        mst.addEdge(next_arc[0], next_arc[1:])
        visited[next_arc[1]-1] = True
        frontier_nodes.append(next_arc[1])

    return mst_cost

#Reading the Adjacency list
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/MST.txt", "r")
data = file.readlines()

for index, line in enumerate(data):
    if index == 0:
        n_nodes, n_edges = map(int, line.split())
        G = Graph(n_nodes)
    else:
        items = line.split()
        start_node, end_node, cost = map(int, items)
        G.addEdge(start_node, (end_node, cost))
        G.addEdge(end_node, (start_node, cost))

cost = prims(G)
print(f"Cost of the Minimum Spanning Tree is {cost}")