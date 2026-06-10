#returns the intersection of 2 arrays

def intersection(self, nums1, nums2):

    seen = set(nums1)
    result = set()

    for n in nums2:
        if n in seen():
            result.add(n)
    

    return list(result)

#or return list(set(num1) & set(num2))