
from os import remove
from binarySearchTree import BinarySearchTree


def printNodeData(treeNode):
    print(treeNode.data)

def __yield_method(node):
    # yield node.data
    print(node.data)

bTree = BinarySearchTree()

# bTree.add(9)
# bTree.add(3)
# bTree.add(2)
# bTree.add(1)
# bTree.add(4)
# bTree.add(7)
# bTree.add(6)

bTree.add(50)
bTree.add(25)
bTree.add(20)
bTree.add(30)
bTree.add(10)
bTree.add(15)
bTree.add(100)
bTree.add(80)
bTree.add(60)
bTree.add(70)
bTree.add(200)
bTree.add(180)
bTree.add(160)
bTree.add(165)
bTree.add(190)
bTree.add(300)

# print(bTree.root.left.left.left.data) #Should be 1
# print(bTree.root.left.right.data) # Should be 4

# bTree.pre_order_traversal(printNodeData)
# bTree.in_order_traversal(printNodeData)
# bTree.post_order_traversal(printNodeData)


bTree.remove(25)

for data in bTree:
    print(data)

# (node, parent) = bTree.findWithParent(10)
# print(bool(parent) ^ bool(node))
# print(None if parent is None else parent.data, node.data)