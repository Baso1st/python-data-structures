from trie import Trie

trie = Trie()

trie.add('abcdefg')
trie.add('abc')
trie.add('abcd')
trie.add('defg')
trie.add('abcdefgh')


# trie.__iter__()

for key in trie:
    print(key)

# print(trie.get_count())

# print(trie.contains('abcdefgh'))