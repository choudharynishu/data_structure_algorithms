'''
This script is a heap based implementation of the median maintenenance problem

Nishu Choudhary

'''

# Import Required Packages
import os
import numpy as np


class heap:
    def __init__(self):
        self.size = 1
        self.heap = [None] * self.size

    # Methods for getting Child or Parent index
    @staticmethod
    def getrightchildindex(index):
        return 2*index+1
    @staticmethod
    def getleftchildindex(index):
        return 2*index
    @staticmethod
    def getparentindex(index):
        return index // 2

    #Method for getting the value for Child and Parent index
    def getrightchildvalue(self, index):
        return self.heap[self.getrightchildindex(index)]
    def getleftchildvalue(self, index):
        return self.heap[self.getleftchildindex(index)]
    def getparentvalue(self,index):
        return self.heap[self.getparentindex(index)]

    def hasrightchild(self, index):
        return self.getRightchild_index(index) < self.size
    def hasleftchild(self, index):
        return self.getLeftchild_index(index) < self.size
    def hasparent(self, index):
        return self.getParent_index(index) >= 0

    def swap(self, index_one, index_two):
        temp = self.heap[index_one]
        self.heap[index_one] = self.heap[index_two]
        self.heap[index_two] = temp
        return None


class min_heap(heap):
    def __init__(self):
        super.__init__(self)

    def bubble_down(self):
        index = 0
        while(self.hasleftchild(index)):
            smallerchildindex = self.getleftchildindex(index)
            if ((self.hasrightchild(index))&(self.getrightchildvalue(index) < self.heap[smallerchildindex])):
                smallerchildindex  = self.getrightchildindex(index)
            if self.heap[index] > self.heap[smallerchildindex]:
                self.swap(index, smallerchildindex)
                index = smallerchildindex
        return None

    def bubble_up(self):
        index = self.size -1
        while(self.hasparent(index) & (self.getparentvalue(index) > self.heap[index])):
            self.swap(index, self.getparentindex(index))
            index = self.getparentindex(index)
        return None

    def extract_min(self):
        assert self.heap[0] != None
        minimum_value = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.bubble_down()
        return minimum_value

    def insert(self, value):
        self.heap.append(value)
        self.size = + 1
        self.bubble_up()
