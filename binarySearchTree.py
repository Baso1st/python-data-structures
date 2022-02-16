
from logging import root
from turtle import right


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:                
            parentNode = currentNode = self.root
            shouldBeLeft = True
            while currentNode is not None:
                parentNode = currentNode
                if data < currentNode.data:
                    currentNode = currentNode.left
                    shouldBeLeft = True
                else: 
                    currentNode = currentNode.right
                    shouldBeLeft = False

            if shouldBeLeft:
                parentNode.left = TreeNode(data)
            else:
                parentNode.right = TreeNode(data)



    def remove(self, data):
        pass


    def pre_order_traversal(self, action):
        self.__pre_order_traversal(self.root, action)


    def __pre_order_traversal(self, node, action):
        if node is not None:
            action(node)
            self.__pre_order_traversal(node.left, action)
            self.__pre_order_traversal(node.right, action)


    def in_order_traversal(self, action):
        self.__in_order_traversal(self.root, action)

    
    def __in_order_traversal(self, node, action):
        if node is not None:
            self.__in_order_traversal(node.left, action)
            action(node)
            self.__in_order_traversal(node.right, action)


    def post_order_traversal(self, action):
        self.__post_order_traversal(self.root, action)

    
    def __post_order_traversal(self, node, action):
        if node is not None:
            self.__post_order_traversal(node.left, action)
            self.__post_order_traversal(node.right, action)
            action(node)

    
    def __iter__(self):
        return self._iter_helper(self.root)
        

    def _iter_helper(self, node):
        if node is not None:
            yield from self._iter_helper(node.left)
            yield node.data
            yield from self._iter_helper(node.right)


    def remove(self, data):
        (node, parent) = self.findWithParent(data)
        
        if node is None:
            return

        # # first case: leaf node with no children
        if node.left is None and node.right is None:
            if self.root == node:
                self.root = None
                return

            if node.data < parent.data:
                parent.left = None
            else:
                parent.right = None
            return
                
        # second case: remove a node with one child
        if bool(node.left) ^ bool(node.right):
            theChild = node.left if node.left is not None else node.right
            if node == self.root:
                self.root = theChild
                return
            
            if node.data < parent.data:
                parent.left = theChild
            else:
                parent.right = theChild
            return
        
        # Third case: remove a node with two children
        # Take the left most child of the right child and put it in place of the removed node
        left_most_child = node.right
        left_child_parent = node
        while left_most_child.left is not None:
            left_child_parent = left_most_child
            left_most_child = left_most_child.left
        
        if left_most_child != node.right:
            left_child_parent.left = left_most_child.right

        left_most_child.left = node.left
        left_most_child.right = node.right

        if node.data < parent.data:
            parent.left = left_most_child
        else:
            parent.right = left_most_child

        # if left_most_child == node.right:
        #     if node.data < parent.data:
        #         parent.left = node.right
        #     else:
        #         parent.righ = node.right
        # else:
        #     left_child_parent.left = node.right
        #     if node.data < parent.data:
        #         parent.left = node.right
        #     else:
        #         parent.righ = node.right


    def findWithParent(self, data):
        """Returns a tuple (node, node's parent) for the node of the data in the parameter"""
        currentNode = self.root
        parentNode = None
        while currentNode is not None:
            if currentNode.data == data:
                return (currentNode, parentNode)
            elif  data < currentNode.data :
                parentNode = currentNode
                currentNode = currentNode.left
            else:
                parentNode = currentNode
                currentNode = currentNode.right

