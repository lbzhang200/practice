# =============================================================================
# DAILY PRACTICE 14 — 15 Problems
# =============================================================================
# No hints. No category labels. Figure out the pattern yourself.
# Covers everything: hashing, arrays, strings, two pointers,
# sliding window, stacks, binary search.
# Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# Given an integer array, return true if any value appears at least twice.
#
# Example:
#   nums = [1, 2, 3, 1]
#   Output: True
# -----------------------------------------------------------------------------

def q1(nums):
    seen = {}
    for n in nums:
        if n in seen:
            return True 
        seen.add(n)
    return False 


# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given a string of brackets, return true if it is valid.
#
# Example:
#   s = "()[]{}"   Output: True
#   s = "(]"       Output: False
# -----------------------------------------------------------------------------

def q2(s):
    stack = []
    keys = {'}': '{', ')': '(', ']':'['}
    for letter in s:
        if letter in '{[(':
            stack.append(letter)
        else:
            if not stack or stack[-1] != keys[letter]: #if the stack has expired(popped too much) or not equal to its complement 
                return False  
        stack.pop()
    return True 

# -----------------------------------------------------------------------------
# 3.
# -----------------------------------------------------------------------------
# Given two strings s and t, return true if t is an anagram of s.
# No Counter — write it manually. Include a length check.
#
# Example:
#   s = "rat", t = "car"
#   Output: False
# -----------------------------------------------------------------------------

def q3(s, t):
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    for letter in t:
        count[letter] = count.get(letter, 0) - 1
        if count[letter] < 0:
            return False 
    return True 
        


# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given a sorted array of integers, return the index of target.
# Return -1 if not found. O(log n).
#
# Example:
#   nums = [-1, 0, 3, 5, 9, 12], target = 9
#   Output: 4
# -----------------------------------------------------------------------------

def q4(nums, target):
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

# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return how many days until a
# warmer temperature. Return 0 if none. Store indices in the stack.
#
# Example:
#   temps = [73, 74, 75, 71, 69, 72, 76, 73]
#   Output: [1, 1, 4, 2, 1, 1, 0, 0]
# -----------------------------------------------------------------------------

def q5(temps):
    stack = []
    result = []
    for i in range(temps):
        while temps[i] > temps[stack[i]]: #stack contains the indexes of the weathers 
            idx = stack.pop() #index of that weather day
            result[idx] = i - idx #today minus that day 
        stack.append(i)
    return result   
# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return the index where it should be
# inserted to keep sorted order. Return its index if found.
#
# Example:
#   nums = [1, 3, 5, 6], target = 2
#   Output: 1
# -----------------------------------------------------------------------------

def q6(nums, target):
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

# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given a string, find the length of the longest substring with no
# repeating characters. Use a set for the window.
#
# Example:
#   s = "abcabcbb"
#   Output: 3
# -----------------------------------------------------------------------------

def q7(s): #sliding window problem 
    seen = set()
    maxlen = 0
    left = 0 
    for right in range(len(s)):
        while s[right] in seen: #if there is a duplicate 
            seen.remove[left] #remove the left hand side 
            left += 1
        seen.appeaddd(s[right]) #append the right always to get rid of duplicates 
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
    for word in strs:
        keys = "".join(sorted(word))
        if keys not in groups:
            groups[keys] = []  
        groups[keys].append(word)
    return groups 

# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given an array of integers, return the number of subarrays that sum to k.
# Initialize seen = {0: 1} and use prefix - k for the lookup.
#
# Example:
#   nums = [1, 2, 3], k = 3
#   Output: 2
# -----------------------------------------------------------------------------

def q9(nums, k):
    seen = {0: 1}
    count = 0 
    for right in range(len(nums)):
        prefix += nums[right]
        count = seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count 


# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# A sorted array has been rotated at an unknown pivot. Find the minimum
# element. Compare nums[mid] to nums[right]. O(log n).
#
# Example:
#   nums = [3, 4, 5, 1, 2]
#   Output: 1
# -----------------------------------------------------------------------------

