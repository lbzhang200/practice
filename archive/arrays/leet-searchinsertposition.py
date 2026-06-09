def searchpos(self, nums, target): 

    for num in nums:
        if num != target:
            if target < num:
                count += 1
        else:
            break

    return count 
        