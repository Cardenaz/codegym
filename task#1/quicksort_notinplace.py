


def quicksort_notinplace(array):
    left, equal, right = [], [], []
    if len(array) > 1: 
        pivot = array[-1]

        for value in array:
            if value < pivot: 
                left.append(value)
            elif value == pivot: 
                equal.append 
            elif value > pivot: 
                right.append(value)
        
        return quicksort_notinplace(left) + equal + quicksort_notinplace(right)
    else: 
        return array



