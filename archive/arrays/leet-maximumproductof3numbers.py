def maxproduct(self, nums):

    n = sorted(nums)
    return max(n[-1] * n[-2] * n[-3], n[0] * n[1] * n[-1])