
import math
from platform import node

class MinHeap:
    def __init__(self):
        self._root = None
        self._nodes = []
        self._count = 0


    def __iter__(self):
        return self._iter_helper(0)

    def _iter_helper(self, index):
        if index < self._count:
            yield self._nodes[index]
            yield from self._iter_helper(self._get_left_child_index(index))
            yield from self._iter_helper(self._get_right_child_index(index))

    def _swap(self, firstIndex, secondIndex):
        if self._count <= 0:
            raise ValueError("The heap is Empty...")
        self._nodes[firstIndex], self._nodes[secondIndex] = self._nodes[secondIndex], self._nodes[firstIndex]


    def _get_left_child_index(self, index):
        return (index * 2) + 1

    
    def _get_right_child_index(self, index):
        return (index * 2) + 2


    def _get_parent_index(self, index):
        return max(math.floor((index - 2) / 2), 0)

    def _heapify_up(self):
        if self._count <= 1:
            return
        
        index = self._count -1
        parentIndex = self._get_parent_index(index)
        while self._nodes[index] < self._nodes[parentIndex]:
            self._swap(index, parentIndex)
            index = parentIndex
            parentIndex = self._get_parent_index(index)


    def _heapify_down(self):
        index = 0
        smallerChildIndex = self._get_smaller_child_index(index)
        while self._nodes[smallerChildIndex] < self._nodes[index]: 
            self._swap(index, smallerChildIndex)
            index = smallerChildIndex
            smallerChildIndex = self._get_smaller_child_index(index)


    def _get_smaller_child_index(self, index):
        leftChildIndex = self._get_left_child_index(index)
        if leftChildIndex >= self._count:
            leftChildIndex = index
        rightChildIndex = self._get_right_child_index(index)
        if rightChildIndex >= self._count:
            rightChildIndex = index
        smallerChildIndex = leftChildIndex if self._nodes[leftChildIndex] < self._nodes[rightChildIndex] else rightChildIndex
        return smallerChildIndex

    def add(self, data):
        self._nodes.append(data)

        self._count += 1

        if self._count > 1:
            self._heapify_up()


    def peek(self):
        if self._count <= 0:
            return
        return self._nodes[0]

    
    def poll(self):
        if self._count <= 0:
            return            

        node = self._nodes[0]
        self._swap(0, self._count - 1)
        self._count -= 1
        if self._count > 1:
            self._heapify_down()
        
        return node
