# =============================================================================
# BIG TEST — 50 Problems
# =============================================================================
# No hints. No category labels. No looking things up.
# Covers everything: hashing, arrays, strings, two pointers,
# sliding window, stacks, binary search.
# Time yourself. Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# Given an integer array and a target, return indices of the two numbers
# that add up to the target.
#
# Example:
#   nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
# -----------------------------------------------------------------------------

def q1(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n 
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i 

    
# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given an integer array, return true if any value appears at least twice.
#
# Example:
#   nums = [1, 2, 3, 1]
#   Output: True
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
# Given two strings s and t, return true if t is an anagram of s.
#
# Example:
#   s = "anagram", t = "nagaram"
#   Output: True
# -----------------------------------------------------------------------------

def q3(s, t):
    if len(s) != len(t):
        return False 
    seen = {}
    for letter in s:
        seen[letter] = seen.get(letter, 0) + 1

    for letter in t:
        seen[letter] = seen.get(letter, 0) - 1
        if seen[letter] < 0:
            return False 
    return True 

# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given a string, return true if it is a palindrome ignoring
# non-alphanumeric characters and case.
#
# Example:
#   s = "A man, a plan, a canal: Panama"
#   Output: True
# -----------------------------------------------------------------------------

def q4(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False 
        left += 1
        right -= 1 
    return True 

# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given two strings ransomNote and magazine, return true if ransomNote
# can be built from letters in magazine.
#
# Example:
#   ransomNote = "aa", magazine = "aab"
#   Output: True
# -----------------------------------------------------------------------------

def q5(ransomNote, magazine):
    seen = {}
    for letter in magazine:
        seen[letter] = seen.get(letter, 0) + 1

    for letter in ransomNote:
        seen[letter] = seen.get(letter, 0) - 1
        if seen[letter] < 0:
            return False 
    return True 

    

# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams together.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# -----------------------------------------------------------------------------

def q6(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = [] 
        groups[key].append(word)
    return list(groups.values())
    
# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given an integer array and integer k, return the k most frequent elements.
#
# Example:
#   nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q7(nums, k):
    count = {}
    result = {}
    for letter in nums:
        count[letter] = count.get(letter, 0) + 1
    buckets = [[]for _ in range(len(nums) + 1)] #makes array 
    #count frequency using backwards method 
    
    for num, freq in count.items():
        buckets[freq].append(num) #most frequency towards back

    for freq in range(len(buckets) - 1, 0, -1): #count from backwards 
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result 
            
# -----------------------------------------------------------------------------
# 8.
# -----------------------------------------------------------------------------
# Given an array, return an array where each element is the product of
# all others. No division. O(n).
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
# -----------------------------------------------------------------------------

def q8(nums):
    answer = [1] * len(nums)
    for i in range(1, len(nums)):
        answer[i] = answer[i-1] * answer[i]
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] = answer[i] * suffix 
        suffix = suffix * nums[i] 
    return answer 

# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given an array of integers, return the number of subarrays that sum to k.
#
# Example:
#   nums = [1, 2, 3], k = 3
#   Output: 2
# -----------------------------------------------------------------------------

def q9(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num 
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1 #if seen prefix 
    return count 
    
# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# Given two arrays, return their intersection. Each element must be unique.
#
# Example:
#   nums1 = [1, 2, 2, 1], nums2 = [2, 2]
#   Output: [2]
# -----------------------------------------------------------------------------

def q10(nums1, nums2):
    return list(set(nums1) & set(nums2))

# -----------------------------------------------------------------------------
# 11.
# -----------------------------------------------------------------------------
# Given a string, return the index of the first non-repeating character.
# Return -1 if none.
#
# Example:
#   s = "leetcode"
#   Output: 0
# -----------------------------------------------------------------------------

def q11(s):
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1 

# -----------------------------------------------------------------------------
# 12.
# -----------------------------------------------------------------------------
# Given an array, return the element that appears more than n // 2 times.
#
# Example:
#   nums = [3, 2, 3]
#   Output: 3
# -----------------------------------------------------------------------------

def q12(nums):
    count = {}
    for letter in nums:
        count[letter] = count.get(letter, 0) + 1
    return max(count, key=count.get)

# -----------------------------------------------------------------------------
# 13.
# -----------------------------------------------------------------------------
# Given an unsorted array, return the length of the longest consecutive
# sequence. Must be O(n).
#
# Example:
#   nums = [100, 4, 200, 1, 3, 2]
#   Output: 4
# -----------------------------------------------------------------------------

def q13(nums): 
    nums_set = set(nums)
    best = 0
    for n in nums_set:
        if (n-1) not in nums_set:
            length = 1 
            while (n + length) in nums_set:
                length += 1
            best = max(best, length)
    return best 

# -----------------------------------------------------------------------------
# 14.
# -----------------------------------------------------------------------------
# Check if there exist i != j such that arr[i] == 2 * arr[j].
#
# Example:
#   arr = [10, 2, 5, 3]
#   Output: True
# -----------------------------------------------------------------------------

def q14(arr):
    seen = set()
    for n in arr:
        if 2 * n in seen or (n % 2 == 0 and n // 2 in seen): #checks both ways 
            return True 
        seen.add(n)
    return False 


# -----------------------------------------------------------------------------
# 15.
# -----------------------------------------------------------------------------
# Determine if s and t are isomorphic.
#
# Example:
#   s = "egg", t = "add"
#   Output: True
# -----------------------------------------------------------------------------

def q15(s, t):
    s_to_t, t_to_s = {}, {}
    for sc, tc, in zip(s, t):
        if sc in s_to_t and s_to_t[sc] != tc:
            return False 
        if tc in t_to_s and t_to_s[tc] != sc: 
            return False 
        s_to_t[sc] = tc
        t_to_s[tc] = sc 

    return True 

# -----------------------------------------------------------------------------
# 16.
# -----------------------------------------------------------------------------
# Given a sorted array, remove duplicates in place. Return count of uniques.
#
# Example:
#   nums = [1, 1, 2, 2, 3]
#   Output: 3
# -----------------------------------------------------------------------------

def q16(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]: 
            slow += 1
            nums[slow] = nums[fast] 
    return slow + 1 
    

# -----------------------------------------------------------------------------
# 17.
# -----------------------------------------------------------------------------
# Move all zeroes to the end while keeping relative order. In-place.
#
# Example:
#   nums = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]
# -----------------------------------------------------------------------------

def q17(nums):
    slow = 0 
    for fast in range(len(nums)):
        if nums[fast] != 0: 
            nums[slow] = nums[fast] 
    while slow < fast:
        nums[slow] = 0
        slow += 1 

# -----------------------------------------------------------------------------
# 18.
# -----------------------------------------------------------------------------
# Given a sorted array and target, return 1-indexed positions of the
# two numbers that sum to target. O(1) space.
#
# Example:
#   numbers = [2, 7, 11, 15], target = 9
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q18(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -=1 

# -----------------------------------------------------------------------------
# 19.
# -----------------------------------------------------------------------------
# Given a sorted array (can include negatives), return sorted squares.
#
# Example:
#   nums = [-4, -1, 0, 3, 10]
#   Output: [0, 1, 9, 16, 100]
# -----------------------------------------------------------------------------

def q19(nums):
    left, right = 0, len(nums) - 1
    idx = len(nums) - 1
    sorted = []
    while left < right:
        if nums[left] ** 2 > nums[right] ** 2:
            sorted[idx] = nums[left] ** 2 
            left += 1
        else:
            sorted[idx] = nums[right] ** 2 
            right -= 1
        idx -= 1
    return sorted  


# -----------------------------------------------------------------------------
# 20.
# -----------------------------------------------------------------------------
# Given an array of heights, find two lines forming a container that
# holds the most water. Return the max area.
#
# Example:
#   height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
# -----------------------------------------------------------------------------

def q20(height):
    pass


# -----------------------------------------------------------------------------
# 21.
# -----------------------------------------------------------------------------
# Merge nums2 into nums1 in place. nums1 has extra space at the end.
#
# Example:
#   nums1 = [1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
#   Output: [1,2,2,3,5,6]
# -----------------------------------------------------------------------------

def q21(nums1, m, nums2, n):
    pass


# -----------------------------------------------------------------------------
# 22.
# -----------------------------------------------------------------------------
# Given an array of integers, find all unique triplets that sum to zero.
#
# Example:
#   nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1,-1,2],[-1,0,1]]
# -----------------------------------------------------------------------------

def q22(nums):
    pass


# -----------------------------------------------------------------------------
# 23.
# -----------------------------------------------------------------------------
# Given strings s and t, return true if s is a subsequence of t.
#
# Example:
#   s = "abc", t = "ahbgdc"
#   Output: True
# -----------------------------------------------------------------------------

def q23(s, t):
    pass


# -----------------------------------------------------------------------------
# 24.
# -----------------------------------------------------------------------------
# Given a string, find the length of the longest substring with no
# repeating characters.
#
# Example:
#   s = "pwwkew"
#   Output: 3
# -----------------------------------------------------------------------------

def q24(s):
    pass


# -----------------------------------------------------------------------------
# 25.
# -----------------------------------------------------------------------------
# Given an array of integers and integer k, find the contiguous subarray
# of length k with the maximum average.
#
# Example:
#   nums = [1,12,-5,-6,50,3], k = 4
#   Output: 12.75
# -----------------------------------------------------------------------------

def q25(nums, k):
    pass


# -----------------------------------------------------------------------------
# 26.
# -----------------------------------------------------------------------------
# Given a binary array and k, return the max consecutive 1s after
# flipping at most k zeros.
#
# Example:
#   nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#   Output: 6
# -----------------------------------------------------------------------------

def q26(nums, k):
    pass


# -----------------------------------------------------------------------------
# 27.
# -----------------------------------------------------------------------------
# Given an array of positive integers and a target, return the minimum
# length subarray whose sum >= target. Return 0 if none.
#
# Example:
#   target = 7, nums = [2,3,1,2,4,3]
#   Output: 2
# -----------------------------------------------------------------------------

def q27(target, nums):
    pass


# -----------------------------------------------------------------------------
# 28.
# -----------------------------------------------------------------------------
# Return all start indices of p's anagrams in s.
#
# Example:
#   s = "cbaebabacd", p = "abc"
#   Output: [0, 6]
# -----------------------------------------------------------------------------

def q28(s, p):
    pass


# -----------------------------------------------------------------------------
# 29.
# -----------------------------------------------------------------------------
# Given a string of brackets, return true if it is valid.
#
# Example:
#   s = "{[]}"     Output: True
#   s = "([)]"     Output: False
# -----------------------------------------------------------------------------

def q29(s):
    pass


# -----------------------------------------------------------------------------
# 30.
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return how many days until a
# warmer temperature. Return 0 if none.
#
# Example:
#   temps = [73,74,75,71,69,72,76,73]
#   Output: [1,1,4,2,1,1,0,0]
# -----------------------------------------------------------------------------

def q30(temps):
    stack = [] #stack holds the indexes for the greater weather 
    result = []
    for i in range(len(temps)):
        while (temps[right] > temps[stack[-1]]):
            idx = stack.pop()
            result[idx] = i - idx 
        stack.append(i)
    return result 

# -----------------------------------------------------------------------------
# 31.
# -----------------------------------------------------------------------------
# Given two strings where '#' means backspace, return true if equal
# after processing.
#
# Example:
#   s = "ab#c", t = "ad#c"
#   Output: True
# -----------------------------------------------------------------------------

def q31(s, t):
    pass


# -----------------------------------------------------------------------------
# 32.
# -----------------------------------------------------------------------------
# Given a sorted array of integers, return the index of target.
# Return -1 if not found. O(log n).
#
# Example:
#   nums = [-1, 0, 3, 5, 9, 12], target = 9
#   Output: 4
# -----------------------------------------------------------------------------

def q32(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid 
        if nums[mid] < target:
            right = mid - 1
        else:
            left = mid + 1
        return left 
        


# -----------------------------------------------------------------------------
# 33.
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return the index where it should
# be inserted to keep sorted order.
#
# Example:
#   nums = [1,3,5,6], target = 2
#   Output: 1
# -----------------------------------------------------------------------------

def q33(nums, target):
    pass


# -----------------------------------------------------------------------------
# 34.
# -----------------------------------------------------------------------------
# A sorted array has been rotated. Find the minimum element. O(log n).
#
# Example:
#   nums = [3,4,5,1,2]
#   Output: 1
# -----------------------------------------------------------------------------

def q34(nums):
    pass


# -----------------------------------------------------------------------------
# 35.
# -----------------------------------------------------------------------------
# A sorted array has been rotated. Find the target. Return -1 if not found.
# O(log n).
#
# Example:
#   nums = [4,5,6,7,0,1,2], target = 0
#   Output: 4
# -----------------------------------------------------------------------------

def q35(nums, target):
    pass


# -----------------------------------------------------------------------------
# 36.
# -----------------------------------------------------------------------------
# Given piles of bananas and h hours, find the minimum eating speed k.
#
# Example:
#   piles = [3,6,7,11], h = 8
#   Output: 4
# -----------------------------------------------------------------------------

def q36(piles, h):
    pass


# -----------------------------------------------------------------------------
# 37.
# -----------------------------------------------------------------------------
# Find the first bad version given isBadVersion(). Use as few calls as possible.
#
# Example:
#   n = 5, first_bad = 4
#   Output: 4
# -----------------------------------------------------------------------------

def q37(n, first_bad):
    def isBadVersion(v):
        return v >= first_bad
    pass


# -----------------------------------------------------------------------------
# 38.
# -----------------------------------------------------------------------------
# Given an array of integers and integer k, return true if there are
# two indices i and j such that nums[i] == nums[j] and abs(i-j) <= k.
#
# Example:
#   nums = [1,2,3,1], k = 3
#   Output: True
# -----------------------------------------------------------------------------

def q38(nums, k):
    pass


# -----------------------------------------------------------------------------
# 39.
# -----------------------------------------------------------------------------
# Given an array of prices, return the maximum profit. Buy before selling.
#
# Example:
#   prices = [7,1,5,3,6,4]
#   Output: 5
# -----------------------------------------------------------------------------

def q39(prices):
    maxprofit = 0 
    minprice = float('inf')
    for price in prices:
        minprice = min(minprice, price)
        maxprofit = max(maxprofit, price - minprice)
    return maxprofit 


# -----------------------------------------------------------------------------
# 40.
# -----------------------------------------------------------------------------
# Given a string of brackets, return true if valid. (Write it again.)
#
# Example:
#   s = "()[]{}"   Output: True
# -----------------------------------------------------------------------------

def q40(s):
    pass


# -----------------------------------------------------------------------------
# 41.
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return days until warmer.
# (Write it again — remember to store indices in the stack.)
#
# Example:
#   temps = [30,40,50,60]
#   Output: [1,1,1,0]
# -----------------------------------------------------------------------------

def q41(temps):
    pass


# -----------------------------------------------------------------------------
# 42.
# -----------------------------------------------------------------------------
# Given two strings where '#' means backspace, return true if equal.
# (Write it again — remember elif stack guard.)
#
# Example:
#   s = "ab##", t = "c#d#"
#   Output: True
# -----------------------------------------------------------------------------

def q42(s, t):
    def build(word):
        stack = []
        for letter in word:
            if letter != '#':
                stack.append(letter)
            else:
                stack.pop()
        return stack
    return build(s) == build(t)
    


# -----------------------------------------------------------------------------
# 43.
# -----------------------------------------------------------------------------
# Given a sorted array of integers, return the index of target.
# Return -1 if not found. (Write it again.)
#
# Example:
#   nums = [1, 3, 5, 7, 9], target = 7
#   Output: 3
# -----------------------------------------------------------------------------

def q43(nums, target):
    pass


# -----------------------------------------------------------------------------
# 44.
# -----------------------------------------------------------------------------
# Find the minimum in a rotated sorted array. (Write it again.)
#
# Example:
#   nums = [4,5,6,7,0,1,2]
#   Output: 0
# -----------------------------------------------------------------------------

def q44(nums):
    pass


# -----------------------------------------------------------------------------
# 45.
# -----------------------------------------------------------------------------
# Given a string, find length of longest substring without repeating chars.
# (Write it again — use a set, update max_len after the while loop.)
#
# Example:
#   s = "dvdf"
#   Output: 3
# -----------------------------------------------------------------------------

def q45(s):
    pass


# -----------------------------------------------------------------------------
# 46.
# -----------------------------------------------------------------------------
# Given an array of integers, return the number of subarrays summing to k.
# (Write it again — seen = {0:1}, lookup is prefix - k.)
#
# Example:
#   nums = [1,1,1], k = 2
#   Output: 2
# -----------------------------------------------------------------------------

def q46(nums, k):
    pass


# -----------------------------------------------------------------------------
# 47.
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams. (Write it again.)
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# -----------------------------------------------------------------------------

def q47(strs):
    pass


# -----------------------------------------------------------------------------
# 48.
# -----------------------------------------------------------------------------
# Given piles of bananas and h hours, find minimum eating speed.
# (Write it again — left=1, right=max(piles), while left < right.)
#
# Example:
#   piles = [3,6,7,11], h = 8
#   Output: 4
# -----------------------------------------------------------------------------

def q48(piles, h):
    pass


# -----------------------------------------------------------------------------
# 49.
# -----------------------------------------------------------------------------
# Given a sorted array and target, return 1-indexed positions of two
# numbers summing to target. (Write it again.)
#
# Example:
#   numbers = [2,3,4], target = 6
#   Output: [1,3]
# -----------------------------------------------------------------------------

def q49(numbers, target):
    pass


# -----------------------------------------------------------------------------
# 50.
# -----------------------------------------------------------------------------
# Given an array of integers, return an array where each element is the
# product of all others. (Write it again — prefix pass then suffix pass.)
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
# -----------------------------------------------------------------------------

def q50(nums):
    pass


# =============================================================================
#
#
#
#   ANSWER KEY — only scroll after attempting every single problem
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


def q1_answer(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

def q2_answer(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def q3_answer(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True

def q4_answer(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def q5_answer(ransomNote, magazine):
    count = {}
    for c in magazine:
        count[c] = count.get(c, 0) + 1
    for c in ransomNote:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True

def q6_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

def q7_answer(nums, k):
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
 
def q8_answer(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    return answer

def q9_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count

def q10_answer(nums1, nums2):
    return list(set(nums1) & set(nums2))

def q11_answer(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1

def q12_answer(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return max(count, key=count.get)

def q13_answer(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            best = max(best, length)
    return best

def q14_answer(arr):
    seen = set()
    for n in arr:
        if 2 * n in seen or (n % 2 == 0 and n // 2 in seen):
            return True
        seen.add(n)
    return False

def q15_answer(s, t):
    s_to_t, t_to_s = {}, {}
    for sc, tc in zip(s, t):
        if sc in s_to_t and s_to_t[sc] != tc:
            return False
        if tc in t_to_s and t_to_s[tc] != sc:
            return False
        s_to_t[sc] = tc
        t_to_s[tc] = sc
    return True

def q16_answer(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1

def q17_answer(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1

def q18_answer(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1

def q19_answer(nums):
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

def q20_answer(height):
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

def q21_answer(nums1, m, nums2, n):
    p1, p2, p = m - 1, n - 1, m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

def q22_answer(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        if nums[i] > 0:
            break
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

def q23_answer(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

def q24_answer(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

def q25_answer(nums, k):
    window_sum = sum(nums[:k])
    max_avg = window_sum / k
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        max_avg = max(max_avg, window_sum / k)
    return max_avg

def q26_answer(nums, k):
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

def q27_answer(target, nums):
    left = 0
    window_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len

def q28_answer(s, p):
    if len(p) > len(s):
        return []
    p_count = {}
    window = {}
    for c in p:
        p_count[c] = p_count.get(c, 0) + 1
    result = []
    for i in range(len(s)):
        window[s[i]] = window.get(s[i], 0) + 1
        if i >= len(p):
            left_char = s[i - len(p)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
        if window == p_count:
            result.append(i - len(p) + 1)
    return result

def q29_answer(s):
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

def q30_answer(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

def q31_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build(s) == build(t)

def q32_answer(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def q33_answer(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def q34_answer(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

def q35_answer(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def q36_answer(piles, h):
    def hours_needed(speed):
        return sum(-(-pile // speed) for pile in piles)
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= h:
            right = mid
        else:
            left = mid + 1
    return left

def q37_answer(n, first_bad):
    def isBadVersion(v):
        return v >= first_bad
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

def q38_answer(nums, k):
    seen = {}
    for i, n in enumerate(nums):
        if n in seen and i - seen[n] <= k:
            return True
        seen[n] = i
    return False

def q39_answer(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

def q40_answer(s):
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

def q41_answer(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result

def q42_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build(s) == build(t)

def q43_answer(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def q44_answer(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

def q45_answer(s):
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

def q46_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count

def q47_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

def q48_answer(piles, h):
    def hours_needed(speed):
        return sum(-(-pile // speed) for pile in piles)
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= h:
            right = mid
        else:
            left = mid + 1
    return left

def q49_answer(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1

def q50_answer(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    return answer