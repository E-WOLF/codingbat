def same_first_last(nums):
    '''
    Given an array of ints, return True if the array is length 1 or more,
    and the first element and the last element are equal
    '''
    if  len(nums) == 0:
        return False
    else:
        return nums[0] == nums[len(nums) - 1]

print(same_first_last([1,2,3])) # exp. False 
print(same_first_last([1, 2, 3, 1])) # exp. True
print(same_first_last([1, 2, 1])) # exp. True

