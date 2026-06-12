def maxconsecutive(self, nums): #returns the max count of consecutive one's 

    count = 0
    max = 0
    for num in nums:
        if num == 1:
            count += 1
            if count > max:
                max = count

        else:
            count = 0 
    return max 

def maxConsecutive(self, nums):

    count = 0
    max = 0
    for num in nums:
        if num == 1:
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    return max 