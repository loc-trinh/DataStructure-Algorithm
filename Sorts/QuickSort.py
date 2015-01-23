""" Implementation of quick sort """

def sort(containers):
    if len(containers) > 1:
        pivot_index = len(containers) / 2
        smaller_containers = []
        larger_containers = []

        for i, val in enumerate(containers):
            if i != pivot_index:
                if val < containers[pivot_index]:
                    smaller_containers.append(val)
                else:
                    larger_containers.append(val)

        sort(smaller_containers)
        sort(larger_containers)
        containers[:] = smaller_containers + [containers[pivot_index]] + larger_containers