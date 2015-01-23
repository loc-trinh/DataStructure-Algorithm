class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Queue:
    """FIFO queue implementation using a Python list as underlying storage"""

    def __init__(self):
        """Creaet an empty queue."""
        self._data = []
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def peek(self):
        """Return (but do not remove) the element at the front of the queue.        
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def enqueue(self, e):
        """Add an element to the back of queue."""
        self._data.append(e)
        self._size += 1

    def dequeue(self):
        """Remove and return the first element of the queue
        Raise Empty exception if the queue is empty"""
        if self.is_empty():
            raise Empty('Queue is empty')
        value = self._data[self._front]
        self._data[self._front] = None
        self._front = self._front + 1
        self._size -= 1

        if 0 < self._size < len(self._data) // 4:
            self._resize()
        return value

    def _resize(self):
        """Resize to a new list of capacity > len(self)"""
        new = []
        for i in range(self._size):
            new.append(self._data[self._front])
            self._front += 1
        self._data = new
        self._front = 0