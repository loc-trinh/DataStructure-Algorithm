"""
A min-oriented priority queue implemented with a array-based binary heap.
Operation       Running Time
----------------------------
S.enqueue(e)    O(log n)
S.dequeue()     O(log n)
S.peek()        O(1)
S.is_empty()    O(1)
len(S)          O(1)

"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class PriorityQueue:
	
	#---------------------- nested Item class ----------------------
	class _Item:
		"""Lightweight composition store priority queue items ."""
		__slots__ = '_key', '_value'

		def __init__(self, k, v):
			self._key = k
			self._value = v

		def __lt__(self, other):
			return self._key < other._key

	#--------------------- public methods --------------------------
	def __init__(self, contents=()):
		"""Create a new empty Priority Queue."""
		self._data = [self._Item(k,v) for k,v in contents] #empty by default
		if len(self._data) > 1:
			self._heap_construction()

	def __len__(self):
		"""Return the size of the Priority Queue."""
		return len(self._data)

	def is_empty(self):
		"""Return True if the priority queue is empty."""
		return len(self) == 0

	def peek(self):
		"""Return but do not remove (k,v) tuple with minimum key.
		Raise Empty exception if empty."""
		if self.is_empty():
			raise Empty('Priority queue is empty')
		item = self._data[0]
		return (item._key, item._value)

	def enqueue(self, key, value):
		"""Add a key-value pair to the priority queue."""
		self._data.append(self._Item(key,value))
		self._upheap(len(self._data) - 1)

	def dequeue(self):
		"""Remove and return (k,v) tuple with minimum key.
		Raise Empty exception if empty."""

		if self.is_empty():
			raise Empty('Priority queue is empty')
		self._swap(0, len(self._data) - 1)
		item = self._data.pop()
		self._downheap(0)
		return (item._key, item._value)

	#--------------------- non public methods -----------------------
	def _parent(self, i):
		"""Return parent index of node i"""
		return (i - 1) // 2

	def _left(self, i):
		"""Return left child index of node i"""
		return 2 * i + 1

	def _right(self, i):
		"""Return right child index of node i"""
		return 2 * i + 2

	def _has_left(self, i):
		"""Return True if node at i has left child"""
		return self._left(i) < len(self._data)

	def _has_right(self, i):
		"""Return True if node at i has right child"""
		return self._right(i) < len(self._data)

	def _swap(self, i, j):
		"""Swap the elements at indices i and j of array"""
		self._data[i], self._data[j] = self._data[j], self._data[i]

	def _upheap(self, i):
		parent = self._parent(i)
		if i > 0 and self._data[i] < self._data[parent]:
			self._swap(i, parent)
			self._upheap(parent)

	def _downheap(self, i):
		if self._has_left(i):
			left = self._left(i)
			small_child = left
			if self._has_right(i):
				right = self._right(i)
				if self._data[right] < self._data[left]:
					small_child = right

			if self._data[small_child] < self._data[i]:
				self._swap(i, small_child)

	def _heap_construction(self):
		"""Bottom up construction in linear time"""
		start = self._parent(len(self) - 1)
		for i in range(start, -1, -1):
			self._downheap(i)