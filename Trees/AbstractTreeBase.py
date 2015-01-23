import collections.QueueArray
import collections.StackArray

class Tree:
    """Abstract base class representing a tree structure."""

    #-------------------- nested Position class ---------------------
    class Position:
        """Abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)


    #----- abstact methods that concrete subclass must support -------
    def __len__(self):
        """Return the total nmber of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return Position representing the p's parent (or None if empty)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def positions(self):
        """Generate an iteration of the tree's positions."""
        raise NotImplementedError('must be implemented by subclass')


    # ---------- concrete methods implemented in this class ------------
    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.positions():
            yield p.element()

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the number of levels separating Position p from the root."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p = None):
        """Return the height of the subtree rooted at Position p.
        if p is None, return the height of the entire tree"""
        if p is None:
            p = self.root()

        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(p))


    #---------------------- traversal algorithms ------------------------   
    def _preorder(self, p):
        """Generate a preorder iteration of positions in the tree."""
        yield p
        for child in self.children(p):
            for other in self._preorder(child):
                yield other

    def _postorder(self, p):
        """Generate a postorder iteration of positions in the tree."""
        for child in self.children(p):
            for other in self._preorder(child):
                yield other
        yield p

    def _eulertour(self, p):
        """Generate a euler tour iteration of positions in the tree."""
        yield p
        for child in self.children(p):
            for other in self._eulertour(child):
                yield other
        yield p

    def _breathfirst(self, p):
        """Generate a breadth-first iteration of the positions of the tree."""
        queue = QueueArray.Queue()
        queue.enqueue(p)
        while not queue.is_empty():
            p = queue.dequeue()
            yield p
            for child in self.children(p):
                queue.enqueue(child)

    def _depthfirst(self, p):
        """Generate a depth-first iteration of the positions of the tree."""
        stack = StackArray.Stack()
        stack.push(p)
        while not stack.is_empty():
            p = stack.pop()
            yield p
            for child in self.children(p):
                stack.push(child)

