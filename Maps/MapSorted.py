"""
Map implementation using an sorted list.
Operation							Running Time
--------------------------------------------------
len(M)								O(1)
k in M 								O(log n)
M[k] = v 							O(n) worst, O(log n) if exist
del M[K] 							O(n) worst
find_min, find_max					O(1)
find_gt, find_lt					O(log n)
iter(M), reversed(M)				O(n)
"""

from collections import MutableMapping

class Map(MutableMapping):

	#------------------- nested Item class ------------------------
	class _Item:
		"""Lightweight composite to store key-value pairs as map items."""
		__slots__ = '_key', '_value'

		def __init__(self, k, v):
			self._key = k
			self._value = v

		def __eq__(self, other):
			return self._key == other._key

		def __ne__(self, other):
			return not (self == other)

		def __lt__(self, other):
			return self._key < other._key

	#------------------ non public behaviors ---------------------
	def _find_index(self, k, low, high):
		"""Return the index of the leftmost item with key greater than or equal to k.
		Return high + 1 if no such item qualifies.
		"""
		if high < low:
			return high + 1
		else:
			mid = (low + high) // 2
			if k == self._table[mid]._key:
				return mid
			elif k < self._table[mid]._key:
				return self._find_index(k, low, mid-1)
			else:
				return self._find_index(k, mid + 1, high)

	#-------------------- public behaviors ------------------------
	def __init__(self):
		"""Create an empty map."""
		self._table = []

	def __len__(self):
		"""Return number of items in the map."""
		return len(self._table)

	def __iter__(self):
		"""Generate keys of the map ordered from minimum to maximum."""
		for item in self._table:
			yield item._key

	def __reversed__(self):
		"""Generate keys of the map ordered from maximum to minimum."""
		for item in reversed(self._table):
			yield item._key

	def __getitem__(self, k):
		"""Return value associated with key k (raise KeyError if not found)."""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j == len(self._table) or self._table[j]._key != k:
			raise KeyError('Key Error: ' + repr(k))	
		return self._table[j]._value

	def __setitem__(self, k, v):
		"""Assign value to v to key k, overwriting existing value if present."""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k:
			self._table[j]._value = v
		else:
			self._table.insert(j, self._Item(k, v))

	def __delitem__(self, k):
		"""Remove item associated with key k (raise KeyError if not found."""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j == len(self._table) or self._table[j]._key != k:
			raise KeyError('Key Error: ' + repr(k))
		self._table.pop(j)

	#----------------------- locating methods ------------------------
	def find_min(self):
		"""Return (key, value) pair with minimum key (or None if empty)."""
		if len(self._table) > 0:
			return (self._table[0]._key, self._table[0]._value)
		else:
			return None

	def find_max(self):
		"""Return (key, value) pair with maximum key (or None if empty)."""
		if len(self._table) > 0:
			return (self._table[-1]._key, self._table[-1]._value)
		else:
			return None

	def find_lt(self, k):
		"""Return (key, value) pair with greates key less than k."""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j > 0:
			return (self._table[j-1]._key, self._table[j-1]._value)
		else:
			return None

	def find_gt(self, k):
		"""Return (key, value) pair with leasat key strictly greater than k."""
		j = self._find_index(k, 0, len(self._table) - 1)
		if j < len(self._table) and self._table[j]._key == k:
			j += 1
		if j < len(self._table):
			return (self._table[j]._key, self._table[j]._value)
		else:
			return None

	def find_range(self, start, stop):
		"""Iterate all (key, value) pairs such taht start <= key < stop.
		If start is None, iteration begins with minimum key of map.
		if stop is None, iteration continues through the maximum key of map."""
		if start is None:
			j = 0
		else:
			j = self._find_index(start, 0, len(self._table) - 1)
		while j < len(self._table) and (stop is None or self._table[j]._key < stop):
			yield (self._table[j]._key, self._table[j]._value)
			j += 1