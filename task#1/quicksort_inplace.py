import random 

def quicksort_inplace(array):
    if len(array) < 2: 
        return array 
    else:
        random_pivot = random.randrange(0, len(array)-1)
        pivot = array[random_pivot]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_inplace(less) + [pivot] + quicksort_inplace(greater)







