'''This script is an implementation of Kosaraju's Two Pass Algorithms to discover Strongly Connected Components (SCCs)
   for a given graph

   Nishu Choudhary
   12/23/21'''

# Python implementation of Kosaraju's algorithm to print all SCCs

import sys
import threading
from collections import defaultdict, deque


#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices = None):
        self.vertices = vertices #Initialize this but add value to this later
        self.graph = defaultdict(list)  #default dictionary to store graph

    #Function to define an edge using u,v where the edge is point from u to v
    def addEdge(self,u,v):
            self.graph[u].append(v)

    #Function to reverse the graph representation
    def Reverse(self):
        rev_graph = Graph(self.vertices)

        for key, value_list in self.graph.items():
            for value in value_list:
                rev_graph.addEdge(value,key)

        return rev_graph

    #DFS recursive subroutine
    def DFS(self, key, visited, stack):
        visited[key-1] = True
        #Accessing a key that doesn't exists in Defaultdict would prompt exception clause which will automatically add
        # the missing key
        if key in self.graph:
            neighbors = self.graph[key]
            for neighbor in neighbors:
                if not visited[neighbor - 1]:
                    self.DFS(neighbor, visited, stack)

        stack.append(key)
        return None

    #Function to assign leader to every node
    def assign(self,leader,key,visited):
        visited[key-1] = True

        #Add (Leader,key) relationship to the leadership dictionary
        self.leadership[leader].append(key)

        neighbors = self.graph[key]
        for neighbor in neighbors:
            if not visited[neighbor-1]:
                self.assign(leader,neighbor,visited)

        return None

    #Function to detect Strongly Connected Components (SCCs) in a graph
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

        scc_len = [len(value_list) for key, value_list in self.leadership.items()]
        scc_len.sort()
        print(scc_len[-5:])

def main():
    # Create a graph given in the above diagram
    file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/SCC.txt", "r")
    data = file.readlines()

    g = Graph(875714)

    for line in data:
        items = line.split()
        g.addEdge(int(items[0]), int(items[1]))

    g.Kosaraju()

if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=main)
    thread.start()

