# =============================================================================
# DAILY PRACTICE 9 — 15 Problems
# =============================================================================
# No hints, no category labels. Figure out the pattern yourself.
# Covers: hashing, arrays, strings, two pointers, sliding window, stacks.
# Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# Given an integer array, return an array where each element is the
# product of all other elements. No division allowed. Must be O(n).
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
# -----------------------------------------------------------------------------

def q1(nums):
    result = [1] * len(nums)
    n = len(nums)
    subfix = 1 

    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]

    for i in range(len(nums) - 2, -1, -1):
        result[i] = result[i+1] * subfix 
        subfix *= nums[i]
    return result 



# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given a string of brackets containing '(', ')', '{', '}', '[', ']',
# return true if the string is valid. Every opener must be closed by
# the same type in the correct order.
#
# Example:
#   s = "()[]{}"   Output: True
#   s = "([)]"     Output: False
#   s = "{[]}"     Output: True
# -----------------------------------------------------------------------------

def q2(s):
    pass


# -----------------------------------------------------------------------------
# 3.
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return an array where result[i]
# is the number of days you have to wait for a warmer temperature.
# If no warmer day exists, result[i] = 0.
#
# Example:
#   temps = [73,74,75,71,69,72,76,73]
#   Output: [1,1,4,2,1,1,0,0]
# -----------------------------------------------------------------------------

def q3(temps):
    pass


# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given a string, find the length of the longest substring with no
# repeating characters.
#
# Example:
#   s = "dvdf"
#   Output: 3   ("vdf")
# -----------------------------------------------------------------------------

def q4(s):
    pass


# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given two strings where '#' represents a backspace character, return
# true if they are equal after processing all backspaces.
#
# Example:
#   s = "ab#c", t = "ad#c"
#   Output: True   ("ac" == "ac")
#
#   s = "a##c", t = "#a#c"
#   Output: True   ("c" == "c")
# -----------------------------------------------------------------------------

def q5(s, t):
    pass


# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given an unsorted array, return the length of the longest consecutive
# sequence. Must run in O(n).
#
# Example:
#   nums = [9,1,4,7,3,-1,0,5,8,-1,6]
#   Output: 7   (sequence -1 to 5 or 3 to 9)
# -----------------------------------------------------------------------------

def q6(nums):
    pass


# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given a sorted array (may include negatives), return a sorted array
# of the squares of each number.
#
# Example:
#   nums = [-5,-3,-1,0,2,4]
#   Output: [0,1,4,9,16,25]  (wait - recheck: [0,1,4,9,16,25])
# -----------------------------------------------------------------------------

def q7(nums):
    pass


# -----------------------------------------------------------------------------
# 8.
# -----------------------------------------------------------------------------
# Given an array of positive integers and a target, find the minimum
# length subarray whose sum is >= target. Return 0 if none exists.
#
# Example:
#   target = 11, nums = [1,1,1,1,1,1,1,1]
#   Output: 0   (impossible, total sum = 8 < 11)
#
#   target = 7, nums = [2,3,1,2,4,3]
#   Output: 2
# -----------------------------------------------------------------------------

def q8(target, nums):
    pass


# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given an integer array and integer k, return the k most frequent elements.
#
# Example:
#   nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q9(nums, k):
    pass


# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# Given a binary array and integer k, return the maximum number of
# consecutive 1s if you can flip at most k zeros.
#
# Example:
#   nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#   Output: 6
# -----------------------------------------------------------------------------

def q10(nums, k):
    pass


# -----------------------------------------------------------------------------
# 11.
# -----------------------------------------------------------------------------
# Given an array of integers, move all zeroes to the end while
# maintaining relative order of non-zero elements. In-place.
#
# Example:
#   nums = [0,1,0,3,12]
#   Output: [1,3,12,0,0]
# -----------------------------------------------------------------------------

def q11(nums):
    pass


# -----------------------------------------------------------------------------
# 12.
# -----------------------------------------------------------------------------
# Given two strings s and t, return true if t is an anagram of s.
# Write it manually — no Counter.
#
# Example:
#   s = "triangle", t = "integral"
#   Output: True
# -----------------------------------------------------------------------------

def q12(s, t):
    pass


# -----------------------------------------------------------------------------
# 13.
# -----------------------------------------------------------------------------
# Given an array of integers and a target, return indices of the two
# numbers that sum to target.
#
# Example:
#   nums = [3,3], target = 6
#   Output: [0,1]
# -----------------------------------------------------------------------------

