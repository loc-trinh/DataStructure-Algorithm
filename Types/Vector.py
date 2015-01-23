class Vector:
	"""Represent a vector in multidemensional space"""

	def __init__(self, d):
		"""Create a d-dimension vector of O's"""
		self._coords = [0] * d

	def __len__(self):
		"""Return the dimension of the vector"""
		return len(self._coords)

	def __getitem__(self, j):
		"""Return jth coordinate of vector."""
		return self._coords[j]

	def __setitem__(self, j, value):
		"""Set jth coordinate of vector to given value."""
		self._coords[j] = value

	def __add__(self, other):
		"""Return sum of two vectors."""
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = Vector(len(self))
		for j in range(len(self)):
			result[j] = self[j] + other[j]
		return result

	def __eq__(self, other):
		"""Return True if vector has same coordinates as other."""
		return self._coords == other._coords

	def __ne__(self, other):
		"""Return True if vector differs from other"""
		return not self == other

	def __str__(self):
		"""Produce string representation of vector"""
		return '<' + str(self._coords)[1:-1] + '>'

	def dot(self, other):
		"""Return the dot product of vector and other"""
		if len(self) != len(other):
			raise ValueError('dimensions must agree')
		result = 0
		for j in range(len(self)):
			result += self[j] * other[j]
		return result
