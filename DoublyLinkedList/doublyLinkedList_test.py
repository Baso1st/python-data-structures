from doublyLinkedList import DoublyLinkedList

dlist = DoublyLinkedList()

dlist.add_head('First')
dlist.add_head('Second')
dlist.add_head('Third')
dlist.add_head('Forth')

print(dlist._head.data)
print(dlist._tail.data)