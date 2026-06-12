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
            return [seen[comp], i] #returns number if in array
        seen[n] = i
        

def twosumhash(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i] #i represents the second number index
        
        seen[n] = i