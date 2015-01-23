   """ Implementation of insertion sort """

def sort(containers):
	for i in range(1, len(containers)):
		j = i
		while j > 0 and containers[j] < containers[j-1]:
			containers[j], containers[j-1] = containers[j-1], containers[j]
			j -= 1