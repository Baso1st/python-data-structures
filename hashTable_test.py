from hashTable import HashTable, HashNode

hash = HashTable()

# Test adding

hash.add('IN', 'Indiana')
hash.add('OH', 'Ohio')
hash.add('NY', 'New York')
hash.add('CA', 'California')
hash.add('AK', 'Alaska')

# Test removing and Contains

# if hash.contains('IN'):
#     hash.remove('IN')

# if hash.contains('OU'):
#     hash.remove('OU')

# Testing adding a duplicate key with different values

# hash.add('IN', 'Indiana')
# hash.add('OH', 'Ohio')
# hash.add('OH', 'Ohio')

# Test get count

# print(hash.get_count())

# Test get indexer

# print(hash['IN'])
# print(hash['CA'])
# print(hash['OereH'])

# Test set indexer

hash['IN'] = 'InsideOut'
print(hash['IN'])

# Test iteration

# print(len(hash._values))

# for node in hash:
#     print(node.key,':', node.value)