'''This script is written to implement the single-linkage clustering method using union-find and heap
   data structures.
   Nishu Choudhary
   07/11/2021
'''

#Import Required packages
import heapq
from networkx.utils.union_find import UnionFind

#Reading the Adjacency list
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/clustering.txt", "r")
data = file.readlines()
cost_start_end = []
def check_membership(element, list_of_clusters):
    for i, list in enumerate(list_of_clusters):
        if element in list:
            index = i
    return index

for index, line in enumerate(data):
    if index == 0:
        n_nodes = int(line)
    else:
        items = line.split()
        start_node, end_node, cost = map(int, items)
        cost_start_end.append((cost, start_node, end_node))

#Declare a Union-Find data structure for all nodes
node_list = list(range(1, n_nodes+1))
uf = UnionFind(elements=node_list)

#Convert the cost,start-node, and end-node tuple-list to a heap data structure
#Returns an in-place heapfied list
heapq.heapify(cost_start_end)

def clustering(cost_start_end, uf, n_nodes, nclusters=2):
    nleaders = len([x for x in uf.parents.keys() if uf.parents[x]==x])
    while nleaders > nclusters:
        #print(cost_start_end)
        _, min_cost_start, min_cost_end = heapq.heappop(cost_start_end)
        uf.union(min_cost_start, min_cost_end)
        nleaders = len([x for x in uf.parents.keys() if uf.parents[x] == x])

    print(f"Leaders are: {[x for x in uf.parents.keys() if uf.parents[x] == x]}")
    list_of_clusters = [[]] *nclusters
    cluster_membership_list = list(uf.to_sets())

    for i in range(nclusters):
        list_of_clusters[i] = list(cluster_membership_list[i])

    while cost_start_end:
        spacing, start, end = heapq.heappop(cost_start_end)
        if not check_membership(start, list_of_clusters) == check_membership(end, list_of_clusters) :
            break

    return spacing
    #return None
#clustering(cost_start_end, uf, n_nodes, 2)
spacing = clustering(cost_start_end, uf, n_nodes, 4)
print(f"Spacing is {spacing}")



