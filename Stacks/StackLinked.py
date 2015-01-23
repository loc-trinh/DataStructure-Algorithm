"""
LIFO Stack implementation using a singly linked list for storage.
Operation       Running Time
----------------------------
S.push(e)      	O(1)
S.pop()         O(1)
S.peek()        O(1)
S.is_empty()    O(1)
len(S)          O(1)
* require more space than an array implementation

"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Stack:

	#------------------- nested Node class ---------------------
	class _Node:
		"""Lightweight, nonpublic class for storing a singly linked node."""
		__slots__ = '_element', '_next'

		def __init__(self, element, next):
			self._element = element
			self._next = next

	#------------------- public methods -------------------
	def __init__(self):
		"""Create an empty stack."""
		self._head = None
		self._size = 0

	def __len__(self):
		"""Return the number of elements in the stack."""
		return self._size

	def is_empty(self):
		"""Return True if the stack is empty."""
		return self._size == 0

	def peek(self):
		"""Return (but) do not remove the element at the top of the stack.
		Raise Empty exception if the stack is empty."""
		if self.is_empty():
			raise Empty('Stack is empty.')
		return self._head._element

	def push(self, e):
		"""Add element to the top of the stack."""
		self._head = self._Node(e, self._head)
		self._size += 1

	def pop(self):
		"""Remove and return the element from the top of the stack.
		Raise Empty exception if the stack is empty."""
		if self.is_empty():
			raise Empty('stack is empty')
		value = self._head._element
		self._head = self._head._next
		self._size -= 1
		return value


