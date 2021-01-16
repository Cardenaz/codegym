def quicksort_notinplace():

    

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

print(teacherMethod([23,12,95,17,17,34,45,96,-3]))


