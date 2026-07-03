# =============================================================================
# DAILY PRACTICE 12 — 10 Problems
# =============================================================================
# No hints, no category labels. Figure out the pattern yourself.
# Covers everything: hashing, arrays, strings, two pointers,
# sliding window, stacks, binary search.
# Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# You have n versions [1, 2, ..., n]. Starting from some version, all
# following versions are bad. Given isBadVersion(version) which returns
# True if the version is bad, find the first bad version using as few
# calls as possible.
#
# Example:
#   n = 5, first_bad = 4
#   Output: 4
# -----------------------------------------------------------------------------

def q1(n, first_bad):
    def isBadVersion(version):
        return version >= first_bad
    left, right = 0 , n 
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid 
        else:
            left = mid + 1  
    return left 


# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given an integer array, return true if any value appears at least twice.
#
# Example:
#   nums = [1, 2, 3, 1]
#   Output: True
#
#   nums = [1, 2, 3, 4]
#   Output: False
# -----------------------------------------------------------------------------

def q2(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True  
        seen.add(n)
    return False   


# -----------------------------------------------------------------------------
# 3.
# -----------------------------------------------------------------------------
# Given an array of integers and integer k, return the k most frequent
# elements.
#
# Example:
#   nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q3(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1 
    buckets =[[]for _ in range(len(nums + 1))]

    for num, freq in count:
        buckets[freq] = num #higher frequency means higher num

    result = []
    for freq in range(len(nums) -1, -1, -1):
        for num in buckets[freq]:
            result.append(num)
            while len(result) == k:
                return result

# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given an array of heights, find two lines forming a container that
# holds the most water. Return the max area.
#
# Example:
#   height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
# -----------------------------------------------------------------------------

def q4(height): 
    left, right = 0, len(height) - 1
    area = float('inf')
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        maxarea = max(maxarea, area)
        while height[left] < height[right]:
            left += 1
        else:
            right -= 1 
    return maxarea  

# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given a sorted array that has been rotated at an unknown pivot,
# find the minimum element. Must be O(log n).
#
# Example:
#   nums = [3, 4, 5, 1, 2]
#   Output: 1
# -----------------------------------------------------------------------------

def q5(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            right = mid 
        else:
            left = mid + 1
    return left 

# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given an array of integers, return an array where each element is the
# product of all other elements. No division. Must be O(n).
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
# -----------------------------------------------------------------------------

def q6(nums):
    subfix = 1
    result = [1]* len(nums)

    for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1 ]
    
    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * subfix
        subfix = subfix * nums[i]
    return result  


# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given a binary array and integer k, return the maximum number of
# consecutive 1s if you can flip at most k zeros.
#
# Example:
#   nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#   Output: 6
# -----------------------------------------------------------------------------

def q7(nums, k):
    left = 0
    zerocount = 0 
    maxlen = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            zerocount += 1
        while zerocount > k:
            if nums[left] == 0:
                zerocount -= 1
            left += 1 
        maxlen = max(maxlen, right - left + 1)
    return maxlen  



# -----------------------------------------------------------------------------
# 8.
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams together.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# -----------------------------------------------------------------------------

def q8(strs):
    groups = {}
    for letter in strs:
        key = "".join(sorted(letter))
        groups[key] = groups.get(key, []) + letter 
    return list(groups.values)


# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given a string of brackets containing '(', ')', '{', '}', '[', ']',
# return true if the input string is valid.
#
# Example:
#   s = "()[]{}"   Output: True
#   s = "(]"       Output: False
# -----------------------------------------------------------------------------

def q9(s):
    stack = []
    keys = {'}':'{', ']':'[ ', ')': '('}
    for letter in s:
        if letter in '{[(':
            stack.append(letter)
        else:
            if stack and stack[-1] != keys[letter]: #if its a backwards, is the next in the stack equal to its complmement 
                return False 
            stack.pop() 
    return len(stack) == 0 

# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# Given a sorted array (can include negatives), return a sorted array
# of the squares of each element.
#
# Example:
#   nums = [-7, -3, 2, 3, 11]
#   Output: [4, 9, 9, 49, 121]
# -----------------------------------------------------------------------------

def q10(nums):
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    top = len(nums) - 1
    while left < right:
        if nums[left] ** 2 > nums[right] ** 2:
            result[top] = nums[left] ** 2
            left += 1
        elif nums[left] ** 2 < nums[right] ** 2:
            result[top] = nums[right] ** 2
            right -= 1
        top -= 1
    return result   


# =============================================================================
#
#
#
#   ANSWER KEY
#
#
#
# =============================================================================
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# =============================================================================
# ANSWER KEY
# =============================================================================


# 1. First Bad Version — BINARY SEARCH (find boundary)
# when isBadVersion(mid) is True, answer is mid or earlier — right = mid.
# when False, answer is after mid — left = mid + 1.
# left == right at the end, pointing to first bad version.
# Time: O(log n) | Space: O(1)

def q1_answer(n, first_bad):
    def isBadVersion(version):
        return version >= first_bad

    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left


# 2. Contains Duplicate — HASHING (seen set)
# check before adding. short circuit on first duplicate.
# Time: O(n) | Space: O(n)

def q2_answer(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# 3. Top K Frequent Elements — HASHING + BUCKET SORT
# frequency dict → buckets by freq → scan right to left for top k.
# Time: O(n) | Space: O(n)

def q3_answer(nums, k):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result


# 4. Container With Most Water — TWO POINTERS (opposite ends)
# always move shorter pointer inward. track max area.
# Time: O(n) | Space: O(1)

def q4_answer(height):
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


# 5. Find Minimum in Rotated Sorted Array — BINARY SEARCH (modified)
# compare nums[mid] to nums[right]. if mid > right, min is in right half.
# else min is at mid or left — keep mid in range with right = mid.
# Time: O(log n) | Space: O(1)

def q5_answer(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# 6. Product of Array Except Self — ARRAYS (prefix + suffix pass)
# left pass fills prefix products. right pass multiplies by running suffix.
# Time: O(n) | Space: O(1) excluding output

def q6_answer(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    return answer


# 7. Max Consecutive Ones III — SLIDING WINDOW (variable)
# track zero_count. shrink when zero_count > k.
# only decrement zero_count when actual zero leaves window.
# Time: O(n) | Space: O(1)

def q7_answer(nums, k):
    left = 0
    zero_count = 0
    max_len = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# 8. Group Anagrams — HASHING (sorted string as key)
# sorted word is canonical key for all anagrams in a group.
# Time: O(n * k log k) | Space: O(n * k)

def q8_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# 9. Valid Parentheses — STACK (matching)
# push openers. on closer, check top matches. pop if yes, False if no.
# stack must be empty at end.
# Time: O(n) | Space: O(n)

def q9_answer(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return len(stack) == 0


# 10. Squares of a Sorted Array — TWO POINTERS (opposite ends)
# biggest squares at extremes. compare both ends, fill result backward.
# Time: O(n) | Space: O(n)

def q10_answer(nums):
    left, right = 0, len(nums) - 1
    top = len(nums) - 1
    result = [0] * len(nums)
    while left <= right:
        if nums[left] ** 2 > nums[right] ** 2:
            result[top] = nums[left] ** 2
            left += 1
        else:
            result[top] = nums[right] ** 2
            right -= 1
        top -= 1
    return result