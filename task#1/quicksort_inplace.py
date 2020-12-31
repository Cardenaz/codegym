import random

def quicksort_inplace(array):

    


    
    sortedArray = []
    picker = len(array)
    pivot = random.randrange(0, len(array))
    realPivot = array[pivot]
    return realPivot


def alternative1(array):
    elements = len(array) 

    

def teacherMethod(array):
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
        
        return teacherMethod(left) + equal + teacherMethod(right)
    else: 
        return array

print(teacherMethod([1,5,3,6]))








#consider one element as pivot
#split elements -> larger values to right -- smaller to left


