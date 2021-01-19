def quicksort_inplace(array):
    if len(array) < 2: 
        return array 
    else: 
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_inplace(less) + [pivot] + quicksort_inplace(greater)






