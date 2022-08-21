'''This script is a heap based implementation of the median maintenenance problem

   Nishu Choudhary
   '''

#Import Required Packages
import os
import numpy as np

class min_heap(object):
    def __init__(self, value):
        self.heap = np.array([value])
        self.shape = 1

    def hasRightchild(self, index):
        return self.getRightchild_index(index) <= self.shape
    def hasLeftchild(self, index):
        return self.getLeftchild_index(index) <= self.shape
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

    def getmin(self):
        return self.heap[0]

    def extract_min(self):
        min_value = self.getmin()
        self.shape = self.shape - 1
        #Add last value to the root
        self.heap[0] = self.heap[self.shape]
        print(f"shape is {self.shape}")
        print(self.heap[self.shape])
        #Replace last value with a np.nan-there might be problem downstream?
        self.heap[self.shape] = np.nan

        #Bubble down the root value to its appropriate place
        self.bubble_down(0)
        return min_value

    def swap(self, index_one, index_two):
        #Here index one has smaller value and index two has bigger value
        temp = self.heap[index_one]
        self.heap[index_one] = self.heap[index_two]
        self.heap[index_two] = temp
        return None

    def bubble_up(self, index_val):
        while(self.hasParent(index_val) and (self.getParent_value(index_val)>self.heap[index_val])):
            self.swap(self.getParent_index(index_val),index_val)
            index_val = self.getParent_index(index_val)
        return None

    def bubble_down(self,index_val):
        while(self.hasLeftchild(index_val)):
            smallerchild_index = self.getLeftchild_index(index_val)
            if self.heap[smallerchild_index] > self.getRightchild_value(index_val):
                smallerchild_index = self.getRightchild_index(index_val)

            if (self.heap[smallerchild_index] < self.heap[index_val]):
                self.swap(smallerchild_index, index_val)
                index_val = smallerchild_index
            else:
                break

        return None



numbers = [13.0, 16.0, 31.0, 62.0, 100.0, 102.0]
heap_low = min_heap(51.0)

for number in numbers:
    heap_low.insert(number)
    print(heap_low.heap)

minimum_value = heap_low.extract_min()
print(minimum_value)
print(heap_low.heap)



