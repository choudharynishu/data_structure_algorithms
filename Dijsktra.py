'''This script is an implementation of Dijkstra's Algorithm to find the shortest path between the source
   and the destination node for the given adjacency list

   Nishu Choudhary
   01/07/22'''

#Required Package
from collections import defaultdict

def dijsktra_score(visited,score):
    min_score = 1000000
    for node in visited:
        outgoing_arcs = list(filter(lambda point: point not in visited, list(graph[node].keys())))
        if not len(outgoing_arcs) == 0:
            distances = [graph[node][arc] for arc in outgoing_arcs]
            for arc, dist in zip(outgoing_arcs,distances):
                score[arc] = min(score[arc], score[node]+dist)

            checking_scores = min([score[arc] for arc in outgoing_arcs])
            if checking_scores <= min_score:
                min_score = checking_scores
                for key, value in graph[node].items():
                    if score[key] == min_score and key not in list(visited):
                        added_node = key

    visited.add(added_node)
    return None

#Dijkstra's algorithm
def dijsktra(graph):
    keys = list(graph.keys())
    score = {key: (1000000 if not key == 1 else 0) for key in keys}

    #Set that would contain values of all visited  nodes
    visited = set()
    visited.add(1)
    while not keys == list(visited):
        dijsktra_score(visited,score)
    #print(score)
    nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for x in nodes:
        print(score[x])
    return None


#Reading the Adjacency list
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/dijkstra.txt", "r")
data = file.readlines()
graph = defaultdict(list)

#Next Optimize this
for line in data:
    items = line.split()
    key = int(items[0])
    values = items[1:]
    node_dist_dict = dict()
    for value in values:
        elements = list(map(int, value.split(',')))
        node_dist_dict[elements[0]] = elements[1]
    graph[key] = node_dist_dict

dijsktra(graph)




