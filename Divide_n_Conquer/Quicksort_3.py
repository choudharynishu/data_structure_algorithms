'''This is an implementation of the Quicksort algorithm, this script outputs the number of comparisons '''
'''In this implementation, the last element of the passed array is selected as the pivot '''
'''The Quicksort method takes O(nlogn) running time'''
'''Nishu Choudhary'''
'''11/13/2021'''

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
    if right > left:
        pivot_idx = right
        pivot_value = array[pivot_idx]
        # Move the pivot to first index
        array[left], array[right] = array[right], array[left]
        #array.insert(left, array.pop(pivot_idx))

        #Call the partition sub-routine on modified array
        count = partition(array,left,right,count)

        k = array.index(pivot_value)

        count = quicksort(array,left,k-1,count)
        count = quicksort(array,k+1,right,count)

    return count


#Driver Case
A = [10, 7, 8, 9, 1, 5]
from numpy import loadtxt
A = list(loadtxt(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/2148.txt", comments="#", delimiter="\n", unpack=False))
NCOMPARE = quicksort(A,0,len(A)-1,0)
print(A)
print(NCOMPARE)
