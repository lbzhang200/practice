def twosumhash(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n #calculates complement 
        if comp in seen:
            return [seen[comp], 1] #returns number if in array
        seen[n] = i