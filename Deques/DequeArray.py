"""
Double-ended queue implementation using a circular list as underlying storage
Operation       Running Time
----------------------------
S.push_head(e)  Amortized O(1)
S.push_tail(e)  Amortized O(1)
S.pop_head(e)   Amortized O(1)
S.pop_tail(e)   Amortized O(1)
S.peek_head()   O(1)
S.peek_tail()   O(1)
S.is_empty()    O(1)
len(S)          O(1)

"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Deque:
    
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Creaet an empty queue."""
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def peek_head(self):
        """Return (but do not remove) the element at the front of the queue.        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def peek_tail(self):
        """Return (but do not remove) the element at the back of the queue.        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        return self._data[back]

    def pop_head(self):
        """Remove and return the first element at the front of the queue
        Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return value

    def pop_tail(self):
        """Remove and return the first element at the back of the queue
        Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        value = self._data[back]
        self._data[back] = None
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return value

    def push_head(self, e):
        """Add an element to the front of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        cur = (self._front - 1) % len(self._data)
        self._data[cur] = e
        self._size += 1
        self._front = (self._front - 1) % len(self._data)

    def push_tail(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        cur = (self._front + self._size) % len(self._data)
        self._data[cur] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity > len(self)"""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0