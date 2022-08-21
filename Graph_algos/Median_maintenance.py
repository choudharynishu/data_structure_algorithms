'''This script is a heap based implementation of the median maintenenance problem

   Nishu Choudhary
'''

#Import Required Packages
import os
import numpy as np

class heap(object):
    def __init__(self, value):
        self.heap = np.array([value])
        self.shape = 1

    def hasRightchild(self, index):
        return self.getRightchild_index(index) < self.shape
    def hasLeftchild(self, index):
        return self.getLeftchild_index(index) < self.shape
    def hasParent(self, index):
        return self.getParent_index(index) >= 0

    def getRightchild_index(self, index):
        return 2*index+2
    def getLeftchild_index(self, index):
        return 2 * index + 1
    def getParent_index(self, index):
        if index % 2 == 0:
            parent_idx = int(index / 2 - 1)
        else:
            parent_idx = int(np.floor(index / 2))
        return parent_idx

    def getRightchild_value(self, index):
        return self.heap[self.getRightchild_index(index)]
    def getLeftchild_value(self, index):
        return self.heap[self.getLeftchild_index(index)]
    def getParent_value(self, index):
        return self.heap[self.getParent_index(index)]

    def insert(self, value):
        last_position = self.shape
        self.heap = np.append(self.heap, value)  #should be more efficient
        self.shape = self.shape + 1
        self.bubble_up(last_position)
        return None

    def swap(self, index_one, index_two):
        #Here index one has smaller value and index two has bigger value
        temp = self.heap[index_one]
        self.heap[index_one] = self.heap[index_two]
        self.heap[index_two] = temp
        return None

class min_heap(heap):
    def __init__(self, value):
        super().__init__(value)

    def getmin(self):
        return self.heap[0]

    def extract_min(self):
        min_value = self.getmin()
        self.shape = self.shape - 1
        #Add last value to the root
        self.heap[0] = self.heap[self.shape]
        #Replace last value with a np.nan-there might be problem downstream?
        self.heap = self.heap[:-1]

        #Bubble down the root value to its appropriate place
        self.bubble_down(0)
        return min_value

    def bubble_up(self, index_val):
        while(self.hasParent(index_val) and (self.getParent_value(index_val)>self.heap[index_val])):
            self.swap(self.getParent_index(index_val),index_val)
            index_val = self.getParent_index(index_val)
        return None

    def bubble_down(self,index_val):
        while(self.hasLeftchild(index_val)):
            smallerchild_index = self.getLeftchild_index(index_val)
            if self.hasRightchild(index_val):
                if self.heap[smallerchild_index] > self.getRightchild_value(index_val):
                    smallerchild_index = self.getRightchild_index(index_val)

            if (self.heap[smallerchild_index] < self.heap[index_val]):
                self.swap(smallerchild_index, index_val)
                index_val = smallerchild_index
            else:
                break

        return None

class max_heap(heap):
    def __init__(self, value):
        super().__init__(value)

    def getmax(self):
        return self.heap[0]

    def extract_max(self):
        max_value = self.getmax()
        self.shape = self.shape - 1
        #Add last value to the root
        self.heap[0] = self.heap[self.shape]
        #Replace last value with a np.nan-there might be problem downstream?
        self.heap = self.heap[:-1]
        #Bubble down the root value to its appropriate place
        self.bubble_down(0)
        return max_value

    def bubble_up(self, index_val):
        while(self.hasParent(index_val) and (self.getParent_value(index_val)<self.heap[index_val])):
            self.swap(self.getParent_index(index_val), index_val)
            index_val = self.getParent_index(index_val)
        return None

    def bubble_down(self,index_val):

        while(self.hasLeftchild(index_val)):
            biggerchild_index = self.getLeftchild_index(index_val)

            if self.hasRightchild(index_val):
                if (self.heap[biggerchild_index] <= self.getRightchild_value(index_val)):
                    biggerchild_index = self.getRightchild_index(index_val)

            if (self.heap[biggerchild_index] > self.heap[index_val]):
                self.swap(biggerchild_index, index_val)
                index_val = biggerchild_index
            else:
                break

        return None

def digitize(x):
    x = x.split('\n')[0]
    return float(x)

#file = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/median.txt", "r")

f = open(f"/Users/nishuchoudhary/Desktop/Academic/Fall 2021/DSA/median.txt", "r")
lines = f.readlines()
numbers = list(map(digitize, lines))

#Initialize High & Low heap
#High heap- represents a minimum heap of upper half of the passed numbers
#Low heap- represents a maximum heap of upper half of the passed numbers

high_heap = min_heap(numbers.pop(0))
low_heap = max_heap(numbers.pop(0))

median = np.empty(10000, dtype=float)
median[0] = high_heap.getmin()
median[1] = min(high_heap.getmin(), low_heap.getmax())

count = 2

for number in numbers:

    if number > high_heap.getmin():
        high_heap.insert(number)
    else:
        low_heap.insert(number)

    #Check size of each resulting heaps
    if np.abs(high_heap.shape-low_heap.shape)>=2:
        if low_heap.shape >= high_heap.shape+1:
            temp_value = low_heap.extract_max()
            high_heap.insert(temp_value)
        else:
            temp_value = high_heap.extract_min()
            low_heap.insert(temp_value)
        del temp_value


    if (low_heap.shape+high_heap.shape)%2 ==0:
        median[count] = min(high_heap.getmin(), low_heap.getmax())
    else:
        if low_heap.shape > high_heap.shape:
            median[count] = low_heap.getmax()
        else:
            median[count] = high_heap.getmin()
    count+=1

np.set_printoptions(suppress=True)
print(np.sum(median)%10000)
