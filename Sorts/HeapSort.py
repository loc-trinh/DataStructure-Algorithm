   """ Implementation of heap sort """

import heapq

def sort(containers):
	heapq.heapify(containers)
	containers[:] = [heapq.heappop(containers) for i in range(len(containers))]