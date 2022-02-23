
from math import fabs


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False



class Trie:
    def __init__(self) -> None:
        self._root = TrieNode()
        self._count = 0


    def __iter__(self):
        return self._recursive_iter(self._root)


    def _recursive_iter(self, node: TrieNode):
        for childKey in node.children:
            yield childKey
            yield from self._recursive_iter(node.children[childKey])
            

    def add(self, word):
        self._recursive_add(self._root, word, 0)


    def _recursive_add(self, node: TrieNode, word: str, index: int):
        if index >= len(word):
            node.isEndOfWord = True
            return
        
        char = word[index]
        if char in node.children:
            nextNode = node.children[char]
        else:
            nextNode = TrieNode()
            node.children[char] = nextNode
            self._count += 1

        self._recursive_add(nextNode, word, index + 1)


    def remove(self, word):
        pass


    def contains(self, word) -> bool:
        if len(word) == 0:
            return False
        return self._recursive_search(self._root, word, 0)


    def _recursive_search(self, node: TrieNode, word, index):
        if index == len(word):
            return node.isEndOfWord

        char = word[index]
        if char not in node.children:
            return False

        nextNode = node.children[char]
        return self._recursive_search(nextNode, word, index + 1)


    def get_count(self):
        return self._count



