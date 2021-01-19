def mergesort(array,pointer,length ):
    # r must be greater than pointer 
    
    
    if (length-pointer) > 1:
        midpoint = (pointer+length)//2 
        mergesort(array, pointer, midpoint)
        mergesort(array, midpoint, pointer)
        merge(array, pointer, length, midpoint )


def merge(array, start, end, midpoint):
    i = j = 0 
    first_half = array[start:midpoint]
    second_half = array[midpoint:end]

    for z in range(start, end): 
        if j >= len(second_half) or (i < len(first_half) and first_half[i] < second_half[j]):  
            array[z] = first_half[i]
            i += 1 
        else: 
            array[z] = second_half[j]
            j += 1 
    return array
    

def mergesort_inplace(array): 

    pointer = 0
    length = len(array)  
    return mergesort(array, pointer, length)
'''
jjj = [3,6,5,4,1]
print(mergesort_inplace(jjj))
print(jjj)'''


def MERGE(A,start,mid,end):
    L = A[start:mid]
    R = A[mid:end]
    i = 0
    j = 0
    k = start
    for l in range(k,end):
        if j >= len(R) or (i < len(L) and L[i] < R[j]):
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1 
     

def mergeSort(A,p,r):
    if r - p > 1:
        mid = int((p+r)/2)
        mergeSort(A,p,mid)
        mergeSort(A,mid,r)
        MERGE(A,p,mid,r)




A  = [20, 30, 21, 15, 42, 45, 31, 0, 9]
print(mergeSort(A,0,len(A)))            # changed


    


    
    

    