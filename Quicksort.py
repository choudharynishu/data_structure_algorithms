'''This is an implementation of the Quicksort algorithm, this script outputs the number of comparisons '''
'''In this implementation, the selection of pivot is randomized'''
'''The Quicksort method takes O(nlogn) running time'''
'''Nishu Choudhary'''
'''11/13/2021'''
#Import random package for pivot selection
from random import randrange
#Implementation of the partition sub routine
def partition(A,l,r,count):

    pivot = A[l]
    i = l+1
    for j in range(l+1,r+1):
        count += 1
        if A[j] < pivot:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
    A[l] = A[i-1]
    A[i-1] = pivot
    return count

def quicksort(array,left,right,count):

    #Select a pivot- randomized selection of pivot gives best performance
    #Total available choices for pivot selection = (right-left) index
    if right > left+1:
        #Randomly selected pivot index
        pivot_idx = randrange(left,right)

        #Move the pivot to first index
        pivot_value = array[pivot_idx]
        array.insert(left,array.pop(pivot_idx))

        #Call the partition sub-routine on modified array
        count = partition(array,left,right,count)

        k = array.index(pivot_value)

        count = quicksort(array,left,k-1,count)
        count = quicksort(array,k+1,right,count)

    return count


#Driver Case
A = [10, 7, 8, 9, 1, 5]
NCOMPARE = quicksort(A,0,len(A)-1,0)
print(NCOMPARE)
