"""Implementation of bubble sort"""

def sort(containers):
	for i in range(len(containers)):
		for j in range(len(containers) - 1 - i):
			if containers[j] > containers[j+1]:
				containers[j], containers[j+1] = containers[j+1], containers[j]