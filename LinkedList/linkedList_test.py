from linkedList import LinkedList, Node 

linkedList = LinkedList()

linkedList.add_first('First')
linkedList.add_first('Second')
linkedList.add_first('Third')
linkedList.add_first('Forth')


# print(linkedList.head.data)
# print(linkedList.tail.data)
# print(linkedList.get_count())

# print('-----------------')

# testNode = linkedList.head

# while testNode is not None:
#     print(testNode.data)
#     testNode = testNode.next


# iterator = iter(linkedList)
# nextdata = next(iterator)
# print(nextdata)

for data in linkedList:
    print(data)
