from stack import Stack

stack = Stack()

stack.push('First')
stack.push('Second')
stack.push('Third')
stack.push('Forth')

print(stack.get_count())
print(stack.peek())
# print(stack._dataList)
print('--------------')

# print(stack.pop())
# print(stack.pop())
# print(stack.get_count())
# print(stack.pop())
# print(stack.pop())
# print(stack.get_count())

for item in stack:
    print(item)
