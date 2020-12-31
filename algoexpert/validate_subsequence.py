# O(n) time | 


def isValidSubsequence(array, subsequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(subsequence): 
        if array[arrIdx] == subsequence[seqIdx]:
            seqIdx += 1
        array += 1
    
    return seqIdx == len(subsequence) - 1 



    


    
