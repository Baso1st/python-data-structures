from doublyLinkedList import DoublyLinkedList

dlist = DoublyLinkedList()

dlist.add_head('First')
dlist.add_head('Second')
dlist.add_head('Third')
dlist.add_head('Forth')

# dlist.add_tail('First')
# dlist.add_tail('Second')
# dlist.add_tail('Third')
# dlist.add_tail('Forth')

# dlist.remove_head()
# dlist.remove_head()

# dlist.remove('Second')

# print(dlist._head.data)
# print(dlist._tail.data)

for data in dlist:
    print(data)