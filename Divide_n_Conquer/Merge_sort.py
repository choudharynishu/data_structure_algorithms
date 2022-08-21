'''This is the implementation of the Merge sort algorithm'''
'''Nishu Choudhary'''
'''10/28/2021'''

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

#Driver Case
arr = [14, 33, 27, 10, 35, 19, 42, 44]
merge_sort(arr)
for i in range(len(arr)):
    print(arr[i])
