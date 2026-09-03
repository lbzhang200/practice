# =============================================================================
# FINAL TEST — 20 Problems
# =============================================================================
# No hints. No category labels. No looking things up.
# This is everything you've learned — hashing, arrays, strings,
# two pointers, sliding window, stacks, binary search.
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
# Given a sorted array of integers, return the index of the target.
# Return -1 if not found. Must be O(log n).
#
# Example:
#   nums = [-1, 0, 3, 5, 9, 12], target = 9
#   Output: 4
# -----------------------------------------------------------------------------

def q2(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid 
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return - 1

# -----------------------------------------------------------------------------
# 3.
# -----------------------------------------------------------------------------
# Given a string of brackets, return true if it is valid. Every opening
# bracket must be closed by the correct type in the correct order.
#
# Example:
#   s = "{[]}"     Output: True
#   s = "([)]"     Output: False
# -----------------------------------------------------------------------------

def q3(s):
    stack = []
    keys = {'}': '{', ']':'[', ')':'('}

    for letter in s:
        if letter in '{[(':
            stack.append(letter)
        else:
            if stack or stack[-1] != keys[letter]:
                return False 
            stack.pop()
    return len(stack) == 0 

# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given an array of integers, return true if any value appears at least twice.
#
# Example:
#   nums = [1, 2, 3, 1]
#   Output: True
# -----------------------------------------------------------------------------

def q4(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
        if count[n] > 1:
            return True 
    return False 

# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return an array where result[i]
# is the number of days until a warmer temperature. Return 0 if none.
#
# Example:
#   temps = [73, 74, 75, 71, 69, 72, 76, 73]
#   Output: [1, 1, 4, 2, 1, 1, 0, 0]
# -----------------------------------------------------------------------------

def q5(temps):
    stack = []
    result = [0] * len(temps )
    for i in range(len(temps)):
        while (temps[i] > temps(stack[-1])): #stack holds the indexes 
            idx = stack.pop()
            result[idx] = i - idx #today minus that day 
        stack.append(i) #append only the index of the days 
    return result 

# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given two strings s and t, return true if t is an anagram of s.
# No Counter — write it manually.
#
# Example:
#   s = "anagram", t = "nagaram"
#   Output: True
# -----------------------------------------------------------------------------

def q6(s, t):
    if len(s) != len(t):
        return False 
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    for letter in t:
        count[letter] = count.get(letter, 0) - 1
        if count[letter] < 0:
            return False 
    return True 


# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return the index where it should
# be inserted to keep the array sorted. If found, return its index.
#
# Example:
#   nums = [1, 3, 5, 6], target = 2
#   Output: 1
# -----------------------------------------------------------------------------

def q7(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid 
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left 

# -----------------------------------------------------------------------------
# 8.
# -----------------------------------------------------------------------------
# Given a string, find the length of the longest substring with no
# repeating characters.
#
# Example:
#   s = "abcabcbb"
#   Output: 3
# -----------------------------------------------------------------------------

def q8(s):
    left = 0
    seen = set()
    maxlen = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1 
        seen.add(s[right])
        maxlen = max(maxlen, right - left + 1)
    return maxlen 
# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams together.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# -----------------------------------------------------------------------------

def q9(strs):
    count = {}
    for letter in strs:
        key = "".join(sorted(letter))
        if key not in count:
            count[key] = [] 
        count[key].append(letter)  
    return list(count.values())

# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# Given a sorted array (can include negatives), return a new sorted array
# of the squares of each element.
#
# Example:
#   nums = [-4, -1, 0, 3, 10]
#   Output: [0, 1, 9, 16, 100]
# -----------------------------------------------------------------------------

def q10(nums):
    left, right = 0, len(nums) - 1
    result = [0] * len(nums)
    top = len(nums) - 1
    while left <= right:
        if nums[left] ** 2 > nums[right] ** 2: 
            result[top] = nums[left] ** 2
            left += 1
        elif nums[left] ** 2 < nums[right] ** 2:
            result[top] = nums[right] ** 2
            right -= 1
        top -= 1
    return result 

# -----------------------------------------------------------------------------
# 11.
# -----------------------------------------------------------------------------
# Given an array of integers, return the number of subarrays that sum to k.
#
# Example:
#   nums = [1, 2, 3], k = 3
#   Output: 2
# -----------------------------------------------------------------------------

def q11(nums, k):
    prefix = 0
    count = 0
    seen = {0: 1}
    for n in nums:
        prefix += n
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count 

# -----------------------------------------------------------------------------
# 12.
# -----------------------------------------------------------------------------
# A sorted array has been rotated at an unknown pivot. Find the minimum
# element. Must be O(log n).
#
# Example:
#   nums = [3, 4, 5, 1, 2]
#   Output: 1
# -----------------------------------------------------------------------------

def q12(nums):
    left, right = 0, len(nums) - 1
    while left < right: 
        mid = (left + right) // 2
        if nums[mid] > nums[left]: 
            left = mid + 1
        else:
            right = mid 
    return nums[left] 

# -----------------------------------------------------------------------------
# 13.
# -----------------------------------------------------------------------------
# Given two strings where '#' means backspace, return true if they are
# equal after processing all backspaces.
#
# Example:
#   s = "ab#c", t = "ad#c"
#   Output: True
# -----------------------------------------------------------------------------

def q13(s, t):
    def build(word):
        stack = []
        for letter in word:
            if letter != '#':
                stack.append(letter)
            elif stack:
                stack.pop()
        return stack 
    return build(s) == build(t)


# -----------------------------------------------------------------------------
# 14.
# -----------------------------------------------------------------------------
# Given an array of integers and integer k, return the k most frequent
# elements. Use the bucket sort approach.
#
# Example:
#   nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q14(nums, k):
    count = {}
    for letter in nums:
        count[letter] = count.get(letter, 0) + 1
    buckets = [[]for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)
    
    result = []
    for freq in range(len(nums) - 1, 0, -1):
        for nums in buckets[freq]:
            result.append(nums) 
            if len(result) == k:
                return result 
# -----------------------------------------------------------------------------
# 15.
# -----------------------------------------------------------------------------
# Given an array of positive integers and a target, return the minimum
# length subarray whose sum >= target. Return 0 if none exists.
#
# Example:
#   target = 7, nums = [2, 3, 1, 2, 4, 3]
#   Output: 2
# -----------------------------------------------------------------------------

def q15(target, nums):
    window_sum = 0
    left = 0 
    minlen = float('inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            minlen = min(minlen, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if minlen == float('inf') else minlen  



# -----------------------------------------------------------------------------
# 16.
# -----------------------------------------------------------------------------
# Given an array of heights, find two lines that form a container
# holding the most water. Return the max area.
#
# Example:
#   height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
# -----------------------------------------------------------------------------

def q16(height):
     
    left, right  = 0, len(height) - 1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        maxarea = max(maxarea, area)
        if height[right] < height[left]:
            left += 1
        else:
            right -= 1
    return maxarea 

# -----------------------------------------------------------------------------
# 17.
# -----------------------------------------------------------------------------
# A sorted array has been rotated at an unknown pivot. Given a target,
# return its index or -1 if not found. Must be O(log n).
#
# Example:
#   nums = [4, 5, 6, 7, 0, 1, 2], target = 0
#   Output: 4
# -----------------------------------------------------------------------------

def q17(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid 
        if nums[left] < target:
            if nums[left] <= target < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[right] > target:
            if nums[right] >= target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
    return left   
            
#double check this one 

# -----------------------------------------------------------------------------
# 18.
# -----------------------------------------------------------------------------
# Given an array, move all zeroes to the end while maintaining relative
# order of non-zero elements. In-place.
#
# Example:
#   nums = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]
# -----------------------------------------------------------------------------

def q18(nums):
    result = [0] * len(nums)
    left = 0 
    for right in range(len(nums)):
        while nums[right] != 0:
            result[left] = nums[right] 
            left += 1 
    while right > left:
        result[left] = 0
        left += 1 

# -----------------------------------------------------------------------------
# 19.
# -----------------------------------------------------------------------------
# Given an array of integers, return an array where each element is
# the product of all other elements. No division. O(n).
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
# -----------------------------------------------------------------------------

def q19(nums):
    result = [1] * len(nums)
    for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1] 

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * suffix 
        suffix *= nums[i]
    return result  

# -----------------------------------------------------------------------------
# 20.
# -----------------------------------------------------------------------------
# Given piles of bananas and h hours, find the minimum eating speed k
# such that Koko can finish all piles within h hours.
#
# Example:
#   piles = [3, 6, 7, 11], h = 8
#   Output: 4
# -----------------------------------------------------------------------------

def q20(piles, h):
    def hours_needed(speed):
        return sum(-(-pile // speed) for pile in piles)
    
    left, right = 0, len(piles) - 1
    while left <= right:
        mid = (left + right) // 2 #looking the piles 
        if hours_needed(mid) >= h: #piles = minimum pile speed  if it works, then we look for an even smaller one 
            right = mid 
        else:
            left = mid + 1 #if not, look for a bigger one until it fits 
    return left 

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


# 1. Two Sum — HASHING (complement lookup)
def q1_answer(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


# 2. Binary Search — BINARY SEARCH (classic)
def q2_answer(nums, target):
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


# 3. Valid Parentheses — STACK (matching)
def q3_answer(s):
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


# 4. Contains Duplicate — HASHING (seen set)
def q4_answer(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# 5. Daily Temperatures — STACK (monotonic, stores indices)
def q5_answer(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


# 6. Valid Anagram — HASHING (one dict, increment/decrement)
def q6_answer(s, t):
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


# 7. Search Insert Position — BINARY SEARCH (find boundary)
def q7_answer(nums, target):
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


# 8. Longest Substring Without Repeating Characters — SLIDING WINDOW (variable)
def q8_answer(s):
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


# 9. Group Anagrams — HASHING (sorted string as key)
def q9_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# 10. Squares of a Sorted Array — TWO POINTERS (opposite ends, fill backward)
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


# 11. Subarray Sum Equals K — HASHING (prefix sum + hashmap)
def q11_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


# 12. Find Minimum in Rotated Sorted Array — BINARY SEARCH (modified)
def q12_answer(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


# 13. Backspace String Compare — STACK (simulate)
def q13_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build(s) == build(t)


# 14. Top K Frequent Elements — HASHING + BUCKET SORT
def q14_answer(nums, k):
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


# 15. Minimum Size Subarray Sum — SLIDING WINDOW (variable)
def q15_answer(target, nums):
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


# 16. Container With Most Water — TWO POINTERS (opposite ends)
def q16_answer(height):
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


# 17. Search in Rotated Sorted Array — BINARY SEARCH (modified)
def q17_answer(nums, target):
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


# 18. Move Zeroes — TWO POINTERS (slow/fast)
def q18_answer(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1


# 19. Product of Array Except Self — ARRAYS (prefix + suffix)
def q19_answer(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    return answer


# 20. Koko Eating Bananas — BINARY SEARCH (search on answer)
def q20_answer(piles, h):
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