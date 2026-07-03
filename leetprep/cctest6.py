# =============================================================================
# DAILY PRACTICE 11 — 15 Problems
# =============================================================================
# No hints, no category labels. Figure out the pattern yourself.
# Covers everything: hashing, arrays, strings, two pointers,
# sliding window, stacks, binary search.
# Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# Given a sorted array of integers, return the index of the target.
# If not found, return -1. Must be O(log n).
#
# Example:
#   nums = [-1, 0, 3, 5, 9, 12], target = 9
#   Output: 4
#
#   nums = [-1, 0, 3, 5, 9, 12], target = 2
#   Output: -1
# -----------------------------------------------------------------------------

def q1(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        result = nums[mid]
        if result == target:
            return mid 
        elif result < target:
            right = mid - 1
        else:
            left = mid + 1
    return -1 


# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given a string of brackets, return true if it is valid. Every opening
# bracket must be closed by the same type in the correct order.
#
# Example:
#   s = "{[]}"     Output: True
#   s = "([)]"     Output: False
# -----------------------------------------------------------------------------

def q2(s):
    stack = []
    values = {')': '(', '}': '{', ']': '['}

    for letter in s:
        if stack and letter in '{[(':
            stack.append(letter)
        else:
            if not stack or stack[-1] != values[letter]:
                return False 
            stack.pop()
    return len(stack) == 0 #all stacks should be appended and popped 
             
# -----------------------------------------------------------------------------
# 3.
# -----------------------------------------------------------------------------
# Given an array of integers and a target, return indices of the two
# numbers that sum to target.
#
# Example:
#   nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
# -----------------------------------------------------------------------------

def q3(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i
 
# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return the index where it should
# be inserted to keep the array sorted.
#
# Example:
#   nums = [1, 3, 5, 6], target = 2
#   Output: 1
#
#   nums = [1, 3, 5, 6], target = 7
#   Output: 4
# -----------------------------------------------------------------------------

def q4(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right: 
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid -  1
    return left  

# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return an array where result[i]
# is how many days until a warmer temperature. Return 0 if none exists.
#
# Example:
#   temps = [73, 74, 75, 71, 69, 72, 76, 73]
#   Output: [1, 1, 4, 2, 1, 1, 0, 0]
# -----------------------------------------------------------------------------

def q5(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > stack[-1]: #found a warmer day
            idx = stack.pop()
            result[idx] = i - idx #today - day that needed warmer day 
        stack.append(temps[i])
    return result  

# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given a string, find the length of the longest substring with no
# repeating characters.
#
# Example:
#   s = "pwwkew"
#   Output: 3
# -----------------------------------------------------------------------------

def q6(s):
    seen = set()
    left = 0
    maxlen = 0
    for right in range(len(s)):
        while s[right] in seen: #if catches duplicate 
            seen.remove(s[left]) #remove the duplicate 
            left += 1
        seen.add(s[right]) #append the new one in hopes of a higher maxlen
        maxlen = max(maxlen, right - left + 1)
    return maxlen  
         
# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# A sorted array has been rotated at an unknown pivot. Find the minimum
# element. Must be O(log n).
#
# Example:
#   nums = [3, 4, 5, 1, 2]
#   Output: 1
#
#   nums = [4, 5, 6, 7, 0, 1, 2]
#   Output: 0
# -----------------------------------------------------------------------------

def q7(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[left]: #larger numbers on left, smaller on right 
            left = mid + 1
        else:
            right = mid 
    return nums[left] 

# -----------------------------------------------------------------------------
# 8.
# -----------------------------------------------------------------------------
# Given an array of integers, return the number of subarrays that sum to k.
#
# Example:
#   nums = [1, 2, 3], k = 3
#   Output: 2
# -----------------------------------------------------------------------------

def q8(nums, k):
    seen = {0: 1}
    prefix = 0 
    for num in nums:
        prefix += num
        count += seen.get(k - prefix, 0)
        seen[prefix ] = seen.get(prefix, 0) + 1 
    return count 


# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given two strings where '#' means backspace, return true if they are
# equal after processing all backspaces.
#
# Example:
#   s = "ab#c", t = "ad#c"
#   Output: True
# -----------------------------------------------------------------------------

def q9(s, t):
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
# 10.
# -----------------------------------------------------------------------------
# Given an array of integers, move all zeroes to the end while keeping
# relative order of non-zero elements. In-place.
#
# Example:
#   nums = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]
# -----------------------------------------------------------------------------

def q10(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[slow] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1
    while slow < fast:
        nums[slow] = 0
        slow += 1  

# -----------------------------------------------------------------------------
# 11.
# -----------------------------------------------------------------------------
# Given a sorted array that has been rotated at an unknown pivot and a
# target value, return the index of the target or -1 if not found.
# Must be O(log n).
#
# Example:
#   nums = [4, 5, 6, 7, 0, 1, 2], target = 0
#   Output: 4
#
#   nums = [4, 5, 6, 7, 0, 1, 2], target = 3
#   Output: -1
# -----------------------------------------------------------------------------

def q11(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid 
        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: 
            if nums[right] >= target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
      #run through this one 

# -----------------------------------------------------------------------------
# 12.
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams together.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# -----------------------------------------------------------------------------

def q12(strs):
    seen = set()
    for letter in strs:
        key = "".join(sorted(letter))
        seen[key] = seen.get(key, []) + letter
    return list(seen.values())

# -----------------------------------------------------------------------------
# 13.
# -----------------------------------------------------------------------------
# Given an array of positive integers and a target sum, find the minimum
# length subarray whose sum is >= target. Return 0 if none exists.
#
# Example:
#   target = 7, nums = [2, 3, 1, 2, 4, 3]
#   Output: 2
# -----------------------------------------------------------------------------

def q13(target, nums):
    window_sum = 0
    left = 0
    minlen = 0
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            minlen = min(minlen, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return minlen  


# -----------------------------------------------------------------------------
# 14.
# -----------------------------------------------------------------------------
# Given a sorted array (can include negatives), return a sorted array
# of the squares of each element.
#
# Example:
#   nums = [-4, -1, 0, 3, 10]
#   Output: [0, 1, 9, 16, 100]
# -----------------------------------------------------------------------------

def q14(nums):
    left, right = 0, len(nums) - 1
    top = len(nums) - 1
    result = [0] * len(nums)
    while left < right:
        if nums[left] ** 2 > nums[right] ** 2:
            result[top] = nums[left] ** 2
            left += 1
        elif nums[left] ** 2< nums[right] ** 2:
            result[top] = nums[right] ** 2
            right -= 1
        top -= 1
    return result 

# -----------------------------------------------------------------------------
# 15.
# -----------------------------------------------------------------------------
# Koko has piles of bananas and h hours to eat them. Each hour she picks
# a pile and eats up to k bananas from it. Find the minimum integer k
# such that she can finish all piles within h hours.
#
# Example:
#   piles = [3, 6, 7, 11], h = 8
#   Output: 4
# -----------------------------------------------------------------------------

def q15(piles, h):
    #idk 


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


# 1. Binary Search — BINARY SEARCH (classic)
# narrow search space by half each step. left <= right to catch single element.
# Time: O(log n) | Space: O(1)

def q1_answer(nums, target):
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


# 3. Two Sum — HASHING (complement lookup)
# complement = target - n. store index. return on hit.
# Time: O(n) | Space: O(n)

def q3_answer(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


# 4. Search Insert Position — BINARY SEARCH (find boundary)
# same as classic but return left when not found.
# left naturally lands at the correct insertion point.
# Time: O(log n) | Space: O(1)

def q4_answer(nums, target):
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


# 5. Daily Temperatures — STACK (monotonic, stores indices)
# stack holds indices waiting for warmer day.
# pop when current temp beats top. record distance i - idx.
# Time: O(n) | Space: O(n)

def q5_answer(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


# 6. Longest Substring Without Repeating Characters — SLIDING WINDOW (variable)
# seen set tracks current window chars. shrink left on duplicate.
# Time: O(n) | Space: O(n)

def q6_answer(s):
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


# 7. Find Minimum in Rotated Sorted Array — BINARY SEARCH (modified)
# compare nums[mid] to nums[right]. if mid > right, min is in right half.
# else min is at mid or left of mid — keep mid in range.
# Time: O(log n) | Space: O(1)

def q7_answer(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# 8. Subarray Sum Equals K — HASHING (prefix sum + hashmap)
# prefix tracks running total. {0:1} handles subarrays from index 0.
# Time: O(n) | Space: O(n)

def q8_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


# 9. Backspace String Compare — STACK (simulate)
# push chars, pop on '#', guard empty stack. compare final stacks.
# Time: O(n) | Space: O(n)

def q9_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build(s) == build(t)


# 10. Move Zeroes — TWO POINTERS (slow/fast)
# slow tracks write position. fast scans. fill rest with 0 after.
# Time: O(n) | Space: O(1)

def q10_answer(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1


# 11. Search in Rotated Sorted Array — BINARY SEARCH (modified)
# one half is always sorted. check if target is in sorted half.
# if yes search there, if no search other half.
# Time: O(log n) | Space: O(1)

def q11_answer(nums, target):
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


# 12. Group Anagrams — HASHING (sorted string as key)
# sorted word is canonical key. group under that key.
# Time: O(n * k log k) | Space: O(n * k)

def q12_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# 13. Minimum Size Subarray Sum — SLIDING WINDOW (variable)
# expand right, add to sum. when sum >= target, record size and shrink.
# Time: O(n) | Space: O(1)

def q13_answer(target, nums):
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


# 14. Squares of a Sorted Array — TWO POINTERS (opposite ends)
# biggest squares at extremes. compare both ends, fill result backward.
# Time: O(n) | Space: O(n)

def q14_answer(nums):
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


# 15. Koko Eating Bananas — BINARY SEARCH (search on answer)
# binary search over possible speeds 1 to max(piles).
# for each speed, calculate hours needed using ceiling division.
# find minimum speed where hours needed <= h.
# Time: O(n log m) | Space: O(1)

def q15_answer(piles, h):
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