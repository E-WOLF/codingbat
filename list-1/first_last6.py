def first_last6(nums):
    """
    Given an array of ints, return True if 6 appears
    as either the first or last element in the array.
    The array will be length 1 or more.
    """
    # if len(nums) == 1: 
    #     return sum(nums) == 6 

    # else:
    #     first_last = []
    #     first_last.append(nums[0])
    #     first_last.append(nums[len(nums)-1])
    return nums[0] == 6 or nums[-1] == 6


print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))


