def twoSum(nums, target):
    pointers = []
    numsIdx = 0 
    numsNextIdx = 1

    while numsIdx < len(nums) -1:
        
        if nums[numsIdx] + nums[numsNextIdx] == target:
            pointers.append(numsIdx)
            pointers.append(numsNextIdx)
            numsNextIdx += 1
        else: 
            numsNextIdx +=1 

        






