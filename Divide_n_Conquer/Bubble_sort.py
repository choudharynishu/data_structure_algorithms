'''This script is used to implement Bubble sort
   Nishu Choudhary'''

#Function
def bubble_sort(arr):
    swap = True
    while(swap):
        swap = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap = True
    return arr

#Input
#Driver case
arr = [64,34,25,25,22,90,11]
sorted_arr = bubble_sort(arr)

for i in sorted_arr:
    print(i)