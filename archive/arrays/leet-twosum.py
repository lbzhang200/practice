def twosum(nums, target):

    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
            
def twosumhash(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n 
        if comp in seen:
            return [seen[comp], 1] #returns number if in array
        seen[n] = i
        

def twosum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
            

def twosumhash(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[comp], 1]
        seen[n] = i