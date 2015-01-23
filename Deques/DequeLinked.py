class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Deque:
    """Double-ended queue implementation using a doubly linked list with as underlying storage"""

    #--------------------- nested Node class ----------------------
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    #---------------------- public methods -------------------------
    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def peek_head(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element

    def peek_tail(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element

    def push_head(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)

    def push_tail(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def pop_head(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next)

    def pop_tail(self):
        """Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev)

    #----------------------- non public methods --------------------------
    def _insert_between(self, e, predecessor, sucessor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, sucessor)
        predecessor._next = newest
        sucessor._prev = newest
        self._size += 1
        return newest._element

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        sucessor = node._next
        predecessor._next = sucessor
        sucessor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

