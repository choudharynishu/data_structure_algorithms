'''This script is used to implement Maximum Weight Independent set estimation using Dynamic Programming
   Nishu Choudhary
   08/16/2022
'''

#Import Required Packages

#Read input file
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/mwis.txt", "r")
data = file.readlines()

num_vertices = int(data[0]) #Number of vertices
weights = [int(item) for item in data[1:]]
#Insert weight for zeroth node (which is not present)
weights.insert(0, 0)

#Matrix used to determine mwis solution for each subproblem
A = [0] * (num_vertices+1)
#Initialization
A[1] = weights[1]

for i in range(2, num_vertices+1):
    A[i] = max(A[i-1], A[i-2]+weights[i])
index = num_vertices
present_nodes = [0]*(num_vertices+1)


while index>=1:
    if A[index-1] >= A[index-2] +weights[index]:
        present_nodes[index] = 0
        index = index-1
    else:
        present_nodes[index] = 1
        present_nodes[index-1] = 0
        index = index-2
index_list = [1,2,3,4,17,117,517,997]
res_list = list(map(present_nodes.__getitem__, index_list))
print(res_list)
