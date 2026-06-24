# =============================================================================
# DAILY PRACTICE — 10 Problems
# =============================================================================
# No hints, no category labels. Figure out the pattern yourself.
# Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# Given a string s, find the length of the longest substring that contains
# no repeating characters.
#
# Example:
#   s = "pwwkew"
#   Output: 3   ("wke")
#
#   s = "bbbbb"
#   Output: 1
# -----------------------------------------------------------------------------

def q1(s):
    seen = set()
    left = 0
    maxlength = 0 
    for right in (len(s)):
        while s[right] in seen: #if duplicate 
            seen.remove(s[left]) #shrink left until catches duplicate 
            left += 1
        seen.add(s[right])
        maxlength = max(maxlength, right - left + 1)

    return maxlength 

# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given an array of integers, return true if any value appears at least
# twice. Return false if every element is distinct.
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: False
#
#   nums = [1, 1, 2, 3]
#   Output: True
# -----------------------------------------------------------------------------

def q2(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return False 
        seen.add(n)
    return True  

# -----------------------------------------------------------------------------
# 3.
# -----------------------------------------------------------------------------
# Given a sorted array of integers, remove duplicates in place and return
# the count of unique elements.
#
# Example:
#   nums = [1, 1, 2, 2, 3]
#   Output: 3   (nums becomes [1, 2, 3, ...])
# -----------------------------------------------------------------------------

def q3(nums):
    seen = set()
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            nums[slow] = nums[fast]
            slow += 1
    return slow + 1

# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given a string, return true if it is a palindrome after removing
# non-alphanumeric characters and lowercasing everything.
#
# Example:
#   s = "Was it a car or a cat I saw?"
#   Output: True
#
#   s = "hello"
#   Output: False
# -----------------------------------------------------------------------------

def q4(s):
    left, right = 0, len(s) - 1
    while left < right:
        while s[left] != s[right] and not s[left].isalpha():
            left += 1
        while s[left] != s[right] and not s[right].isalpha():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False 
        else:
            left += 1
            right -= 1
    return True 

# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given an array of integers and a target, return the indices of the two
# numbers that add up to the target.
#
# Example:
#   nums = [3, 2, 4], target = 6
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q5(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[n], i] 
        seen[n] = i


# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given an array of positive integers and a target, return the minimum
# length of a contiguous subarray whose sum is greater than or equal to
# target. Return 0 if no such subarray exists.
#
# Example:
#   nums = [2, 3, 1, 2, 4, 3], target = 7
#   Output: 2   ([4, 3])
# -----------------------------------------------------------------------------

def q6(target, nums):

    minlength = 0
    left = 0
    sum = 0 
    for right in range(len(nums)):
        sum += nums[right]
        while sum >= target:
            minlength = min(minlength, right - left + 1)
            sum -= nums[left] #shrink until finds minimum 
            left += 1
    return minlength 

# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given two strings s and t, return true if t is an anagram of s.
#
# Example:
#   s = "cinema", t = "iceman"
#   Output: True
#
#   s = "hello", t = "world"
#   Output: False
# -----------------------------------------------------------------------------

def q7(s, t):
    count = {}
    for letter in s:
        count[letter] = count.get(s, 0) + 1
    for letter in t:
        count[letter] = count.get(s, 0) - 1
        if count < 0:
            return False 
    return True 


# -----------------------------------------------------------------------------
# 8.
# -----------------------------------------------------------------------------
# Given an array of heights representing vertical lines, find two lines
# that together form a container that holds the most water. Return the
# max area.
#
# Example:
#   height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
# -----------------------------------------------------------------------------

def q8(height):
    left, right = 0, len(height) - 1
    maxarea = 0 
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        maxarea = max(area, maxarea)
        if height[left] < height[right]:
            left += 1
        if height[right] > height[left]:
            right -= 1
         

# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given a binary array and integer k, return the maximum number of
# consecutive 1s if you can flip at most k zeros.
#
# Example:
#   nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
#   Output: 10
# -----------------------------------------------------------------------------

def q9(nums, k):
    zerocount = 0 
    left = 0 
    maxlen = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zerocount += 1
        while zerocount > k: 
            if nums[left] == 0:
                zerocount -= 1
            left += 1
        maxlen = max(maxlen, right - left + 1)
    return maxlen 



# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams together and return
# all groups.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# -----------------------------------------------------------------------------

def q10(strs):
    seen = {}
    for words in strs:
        key = "".join(sorted(words))
        seen[key] = seen.get(key, []) + words
    return list(seen.values)

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


# 1. Longest Substring Without Repeating Characters — SLIDING WINDOW (variable)
# seen set tracks current window chars. shrink left on duplicate. track max len.
# Time: O(n) | Space: O(n)

def q1_answer(s):
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


# 2. Contains Duplicate — HASHING (seen set)
# check before adding. short circuit on first hit.
# Time: O(n) | Space: O(n)

def q2_answer(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# 3. Remove Duplicates from Sorted Array — TWO POINTERS (slow/fast)
# slow tracks last unique written. increment slow BEFORE writing.
# Time: O(n) | Space: O(1)

def q3_answer(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


# 4. Valid Palindrome — TWO POINTERS (opposite ends)
# skip non-alphanumeric from both ends. compare lowercased chars.
# Time: O(n) | Space: O(1)

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


# 5. Two Sum — HASHING (complement lookup)
# complement = target - n. store indices. return on hit.
# Time: O(n) | Space: O(n)

def q5_answer(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


# 6. Minimum Size Subarray Sum — SLIDING WINDOW (variable)
# expand right, add to sum. when sum >= target, record size and shrink left.
# Time: O(n) | Space: O(1)

def q6_answer(target, nums):
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


# 7. Valid Anagram — HASHING (one dict, increment/decrement)
# length check first. increment for s, decrement for t.
# Time: O(n) | Space: O(1)

def q7_answer(s, t):
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


# 8. Container With Most Water — TWO POINTERS (opposite ends)
# area = min(heights) * width. always move the shorter pointer inward.
# Time: O(n) | Space: O(1)

def q8_answer(height):
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


# 9. Max Consecutive Ones III — SLIDING WINDOW (variable)
# track zero_count in window. shrink when zero_count > k.
# only decrement zero_count when an actual zero leaves the window.
# Time: O(n) | Space: O(1)

def q9_answer(nums, k):
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


# 10. Group Anagrams — HASHING (sorted string as key)
# sorted word is canonical key for all anagrams in a group.
# Time: O(n * k log k) | Space: O(n * k)

def q10_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())