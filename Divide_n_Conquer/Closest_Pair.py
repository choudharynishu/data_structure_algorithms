'''This is the implementation to find the closest pair of points from a given set of points'''

#To calculate Euclidean distance
import math
import numpy as np

#Class to represent a 2-D point
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

#Implementation of merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid_index = len(arr)//2
        left = arr[:mid_index]
        right = arr[mid_index:]

        merge_sort(left)
        merge_sort(right)

        #Initializing the starting indices of left and right
        i = j = 0

        for k in range(len(left)+len(right)):
            if i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # Modifying array in-place
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
            elif i == len(left):
                arr[k] = right[j]
                j += 1
            elif j == len(right):
                arr[k] = left[i]
                i += 1

#Modification of merge sort
def merge_sort_adv(key,value):
    P_key = dict(zip(key, value))
    merge_sort(key)
    P_key_sorted = {k: P_key.get(k) for k in key}
    P_key_sorted_list = list(P_key_sorted.items())
    return P_key_sorted_list

#Method to calculate closest pair of points from the given list of points

def closest(P,n):
    #Call Mergrsort to sort given list according to Point.x and Point.y
    P_x = merge_sort_adv(key=[point.x for point in P],value = [point.y for point in P])
    P_y = merge_sort_adv(key=[point.y for point in P], value=[point.x for point in P])
    print(P_x)
    print(P_y)
    #Need to create a global counter of closest pair discovered so far
    #if n==1:
    #return P
    #delta = np.inf
    #m  = n//2    #mid-index
    #Q = closest(P[0:m],m,delta)
    #R = closest(P[m+1:n], n-m,delta))
    return None

#Driver Case
P = [Point(2, 3), Point(12, 30),
     Point(40, 50), Point(5, 1),
     Point(12, 10), Point(3, 4)]
n = len(P)
closest(P,n)
#print(f"The closest Pair of points are {pair} and the smallest distance is {distance}")
#m = n//2
#[print(point.x, point.y) for  point in P[0:m]]