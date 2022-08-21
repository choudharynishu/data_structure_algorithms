'''This script is written to compute shortest path using Dijsktra's algorithm
   using a heap based implementation
   Nishu Choudhary
'''

#Import Required Packages
from collections import defaultdict

def dijsktra_score(x):
    return min_distance[x[0]-1]+graph[x[0]].get(x[1])

#Dijsktra Algorithm implementation
def dijsktra(graph):

    #Initializing minimum distance, denoting Dijsktra'a Algorithm score,
    # and track of nodes that have been assigned a score
    global min_distance
    min_distance = [1000000]*len(graph)
    score_assigned = [False] * len(graph)

    #Assigning Dijsktra's score of first node as zero and changing its scoring status
    min_distance[0] = 0
    score_assigned[0] = True
    #To keep track of nodes responsible for outgoing arcs
    frontier_nodes = [1]

    while not all(score_assigned):
        potential_outgoing_arcs = [(node, end) for node in frontier_nodes for end in graph[node].keys() if not score_assigned[end-1]]
        #Select the next arc based on the end node of the outgoing arc that minimize the Dijsktra's score
        next_arc = min(potential_outgoing_arcs, key=dijsktra_score)

        #Edit the distance list for nodes, frontier node list, and status of score_assigned
        min_distance[next_arc[1]-1] = dijsktra_score(next_arc)
        score_assigned[next_arc[1]-1] = True
        frontier_nodes.append(next_arc[1])

    result = []
    check_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for nodes in check_nodes:
        result.append(min_distance[nodes-1])
    print(result)

    return None

#Reading the Adjacency list
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/dijkstra.txt", "r")
data = file.readlines()
graph = defaultdict(list)
counter = 0

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
