from deque import Deque

dq = Deque()

# dq.enqueue_head('First')
# dq.enqueue_head('Second')
# dq.enqueue_head('Third')
# dq.enqueue_head('Forth')

dq.enqueue_tail('First')
dq.enqueue_tail('Second')
dq.enqueue_tail('Third')
dq.enqueue_tail('Forth')

# dq.dequeue_head()
# dq.dequeue_head()
# dq.dequeue_tail()
# dq.dequeue_tail()

# print(dq.peak_head())
# print(dq.peak_tail())

for data in dq:
    print(data)