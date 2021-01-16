def mergesort(array):
    midpoint = len(array)// 2 
    left = array[:midpoint]
    right = array[midpoint:]


    mergesort(left)
    mergesort(right)

    


    
    

    