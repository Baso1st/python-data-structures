
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self._count = 0
        self._head = None
        self._tail = None


    def get_count(self):
        return self._count


    def get_head(self):
        return self._head


    def get_tail(self):
        return self._tail


    def add_head(self, data):
        newNode = DNode(data)

        if self._count == 0:
            self._head = self._tail = newNode
        else:
            self._head.previous = newNode
            newNode.next = self._head
            self._head = newNode
        
        self._count += 1



    def add_tail(self, data):
        pass


    def remove_head(self):
        pass


    def remove_tail(self):
        pass


    def remove(self, data):
        pass


    def __iter__(self):
        pass