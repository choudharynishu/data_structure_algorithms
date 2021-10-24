'''This script is used to implement Insertion sort'''
'''Nishu Choudhary'''
'''10/23/2021'''

#Function
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        #Start with previous value of i
        j = i-1
        #We need to shift the position og arr[j] if it is greater than key
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        #After swapping we have the last swap value in two positions, replace it with key
        arr[j+1] = key
    return arr
#Driver Case
arr = [14, 33, 27, 10, 35, 19, 42, 44]
sorted_arr = insertion_sort(arr)
for i in range(len(sorted_arr)):
    print(arr[i])