def q10(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < nums[left]:
            left = mid + 1
        else:
            right = mid 
    return nums[left]   


# -----------------------------------------------------------------------------
# 11.
# -----------------------------------------------------------------------------
# Given a sorted array (can include negatives), return a sorted array
# of squares. Build the result array backward using two pointers.
#
# Example:
#   nums = [-4, -1, 0, 3, 10]
#   Output: [0, 1, 9, 16, 100]
# -----------------------------------------------------------------------------

def q11(nums):
    left, right = 0, len(nums) - 1
    top = len(nums) - 1
    result = []
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
# 12.
# -----------------------------------------------------------------------------
# Given two strings where '#' means backspace, return true if they are
# equal. Guard the pop with elif stack.
#
# Example:
#   s = "ab#c", t = "ad#c"
#   Output: True
# -----------------------------------------------------------------------------

def q12(s, t):
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
# 13.
# -----------------------------------------------------------------------------
# Given an array of integers and integer k, return the k most frequent
# elements. Use frequency dict + bucket sort.
#
# Example:
#   nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q13(nums, k):
    count = {}
    for letter in nums:
        count[letter] = count.get(letter, 0) + 1
    buckets = [[]for _ in range(len(nums) + 1)]
    for num, freq in range(count.items()):
        buckets[freq] = num
        result = []
    for i in range(len(nums) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result 
# -----------------------------------------------------------------------------
# 14.
# -----------------------------------------------------------------------------
# Given an array of positive integers and a target, return the minimum
# length subarray whose sum >= target. Return 0 if none.
# Initialize min_len = float('inf').
#
# Example:
#   target = 7, nums = [2, 3, 1, 2, 4, 3]
#   Output: 2
# -----------------------------------------------------------------------------

def q14(target, nums):
    minlen = float('inf')
    windowsum = 9 
    for right in range(len(nums)):
        windowsum += nums[right]
        while windowsum >= target:
            minlen = min(minlen, right - left + 1)
            windowsum -= nums[left]
            left += 1 
    return minlen  

# -----------------------------------------------------------------------------
# 15.
# -----------------------------------------------------------------------------
# Given piles of bananas and h hours, find the minimum eating speed k
# such that Koko can finish all piles within h hours.
# Search over speeds 1 to max(piles). Use while left < right.
#
# Example:
#   piles = [3, 6, 7, 11], h = 8
#   Output: 4
# -----------------------------------------------------------------------------

def q15(piles, h):
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


# 1. Contains Duplicate — HASHING (seen set)
# check before adding. short circuit on first duplicate.
# Time: O(n) | Space: O(n)

def q1_answer(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# 2. Valid Parentheses — STACK (matching)
# push openers. on closer, check if not stack OR top doesn't match → False.
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


# 3. Valid Anagram — HASHING (one dict, increment/decrement)
# length check first. increment for s, decrement for t.
# return False when count goes negative.
# Time: O(n) | Space: O(1)

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


# 4. Binary Search — BINARY SEARCH (classic)
# narrow search space by half. return mid on hit. return -1 when not found.
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
    return -1


# 5. Daily Temperatures — STACK (monotonic, stores INDICES)
# result starts as [0] * len(temps). stack stores indices.
# pop when current temp beats stack top. record i - idx.
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


# 6. Search Insert Position — BINARY SEARCH (find boundary)
# same as classic but return left when not found.
# left naturally lands at correct insertion point.
# Time: O(log n) | Space: O(1)

def q6_answer(nums, target):
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


# 7. Longest Substring Without Repeating Characters — SLIDING WINDOW (variable)
# seen is a SET not dict. expand right. shrink left on duplicate.
# update max_len AFTER the while loop, outside it.
# Time: O(n) | Space: O(n)

def q7_answer(s):
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


# 8. Group Anagrams — HASHING (sorted string as key)
# sorted word is canonical key. use if key not in groups + append.
# Time: O(n * k log k) | Space: O(n * k)

def q8_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# 9. Subarray Sum Equals K — HASHING (prefix sum + hashmap)
# seen = {0: 1}. lookup is prefix - k NOT k - prefix.
# add prefix to seen AFTER the lookup.
# Time: O(n) | Space: O(n)

def q9_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


# 10. Find Minimum in Rotated Sorted Array — BINARY SEARCH (modified)
# while left < right (not <=). compare nums[mid] to nums[right].
# if mid > right → left = mid + 1. else → right = mid (keep mid in range).
# return nums[left].
# Time: O(log n) | Space: O(1)

def q10_answer(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# 11. Squares of a Sorted Array — TWO POINTERS (opposite ends, fill backward)
# result = [0] * len(nums). use left <= right (not <) to catch all elements.
# compare squares from both ends, fill result from top downward.
# Time: O(n) | Space: O(n)

def q11_answer(nums):
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


# 12. Backspace String Compare — STACK (simulate)
# push chars. elif stack: pop on '#' — guards against empty stack crash.
# compare final stacks.
# Time: O(n) | Space: O(n)

def q12_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build(s) == build(t)


# 13. Top K Frequent Elements — HASHING + BUCKET SORT
# buckets = [[] for _ in range(len(nums) + 1)].
# buckets[freq].append(num) — not assignment.
# scan range(len(buckets) - 1, 0, -1) not range(len(nums) - 1, ...).
# Time: O(n) | Space: O(n)

def q13_answer(nums, k):
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


# 14. Minimum Size Subarray Sum — SLIDING WINDOW (variable)
# min_len = float('inf') not 0. track minimum not maximum.
# return 0 if min_len == float('inf') else min_len.
# Time: O(n) | Space: O(1)

def q14_answer(target, nums):
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


# 15. Koko Eating Bananas — BINARY SEARCH (search on answer)
# left=1, right=max(piles) — searching SPEEDS not indices.
# while left < right. hours_needed uses ceiling division.
# right = mid when works, left = mid + 1 when too slow. return left.
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