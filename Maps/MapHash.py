"""
Hash map implemented with separate chaining for collision resolution.
Operation 					Running Time
------------------------------------------
getitem 					O(1) expected, O(n) worst
setitem 					O(1) expected, O(n) worst
getitem 					O(1) expected, O(n) worst
len 						O(1)
iter 						O(n)

"""

from collections import MutableMapping
import MapUnsorted, random

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


	#-------------------- public methods ---------------------------
	def __init__(self, cap = 11, p=109345121):
		"""Create an empty hash-table map."""
		self._table = cap * [None]
		self._n = 0
		self._prime = p
		self._scale = 1 + random.randrange(p-1)
		self._shift = random.randrange(p)

	def __len__(self):
		return self._n

	def __iter__(self):
		for bucket in self._table:
			if bucket is not None:
				for key in bucket:
					yield key

	def _hash_function(self, k):
		return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

	def __getitem__(self, k):
		j = self._hash_function(k)
		return self._bucket_getitem(j, k)

	def __setitem__(self, k, v):
		j = self._hash_function(k)
		self._bucket_setitem(j, k, v)
		if self._n > len(self._table) // 2:
			self._resize(2 * len(self._table) - 1)

	def __delitem__(self, k):
		j = self.hash_function(k)
		self._bucket_delitem(j, k)
		self._n -= 1


	#------------------- nonpublic bucket implementation ---------------
	def _resize(self, c):
		old = list(self.item())
		self._table = c * [None]
		self._n = 0
		for (k, v) in old:
			self[k] = v

	def _bucket_getitem(self, j, k):
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('Key Error: ' + repr(k))	
		return bucket[k]

	def _bucket_setitem(self, j, k, v):
		if self._table[j] is None:
			self._table[j] = MapUnsorted.Map()
		oldsize = len(self._table[j])
		self._table[j][k] = v
		if len(self._table[j]) > oldsize:
			self._n += 1

	def _bucket_delitem(self, j, k):
		bucket = self._table[j]
		if bucket is None:
			raise KeyError('Key Error: ' + repr(k))
		del bucket[k]

