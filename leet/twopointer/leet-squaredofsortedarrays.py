def sortedSquares(self, nums):

    #pattern - use 2 pointers because squared means numbers on end are biggest (sorted array)
    left= 0 
    right = 0
    top = len(nums) - 1
    result = [0] * len(nums)

    while left < right:
        if nums[left] ** 2 > nums[right] ** 2:
            result[top] = nums[left] ** 2
            left += 1
        else:
            result[top] = nums[right] ** 2
            right -= 1
        top -= 1
    return result 