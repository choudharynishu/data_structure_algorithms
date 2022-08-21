'''This script is used to schedule a series of task for using a shared resource in increasing order of the difference
   between their weight and processing times. The script returns the total completion time with this scheduling algorithm
   Nishu Choudhary
   06/27/2022
'''

# Import Required Packages
import numpy as np

# Import the datafile
#Reading the Adjacency list
file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/jobs.txt", "r")
data = file.readlines()

#List to store task
task_list = []
for index, line in enumerate(data):
    # First line gives total number of jobs to be scheduled
    if index == 0:
        njobs = int(line)
    # After first line, each line gives weight and processing time of each job
    else:
        weight, time = map(int, line.split(' '))
        task_list.append((weight, time))

# Sorting the tasks according to the difference between weight and processing times
# Breaking ties with sorting higher weight first
task_order = sorted(task_list, key=lambda t: ((t[0] - t[1]), t[0]), reverse=True)

completion_time = 0
time_elapsed = 0
for task in task_order:
    time_elapsed += task[1]
    completion_time += (task[0]*time_elapsed)

print(completion_time)



