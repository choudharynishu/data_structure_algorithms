'''
   Implementation of the Kosaraju's Strongly Connected Connected Components to solve the 2-SAT problem
   Running Time: O(E+V)
'''

#Import Required Package
import os
import sys
import threading
import numpy as np
from collections import defaultdict, deque

class Graph():
    def __init__(self, vertices=None):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
            if v not in self.graph[u]:
                self.graph[u].append(v)

            # Function to reverse the graph representation

    def Reverse(self):
        rev_graph = Graph(self.vertices)

        for key, value_list in self.graph.items():
            for value in value_list:
                rev_graph.addEdge(value, key)

        return rev_graph

        # DFS recursive subroutine

    def DFS(self, key, visited, stack):
        visited[key - 1] = True
        # Accessing a key that doesn't exists in Defaultdict would prompt exception clause which will automatically add
        # the missing key
        if key in self.graph:
            neighbors = self.graph[key]
            for neighbor in neighbors:
                if not visited[neighbor - 1]:
                    self.DFS(neighbor, visited, stack)

        stack.append(key)
        return None

        # Function to assign leader to every node

    def assign(self, leader, key, visited):
        visited[key - 1] = True

        # Add (Leader,key) relationship to the leadership dictionary
        self.leadership[leader].append(key)

        neighbors = self.graph[key]
        for neighbor in neighbors:
            if not visited[neighbor - 1]:
                self.assign(leader, neighbor, visited)

        return None

    def Kosaraju(self):
        #Implementing First-half of Kosaraju's

        #Reverse the graph
        rev_g = self.Reverse()

        # To store the values of vertices in increasing order of their finishing times
        stack = deque()

        # List to store whether or not a vertex has been visited or not
        # Copied False value to the list for each vertex
        visited = [False]*rev_g.vertices

        for key, value_list in rev_g.graph.items():

            if not visited[key-1]:
                rev_g.DFS(key, visited, stack)

        #Dictionary to store leaders and their nodes
        self.leadership = defaultdict(list)

        #Reset the visited list for the original graph
        visited = [False] * self.vertices

        while stack:
            leader = stack.pop()
            key = leader
            if not visited[leader-1]:
                self.assign(leader, key, visited)
        scc_components = self.leadership
        return scc_components

def literal_to_index(x, n_variables):
    '''
    :param x: The value of boolean literal to be converted into a numerical vertex.
              For example, boolean literal is A then vertex value is A
              while if if boolean is A then vertex value is A+total number of variables
    :return: vertex value to be added to the graph
    '''
    x = int(x)
    if x < 0:
        return n_variables + abs(x)
    else:
        return x

def negate(x, nvar):
    '''

    :param x: Boolean literal for which the vertex value of the complement is to be computed
    :param nvar: Total number of variables in the given 2SAT problem
    :return: Vertex value of the complement of the given boolean literal
    '''
    if x > nvar:
        return x-nvar
    else:
        return x+nvar


def main():
    # Create a graph given in the above diagram
    # Imput file
    file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/2SAT4.txt", "r")
    data = file.readlines()
    # Extract number of total variables
    n_variables = int(data[0])
    verification_pairs = [(x, x+n_variables) for x in range(1, n_variables+1)]

    # Create two vertices for each variable
    implication_graph = Graph(2 * n_variables)

    # Create Implication graph for each node
    for index, item in enumerate(data[1:]):
        a, b = tuple(map(lambda x: literal_to_index(x,n_variables), item.split()))
        implication_graph.addEdge(negate(a, n_variables), b)
        implication_graph.addEdge(negate(b, n_variables), a)

    scc_components = implication_graph.Kosaraju()
    statements = [any(x in checklist and y in checklist for (x, y) in verification_pairs) for checklist in
                  scc_components.values()]
    print(f" Is 2SAT satisfiable: {not any(statements)}")
    
if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()
