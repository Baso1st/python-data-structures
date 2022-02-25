
class TrieNode:
    def __init__(self):
        self.children: dict = {}
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
        self._add_recursive(self._root, word, 0)


    def _add_recursive(self, node: TrieNode, word: str, index: int):
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

        self._add_recursive(nextNode, word, index + 1)


    def remove(self, word):
        """Removes the word sent in the argument"""
        if not self.contains(word):
            return
        self._remove_recursive(self._root, word, 0)

    
    def _remove_recursive(self, node: TrieNode, word, index):
        if index < len(word):
            char = word[index]
            nextNode = node.children[char]
            if len(nextNode.children) > 0:
                self._remove_recursive(nextNode, word, index + 1)
                if len(nextNode.children) == 0 and not nextNode.isEndOfWord:
                    node.children.pop(char)
            else:
                node.children.pop(char)
                self._count -= 1
                return
        elif node.isEndOfWord:
            node.isEndOfWord = False
            self._count -= 1



    def contains(self, word) -> bool:
        if len(word) == 0:
            return False
        return self._search_recursive(self._root, word, 0)


    def _search_recursive(self, node: TrieNode, word, index):
        if index == len(word):
            return node.isEndOfWord

        char = word[index]
        if char not in node.children:
            return False

        nextNode = node.children[char]
        return self._search_recursive(nextNode, word, index + 1)


    def contains_words_with_prefix(self, prefix):
        return self._contains_with_prefix_recursive(self._root, prefix, 0)


    def _contains_with_prefix_recursive(self, node:TrieNode, prefix, index):
        if index == len(prefix):
            return True

        char = prefix[index]
        if char in node.children:
            nextNode = node.children[char]
            return self._contains_with_prefix_recursive(nextNode, prefix, index + 1)
        
        return False


    def get_count(self):
        """Returns the number of litters in the Trie"""
        return self._count


    def get_all_words(self):
        """Returns a list of all the words stored in the Trie"""
        words = []
        self._all_words_recursive(self._root, [], words)
        return words

    
    def _all_words_recursive(self, node: TrieNode, word: list, words: list):
        if node.isEndOfWord:
            words.append(''.join(word))

        for child in node.children:
            newWord = word.copy()
            newWord.append(child)
            nextNode = node.children[child]
            self._all_words_recursive(nextNode, newWord, words)
                    

    def remove_using_prefix(self, prefix):
        """Removes all the words that start with the provided prefix"""
        self._remove_using_prefix_recursive(self._root, prefix, 0)


    def _remove_using_prefix_recursive(self, node: TrieNode, prefix,  index):
        if index < (len(prefix) - 1):
            char = prefix[index]
            nextNode: TrieNode = node.children[char]
            self._remove_using_prefix_recursive(nextNode, prefix, index + 1)
            if len(nextNode.children) == 0 and not nextNode.isEndOfWord:
                node.children.pop(char)
        else:
            node.children.pop(prefix[index])
            self._count -= 1
            