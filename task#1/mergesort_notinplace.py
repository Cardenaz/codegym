def mergesort_notinplace(array):
    #divide into sublists 
    if len(array) < 2: 
        return array
    midpoint = len(array)// 2 
    first = array[:midpoint]
    second = array[midpoint:]
    half_first = mergesort_notinplace(first)
    half_second = mergesort_notinplace(second)
    return merge(half_first, half_second)

def merge(first, second): 
    i = j = 0 
    sorted_array = []
    while i < len(first) and j < len(second): 
        if first[i] < second[j]:
            sorted_array.append(first[i])
            i += 1 
        else: 
            sorted_array.append(second[j])
            j += 1 
    if i == len(first): 
        item = second[j]
        sorted_array.append(item)
    else: 
        item = first[i]
        sorted_array.append(item)
    return sorted_array

