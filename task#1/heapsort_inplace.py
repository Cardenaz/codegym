import heapq 

def heapsort_inplace(array): 
    heap_list = []
    sorted_heap_list = []
    for item in array: 
        heapq.heappush(heap_list, item)
    for _ in range(len(heap_list)):
        sorted_heap_list.append(heapq.heappop(heap_list))
    return sorted_heap_list



