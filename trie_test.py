from trie import Trie

trie = Trie()

trie.add('abcdefg')
trie.add('abc')
trie.add('abgl')
trie.add('abcd')
trie.add('defg')
trie.add('abz')
trie.add('abcdefgh')
trie.add('xyz')
trie.add('aul')

# print(trie.get_all_words())

# trie.remove('abcdefg')
# trie.remove('abc')
# trie.remove('abgl')
# trie.remove('abcd')
# trie.remove('defg')
# trie.remove('abz')
# trie.remove('abcdefgh')
# trie.remove('xyz')
# trie.remove('aul')

# trie.remove_using_prefix('ab')

# print(trie.get_all_words())


print(trie.contains_words_with_prefix('aule'))


# trie.__iter__()

# for key in trie:
#     print(key)

# print(trie.get_count())

# print(trie.contains('abcdefgh'))