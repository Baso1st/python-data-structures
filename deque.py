import re
from doublyLinkedList import DoublyLinkedList

class Deque:
    def __init__(self):
        self._dList = DoublyLinkedList()

    def enqueue_head(self, data):
        self._dList.add_head(data)

    def enqueue_tail(self, data):
        self._dList.add_tail(data)

    def dequeue_head(self):
        head = self._dList.get_head()
        if head is not None:
            self._dList.remove_head()
        return head

    def dequeue_tail(self):
        tail = self._dList.get_tail()
        if tail is not None:
            self._dList.remove_tail()
        return tail

    def peak_head(self):
        return self._dList.get_head()

    def peak_tail(self):
        return self._dList.get_tail()

    def __iter__(self):
        return self._dList.__iter__()

