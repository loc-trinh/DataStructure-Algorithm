"""
LIFO Stack implementation using Python list as underlying storage.
Operation       Running Time
----------------------------
S.push(e)       Amortized O(1)
S.pop()         Amortized O(1)
S.peek()        O(1)
S.is_empty()    O(1)
len(S)          O(1)

"""

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Stack:
    
    def __init__(self):
        """Create an empty stack"""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self) == 0

    def peek(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def pop(self):
        """Remove and return the element from the top of the stack
        Raise Empty exception if the stack is empty."""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
        



