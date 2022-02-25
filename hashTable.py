
from doublyLinkedList import DoublyLinkedList

class HashNode:
    def __init__(self, key, value):
       self.key = key
       self.value = value


class HashTable:
    def __init__(self):
        self._values = [DoublyLinkedList() for x in range(5)]
        self._fill_factor = 0.75
        self._count = 0
        pass


    def __iter__(self):
        for linkedList in self._values:
            for hashNode in linkedList:
                yield hashNode

    
    def __getitem__(self, key):
        index = self._get_index(key)
        linkedList = self._values[index]

        for hashNode in linkedList:
            if hashNode.key == key:
                return hashNode.value

    
    def __setitem__(self, key, value):
        self.add(key, value)


    def _get_index(self, key):
        return (hash(key) % len(self._values))
    
    
    def add(self, key, value):

        if self.contains(key):
            self.remove(key)

        if self._count >= (len(self._values) * self._fill_factor):
            self._extend()

        index = self._get_index(key)
        self._values[index].add_tail(HashNode(key, value))

        self._count += 1

    
    def _extend(self):
        oldArray = self._values
        self._values = [DoublyLinkedList() for x in range(len(oldArray) * 2)]
        self._count = 0
        
        for linkedList in oldArray:
            if linkedList.get_count() > 0:
                for hashNode in linkedList:
                    self.add(hashNode.key, hashNode.value)


    def remove(self, key):
        index = self._get_index(key)
        linkedList = self._values[index]
        
        nodeToRemove = None
        notFound = True

        for hashNode in linkedList:
            if hashNode.key == key:
                nodeToRemove = hashNode
                notFound = False
                break
        
        if notFound:
            raise ValueError("A node with the supplied key was not found")
        else:
            linkedList.remove(nodeToRemove)
            self._count -= 1




    def get_count(self):
        return self._count


    def contains(self, key):
        index = self._get_index(key)
        linkedList = self._values[index]
        if linkedList.get_count() > 0:
            for hashNode in linkedList:
                    if hashNode.key == key:
                        return True
        return False
