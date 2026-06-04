#checks if two index of ana array can add up to the target 
def twosum(nums, target):

    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
            