def q13(nums, target):
    pass


# -----------------------------------------------------------------------------
# 14.
# -----------------------------------------------------------------------------
# Given two strings s and t where '#' is backspace, return true if equal
# after processing. This time write a helper function to process each string,
# then compare the results.
#
# Wait — this is the same as problem 5. Try this instead:
#
# Given strings s and t, return true if s is a subsequence of t.
#
# Example:
#   s = "abc", t = "ahbgdc"
#   Output: True
#
#   s = "axc", t = "ahbgdc"
#   Output: False
# -----------------------------------------------------------------------------

def q14(s, t):
    pass


# -----------------------------------------------------------------------------
# 15.
# -----------------------------------------------------------------------------
# Given an array and integer k, find the contiguous subarray of length k
# with the maximum average. Return that average value.
#
# Example:
#   nums = [0,1,1,3,3], k = 4
#   Output: 2.0   (subarray [1,1,3,3], avg = 8/4 = 2.0)
# -----------------------------------------------------------------------------

def q15(nums, k):
    pass


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


# 1. Product of Array Except Self — ARRAYS (prefix + suffix pass)
# left pass fills prefix products, right pass multiplies by suffix.
# Time: O(n) | Space: O(1) excluding output

def q1_answer(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    return answer


# 2. Valid Parentheses — STACK (matching)
# push openers. on closer, check top matches. pop if yes, False if no.
# stack must be empty at end.
# Time: O(n) | Space: O(n)

def q2_answer(s):
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


# 3. Daily Temperatures — STACK (monotonic, stores indices)
# stack holds indices of days waiting for warmer temp.
# when current temp beats stack top, pop and record distance i - idx.
# Time: O(n) | Space: O(n)

def q3_answer(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


# 4. Longest Substring Without Repeating Characters — SLIDING WINDOW (variable)
# seen set tracks current window. shrink left on duplicate. track max len.
# Time: O(n) | Space: O(n)

def q4_answer(s):
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


# 5. Backspace String Compare — STACK (simulate)
# push chars, pop on '#', guard empty stack. compare final stacks.
# Time: O(n) | Space: O(n)

def q5_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build(s) == build(t)


# 6. Longest Consecutive Sequence — HASHING (set, count from starts)
# only start counting when n-1 not in set. walk forward while chain holds.
# Time: O(n) | Space: O(n)

def q6_answer(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if (n-1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            best = max(best, length)
    return best


# 7. Squares of a Sorted Array — TWO POINTERS (opposite ends, fill backward)
# biggest squares at extremes. compare both ends, fill result backward.
# Time: O(n) | Space: O(n)

def q7_answer(nums):
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


# 8. Minimum Size Subarray Sum — SLIDING WINDOW (variable)
# expand right, add to sum. when sum >= target, record size and shrink.
# Time: O(n) | Space: O(1)

def q8_answer(target, nums):
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


# 9. Top K Frequent Elements — HASHING + BUCKET SORT
# frequency dict → buckets by freq → scan right to left for top k.
# Time: O(n) | Space: O(n)

def q9_answer(nums, k):
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


# 10. Max Consecutive Ones III — SLIDING WINDOW (variable)
# track zero_count. shrink when zero_count > k.
# only decrement zero_count when actual zero leaves the window.
# Time: O(n) | Space: O(1)

def q10_answer(nums, k):
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


# 11. Move Zeroes — TWO POINTERS (slow/fast)
# slow tracks write position. fast scans. fill rest with 0 after.
# Time: O(n) | Space: O(1)

def q11_answer(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1


# 12. Valid Anagram — HASHING (one dict, increment/decrement)
# length check first. increment for s, decrement for t.
# Time: O(n) | Space: O(1)

def q12_answer(s, t):
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


# 13. Two Sum — HASHING (complement lookup)
# complement = target - n. store index. return on hit.
# Time: O(n) | Space: O(n)

def q13_answer(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


# 14. Is Subsequence — TWO POINTERS (same direction)
# i tracks s, j tracks t. j always advances. i only on match.
# if i reaches len(s), all chars found in order.
# Time: O(len(t)) | Space: O(1)

def q14_answer(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# 15. Maximum Average Subarray — SLIDING WINDOW (fixed)
# seed first window of size k, then slide adding new removing old.
# Time: O(n) | Space: O(1)

def q15_answer(nums, k):
    window_sum = sum(nums[:k])
    max_avg = window_sum / k
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        max_avg = max(max_avg, window_sum / k)
    return max_avg