#given an array nums and integer k, returns true if there ar etwo distinct indices i and j where num[i] == num[j] and abs(i-j) <= k

def containsduplicate(self, nums, k):

    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap:
            if (i - hashmap[num] <= k):
                return True 
        hashmap[num] = i
    return False 

