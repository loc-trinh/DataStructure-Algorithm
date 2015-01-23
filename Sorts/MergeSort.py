""" Implementation of merge sort algorithm """

def _merge(first, second, container):
	i = j = 0
	while i + j < len(container):
		if (j == len(second)) or (i < len(first) and first[i] < second[i]):
			container[i + j] = first[i]
			i += 1
		else:
			container[i + j] = second[j]
			j += 1

def sort(container):
	size = len(container)
	if size < 2:
		return

	mid = size / 2
	first = container[0:mid]
	second = container[mid: size]

	sort(first)
	sort(second)

	_merge(first, second, container)