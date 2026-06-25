# =============================================================================
# DAILY PRACTICE 8 — 10 Problems
# =============================================================================
# No hints, no category labels. Figure out the pattern yourself.
# Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# Given a sorted array (including negatives), return a new array of the
# squares of each number, sorted in ascending order.
#
# Example:
#   nums = [-7, -3, 2, 3, 11]
#   Output: [4, 9, 9, 49, 121]
# -----------------------------------------------------------------------------

def q1(nums):
    left, right = 0, len(nums) - 1
    result = []
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

# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given two strings ransomNote and magazine, return true if ransomNote
# can be constructed using letters from magazine. Each letter in magazine
# can only be used once.
#
# Example:
#   ransomNote = "aab", magazine = "baa"
#   Output: True
#
#   ransomNote = "abc", magazine = "ab"
#   Output: False
# -----------------------------------------------------------------------------

def q2(ransomNote, magazine):
    count = {}
    for letter in magazine:
        count[letter] = count.get(letter, 0) + 1
    for letter in ransomNote:
        count[letter] = count.get(letter, 0) - 1
        if count[letter] < 0:
            return False 
    return True 

# -----------------------------------------------------------------------------
# 3.
# -----------------------------------------------------------------------------
# Given an array of integers and integer k, find the contiguous subarray
# of length k that has the maximum average value. Return that average.
#
# Example:
#   nums = [1, 12, -5, -6, 50, 3], k = 4
#   Output: 12.75
# -----------------------------------------------------------------------------

def q3(nums, k):
    sum = sum(nums[:4])
    maxavg = sum / k 
    for fast in range(k, len(nums)):
        sum += nums[fast]
        sum -= nums[fast - k]
        maxavg = max(maxavg, sum / k)
    return maxavg 

# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given two arrays, return their intersection. Each element in the
# result must appear only once.
#
# Example:
#   nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
#   Output: [9, 4]
# -----------------------------------------------------------------------------

def q4(nums1, nums2):
    return list(set(nums1) & set(nums2))


# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given a string s, find the index of the first character that does not
# repeat. Return -1 if no such character exists.
#
# Example:
#   s = "loveleetcode"
#   Output: 2   ('v' is first unique)
#
#   s = "aabb"
#   Output: -1
# -----------------------------------------------------------------------------

def q5(s):
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    for i, n in enumerate(s):
        if count[letter] == 1:
            return i
    return - 1

# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return the 1-indexed positions of
# the two numbers that add up to target. Use O(1) extra space.
#
# Example:
#   numbers = [1, 2, 3, 4, 4, 9, 56, 90], target = 8
#   Output: [4, 5]
# -----------------------------------------------------------------------------

def q6(numbers, target):
    left, right = 0, len(numbers) -1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
         
# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given an integer array, return the number of subarrays that sum to k.
#
# Example:
#   nums = [1, 1, 1], k = 2
#   Output: 2
# -----------------------------------------------------------------------------

def q7(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(k - prefix, 0)
        seen = seen.get(prefix, 0) + 1
    return count 


# -----------------------------------------------------------------------------
# 8.
# -----------------------------------------------------------------------------
# Given an array, move all zeroes to the end while maintaining the
# relative order of non-zero elements. Do it in place.
#
# Example:
#   nums = [0, 0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0, 0]
# -----------------------------------------------------------------------------

def q8(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < fast:
        nums[slow] = 0
        slow += 1

# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given strings s and t, return true if s is a subsequence of t.
# Characters of s must appear in t in the same order, not necessarily
# adjacent.
#
# Example:
#   s = "ace", t = "abcde"
#   Output: True
#
#   s = "aec", t = "abcde"
#   Output: False
# -----------------------------------------------------------------------------

def q9(s, t):
    i, j = 0, 0
    while i < len(s) and i < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1 #j always iterates 
    return i == len(s)


#always advance array t by j, but only advnace through i when find equals 
#if i made it all the way through, all characters found 
         

# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# Given an unsorted array of integers, return the length of the longest
# consecutive elements sequence. Must run in O(n).
#
# Example:
#   nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
#   Output: 9   (sequence 0-8)
# -----------------------------------------------------------------------------

def q10(nums):
    maxlength = 0
    seen = {}
    for n in nums:
        if n - 1 not in seen:
            length = 1
            while (n + length) in seen:
                length += 1 
                maxlength = max(maxlength, length)
    return maxlength 


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


# 1. Squares of a Sorted Array — TWO POINTERS (opposite ends, fill backward)
# biggest squares at extremes. compare from both ends, fill result backward.
# Time: O(n) | Space: O(n)

def q1_answer(nums):
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


# 2. Ransom Note — HASHING (frequency count, one dict)
# count up magazine chars, count down ransomNote chars.
# return False the moment any count goes negative.
# Time: O(n) | Space: O(1)

def q2_answer(ransomNote, magazine):
    count = {}
    for c in magazine:
        count[c] = count.get(c, 0) + 1
    for c in ransomNote:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True


# 3. Maximum Average Subarray — SLIDING WINDOW (fixed)
# seed first window, slide by adding new and removing outgoing element.
# Time: O(n) | Space: O(1)

def q3_answer(nums, k):
    window_sum = sum(nums[:k])
    max_avg = window_sum / k
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        max_avg = max(max_avg, window_sum / k)
    return max_avg


# 4. Intersection of Two Arrays — HASHING (set intersection)
# convert both to sets, & operator gives common elements.
# Time: O(n + m) | Space: O(n + m)

def q4_answer(nums1, nums2):
    return list(set(nums1) & set(nums2))


# 5. First Unique Character — HASHING (frequency count, two pass)
# pass 1: count all frequencies. pass 2: return first index with count == 1.
# Time: O(n) | Space: O(1)

def q5_answer(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


# 6. Two Sum II — TWO POINTERS (opposite ends, sorted array)
# sorted array lets us use position as information.
# sum too small → left+=1. sum too big → right-=1.
# Time: O(n) | Space: O(1)

def q6_answer(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1


# 7. Subarray Sum Equals K — HASHING (prefix sum + hashmap)
# prefix tracks running total. seen tracks how many times each prefix
# sum has occurred. {0:1} handles subarrays starting at index 0.
# Time: O(n) | Space: O(n)

def q7_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


# 8. Move Zeroes — TWO POINTERS (slow/fast)
# slow tracks write position for non-zeroes. fast scans everything.
# fill remaining positions with 0 after the loop.
# Time: O(n) | Space: O(1)

def q8_answer(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1


# 9. Is Subsequence — TWO POINTERS (same direction)
# i tracks s, j tracks t. j always advances. i only advances on a match.
# if i reaches len(s), all chars of s were found in order.
# Time: O(len(t)) | Space: O(1)

def q9_answer(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# 10. Longest Consecutive Sequence — HASHING (set, count from starts only)
# convert to set. only start counting when n-1 not in set.
# walk forward while chain continues, track best.
# Time: O(n) | Space: O(n)

def q10_answer(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            best = max(best, length)
    return best