'''This script is written to implement the single-linkage clustering method using union-find and heap
   data structures on a very big dataset. For this dataset distance is estimated using the Hamming distance method
   Nishu Choudhary
   08/11/2021
'''

#Import Required packages
import itertools
from collections import defaultdict
from itertools import combinations
from networkx.utils.union_find import UnionFind

#Reading the Adjacency list
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/clustering_big.txt", "r")
data = file.readlines()

map_bit_to_node = defaultdict(list)
n_nodes, n_bits = map(int, data[0].split())

one_bit_mask = [1 << i for i in range(n_bits)]
two_bit_combo = list(combinations(range(n_bits), 2))
two_bit_mask = [(1 << i) | (1 << j) for (i, j) in two_bit_combo]
bit_masks = one_bit_mask+two_bit_mask

for index, line in enumerate(data[1:]):
    bit = int("".join(line.split()),2) #Keeping it as a string for now
    map_bit_to_node[bit].append(index)

#Declare a Union-Find data structure for all nodes- here all nodes point toward to itself as leaders
node_list = list(range(0, n_nodes))
uf = UnionFind(elements=node_list)

#First iteration for zero Hamming distance
for key, values in map_bit_to_node.items():
    if len(values) > 1:
        for value in values[1:]:
            uf.union(values[0], value)

list_of_keys = map_bit_to_node.keys()
processed_keys = []
for key in list_of_keys:
    if key not in processed_keys:
        potential_keys = [key ^ bit for bit in bit_masks]
        common_keys = list(set(potential_keys).intersection(list_of_keys))
        processed_keys.append(common_keys)
        if common_keys:
            leader = map_bit_to_node[key][0]
            nodes_list = [map_bit_to_node[i] for i in common_keys]
            nodes = list(itertools.chain(*nodes_list))
            for node in nodes:
                uf.union(leader, node)


print(f"Number of clusters is :{len(list(uf.to_sets()))}")

