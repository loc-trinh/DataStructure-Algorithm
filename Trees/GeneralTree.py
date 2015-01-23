"""
Linked representation of a general tree structure.

"""

import AbstractTreeBase

class Tree(AbstractTreeBase.Tree):

    #------------- nested Node class and Position wrapper -------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_children'
        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._parent = parent
            self._children = children if children is not None else []

    class Position(TreeBase.Tree.Position):
        """An wrapper abstraction representing the location of a single element."""
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Return the element sotred at this Position."""
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node


    #------------- utility functions for wrapping & unwrapping nodes ------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for a given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    #----------------------- public methods ------------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree(or None if p is root)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        node = self._validate(p)
        for child in node._children:
            yield self._make_position(child)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        return len(node._children)

    def positions(self):
        """Generate an iteration of the tree's positions."""
        if not self.is_empty():
            return self._eulertour(self.root())
            #return self._preorder(self.root())
            #return self._preorder(self.root())
            #return self._breathfirst(self.root())
            #return self._depthfirst(self.root())

    #---------------------- non public methods ------------------------
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty."""
        if self._root is not None: raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_children(self, p, e):
        """Create a new  child for Position p, storing element e. Return the Position of new node.
        Raise ValueError if Position p is invalid"""
        node = self._validate(p)
        self._size += 1
        new_node = self._Node(e, node)
        node._children.append(new_node)
        return self._make_position(new_node)

    def _replace(self, p, e):
        """Replace the element at position p with e, an return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children."""
        node = self._validate(p)
        if self.num_children(p) > 1: raise ValueError('p has more than one children')
        child = self._children[0] if self._children else None
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else: 
            parent = node._parent
            parent._children.append(child)
        self._size -= 1
        node._parent = node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position msut be leaf')
        if not type(self) is type(t1) is type(t2): raise TypeError('Three types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._children.append(t1._root)
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root.parent = node
            node._children.append(t2._root)
            t2._root = None
            t2._size = 0

