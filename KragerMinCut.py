'''This script is an implementation of the Krager's Randomized Minimum Cut Problem'''
'''Nishu Choudhary'''
'''12/02/2021'''

import fileinput
import random


def find(parents, i):
    # This function helps to find a node with degree less than equal to 2
    r = i

    # This will give us the last (farthest) node in the connected graph regardless of whether i and r are connected or not
    while r in parents:
        r = parents[r]

    # This will give us the last (farthest) node in the connected graph regardless of whether i and r are connected or not
    while i in parents:
        p = parents[i]
        parents[i] = r
        i = p
    return i


def unite(parents, i, j):
    parents[i] = j


def karger(num_vertices, edges):
    # Convert the Edge set to a list of tuples
    edges = list(edges)

    # Shuffle the list in-place
    random.shuffle(edges)

    # Initialize a dictionary, to use key as smaller node of the edge and value as bigger node of the edge
    parents = {}

    # Iterate through the list and unpack each tuple into vertex_i and vertex_j
    for i, j in edges:

        # Iterate only till there are two vertices left in the fused graph - single edge
        if num_vertices <= 2:
            break
        # Check if either of the two nodes exists in the new parent dictionary
        # If only one node exists and the other doesn't we can add that (i,j) pair as key, value pair
        # If both nodes exists, implying the edge already exists, then
        #    to avoid creation of self-loop we would skip the unite and reducing number of vertices call
        # If none of the nodes exists then we can safely add that as a new edge
        i = find(parents, i)
        j = find(parents, j)

        if i == j:
            # To prevent creating a self loop
            continue
        unite(parents, i, j)
        # Everytime two vertices are fused together or are added to the parents dictionary num_vertices is reduced by one
        num_vertices -= 1

    return sum(find(parents, i) != find(parents, j) for (i, j) in edges)


def main():
    # Here each row represents adjacency values for a particular vertex
    rows = list(fileinput.input(files=(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/Krager_minncut.txt")))

    # total number of vertices-first element of each row is unique and stands for a particular edge
    n_vertices = len(rows)

    # To uniformly select an edge we first have to find a list of all edges
    # To make sure we don't have duplicate edges, this variable is defined as a set
    edges = set()

    # Iterate through the adjacency list, row-by-row and create a Edge set out of it
    for row in rows:
        # Split each row on whitespaces, convert the string values into int and then create an iterator out of it
        row_int = iter(map(int, row.split()))

        # Get the first item from the iterator on field-this item would be the first vertex in an edge
        vertex_i = next(row_int)

        # Use update method to add new edges to the set
        # Set are unordered because it uses a hashtable to avoid double entries of the same value
        edges.update((min(vertex_i, vertex_j), max(vertex_i, vertex_j)) for vertex_j in row_int)

    # Call the krager function- 1000 times as the algorithm doesn't always give the minimum cut of a graph
    print(min(karger(n_vertices, edges) for k in range(1000)))


if __name__ == "__main__":
    main()