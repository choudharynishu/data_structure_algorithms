'''This script can be used to count the number of array inversions'''
'''The total number of inversions are counted through three different types of recursive calls
   1. Left inversions, where indices to be swapped both are present in the left half of an array
   2. Right inversions, where indices to be swapped both are present in the right half of an array
   3. Split inversions, where indices to be swapped one of them is in the left half and the other is in right half
'''
'''Nishu Choudhary'''
'''10/28/2021'''

def merge_sort(array,sorted_array,start,mid,end):
    if len(array) > 1:
        #Initializing the starting indices of left and right
        left_start = start
        right_start = mid+1
        sorted_start = start
        split_inversions = 0

        while(left_start<=mid and right_start<=end):
            if array[left_start] <= array[right_start]:
                    # Modifying array in-place
                    sorted_array[sorted_start] = array[left_start]
                    left_start += 1
            else:
                sorted_array[sorted_start] = array[right_start]
                split_inversions += (mid-left_start+1)
                right_start += 1
            sorted_start += 1

        while left_start <= mid:
           sorted_array[sorted_start] = array[left_start]
           left_start += 1
           sorted_start += 1

        while right_start <= end:
            sorted_array[right_start] = array[right_start]
            right_start += 1
            sorted_start += 1
        for idx in range(start, end + 1):
            array[idx] = sorted_array[idx]
    return split_inversions

def array_inversions(arr,sorted_arr,start,stop):
    inversions = 0
    if start < stop:

        mid_index = (start+stop) // 2
        inversions += array_inversions(arr,sorted_arr,start,mid_index)
        inversions += array_inversions(arr,sorted_arr,mid_index+1,stop)
        inversions += merge_sort(arr,sorted_arr,start,mid_index,stop)


    return inversions

def count_inversions(arr,n):
    sorted_arr = [0] *n
    return array_inversions(arr,sorted_arr,0,n-1)
#Driver Case
arr = [8, 4, 2, 1]
n = len(arr)
result = count_inversions(arr,n)
print("Number of inversions are", result)
#Expected Output = 6

