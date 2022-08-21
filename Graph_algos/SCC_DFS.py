'''This script is an implementation of Kosaraju's Two Pass Algorithms to discover Strongly Connected Components (SCCs)
   for a given graph

   Nishu Choudhary
'''

# Python implementation of Kosaraju's algorithm to print all SCCs

import sys
import threading
from collections import defaultdict, deque

#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices=None):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self,startNode, endNode):
        self.graph[startNode].append(endNode)

    def reverse(self):
        rev_g = Graph(self.vertices)
        for key, values in self.graph.items():
            for value in values:
                rev_g.graph[value].append(key)
        return rev_g
    def DFS(self,key):
        explore[key-1] = True
        next_nodes = self.graph[key]

        # Check if the next_keys list is empty
        if key in self.graph:
            for node in next_nodes:
                if not explore[node-1]:
                    self.DFS(node)
        # Add the key node in order of finishing time- recursive call would return once the for loop is complete
        finishing_time.append(key)
        return None

        # Function to assign leader to every node
    def assign(self, leader, key, explore):
        explore[key - 1] = True

        # Add (Leader,key) relationship to the leadership dictionary
        self.scc[leader].append(key)

        neighbors = self.graph[key]

        for neighbor in neighbors:
            if not explore[neighbor - 1]:
                self.assign(leader, neighbor, explore)

        return None

    def Kosaraju(self):
        # Explore status of a node
        global explore
        explore = [False] * self.vertices

        # First round of Kosaraju to compute the order of nodes to be processed
        reverse_g = self.reverse()

        # Doubly ended queue to save nodes in the order of there finishing times
        global finishing_time
        finishing_time = deque()

        for node in reversed(range(1, self.vertices + 1)):
            if not explore[node - 1]:
                reverse_g.DFS(node)

        # Second pass at the algorithm
        self.scc = defaultdict(list)
        # Reset the explore status of all nodes
        explore = [False] * self.vertices

        while finishing_time:
            node = finishing_time.pop()
            if not explore[node - 1]:

                leader = key = node
                self.assign(leader, key, explore)

        scc_len = [len(value_list) for key, value_list in self.scc.items()]
        scc_len.sort()
        print(scc_len[-5:])
        return None


#Main loop for inputing data
def main():    # Using readlines() to read the input file
    file = open('/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/SCC.txt', 'r')
    lines = file.readlines()

    #Create an instance of the Graph class
    g = Graph(875714)

    for line in lines:
        start, end = map(int, line.split())
        g.addEdge(start, end)
    g.Kosaraju()
    return None


if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()