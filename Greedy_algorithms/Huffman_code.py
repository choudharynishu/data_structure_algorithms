'''This script is written to implement Huffman coding algorithm
   Nishu Choudhary
   08/15/2021
'''

#Import Required packages
import heapq

class node:
    def __init__(self, frequency, name=None, left=None, right=None):
        #Left child of the node
        self.left = left
        #Right child of the node
        self.right = right
        #Frequency of the node
        self.frequency = frequency
        self.name = f"{name}"
        self.huff = ''
        self.parent = None

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return f"({self.name},{self.frequency})"

    def __str__(self):
        return f"({self.name},{self.frequency})"

def huffcode(node):
    if node.parent is None:
        return ''
    else:
        return f"{huffcode(node.parent)}{node.huff}"

#Reading the number of characters and their respective weights
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/huffman_coding.txt", "r")
data = file.readlines()

num_characters = int(data[0])
nodes = []
for index, line in enumerate(data[1:]):
    nodes.append(node(int(line), index+1))

nodes_dup = nodes[:]
heapq.heapify(nodes)

#Run the while loop till there are no nodes left in the heap
while len(nodes) > 1:
    left_node = heapq.heappop(nodes)
    right_node = heapq.heappop(nodes)
    left_node.huff = 0
    right_node.huff = 1
    new_node = node(left_node.frequency+right_node.frequency, name=f"{left_node.name}+{right_node.name}", left=left_node, right=right_node)
    left_node.parent = new_node
    right_node.parent = new_node
    heapq.heappush(nodes, new_node)


lengths = list(map(lambda x:  len(huffcode(x)), nodes_dup))

print(f"Maximum length is {max(lengths)}")
print(f"Minimum length is {min(lengths)}")


