"""Implementation of selection sort"""

def sort(containers):
	for i in range(len(containers)):
		min = i
		for k in range(i+1, len(containers)):
			if containers[k] < containers[min]:
				min = k
		containers[i], containers[min] = containers[min], containers[i]