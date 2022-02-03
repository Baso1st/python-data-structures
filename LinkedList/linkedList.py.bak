""" Hosts the linkedList class and the Node class"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    head = None
    tail = None

    def __init__(self):
        self._count = 0

    def get_count(self):
        """Returns the number of nodes in the linkedlist"""
        return self._count

    def add_first(self, data):
        newNode = Node(data)
        if (self._count == 0):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

        self._count += 1

        
    def add_last(self, data): 
        newNode = Node(data)
        if(self._count == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self._count += 1
        

    def remove_first(self):
        if self._count == 0:
            return
            
        if self._count == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        self._count -= 1
            

    def remove_last(self):
        if self._count == 0:
            return

        if self._count == 1:
            self.head = self.tail = None
        else:
            currentNode = self.head
            previousNode = None
            while currentNode.next is not None:
                previousNode = currentNode
                currentNode = currentNode.next
            self.tail = previousNode
            self.tail.next = None

        self._count -= 1


    def __iter__(self):
        currentNode = self.head
        while currentNode is not None:
            yield currentNode.data
            currentNode = currentNode.next
