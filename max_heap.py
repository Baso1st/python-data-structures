
class max_heap:

	def __init__(self):
		self.items = []

	def has_parent(self, idx):
		parent_idx = (idx - 1) // 2
		if parent_idx >= 0:
			return True
		return False

	def has_left_child(self, idx):
		left_child_idx = idx * 2 + 1
		if left_child_idx > len(self.items) - 1:
			return False
		return True

	def has_right_child(self, idx):
		left_child_idx = idx * 2 + 2
		if left_child_idx > len(self.items) - 1:
			return False
		return True

	def get_parent_idx(self, idx):
		return (idx - 1) // 2

	def get_left_child_idx(self, idx):
		return idx * 2 + 1

	def get_right_child_idx(self, idx):
		return idx * 2 + 2

	def peek(self):
		if not self.items:
			raise Exception("The heap is empty")
		return self.items[0]

	def add(self, value):
		self.items.append(value)
		self.heapify_up()

	def poll(self):
		if not self.items:
			raise Exception("The heap is empty")
		item = self.items[0]
		self.items[0] = self.items.pop()
		self.heapify_down()
		return item

	def heapify_up(self):
		idx = len(self.items) - 1
		while self.has_parent(idx):
			parent_idx = self.get_parent_idx(idx)
			if self.items[parent_idx] < self.items[idx]:
				self.items[parent_idx], self.items[idx] = self.items[idx], self.items[parent_idx]

			idx = parent_idx

	def heapify_down(self):
		idx = 0
		while self.has_left_child(idx):
			bigger_child_idx = self.get_left_child_idx(idx)
			if self.has_right_child(idx):
				right_idx = self.get_right_child_idx(idx)
				if self.items[right_idx] > self.items[bigger_child_idx]:
					bigger_child_idx = right_idx
			if self.items[idx] < self.items[bigger_child_idx]: 
				self.items[idx], self.items[bigger_child_idx] = self.items[bigger_child_idx], self.items[idx]
			idx = bigger_child_idx



if __name__ == '__main__':
    heap = max_heap()
    heap.add(2)
    heap.add(5)
    heap.add(3)
    heap.add(9)
    heap.add(1)
    print(heap.peek())
    heap.poll()
    print(heap.peek())
    heap.poll()
    print(heap.peek())
