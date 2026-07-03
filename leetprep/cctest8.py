# =============================================================================
# DAILY PRACTICE 13 — 15 Problems
# =============================================================================
# No hints, no category labels. Figure out the pattern yourself.
# Covers: hashing, arrays, strings, two pointers,
# sliding window, stacks, binary search.
# Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# Given a string, return true if it is a palindrome ignoring
# non-alphanumeric characters and case.
#
# Example:
#   s = "A man, a plan, a canal: Panama"
#   Output: True
# -----------------------------------------------------------------------------

def q1(s):
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].islanum():
            right -= 1 
        if s[left].lower() != s[right].lower():
            return False 
        left += 1
        right -= 1
    return True          

# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return its index. If not found,
# return the index where it would be inserted to maintain sorted order.
#
# Example:
#   nums = [1, 3, 5, 6], target = 2
#   Output: 1
# -----------------------------------------------------------------------------

def q2(nums, target):
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
# 3.
# -----------------------------------------------------------------------------
# Given an array of integers, return the number of subarrays summing to k.
#
# Example:
#   nums = [1, 1, 1], k = 2
#   Output: 2
# -----------------------------------------------------------------------------

def q3(nums, k):
    prefix = 0 
    count = 0
    seen = {0: 1}
    for n in nums: 
        prefix += n
        count += seen.get(prefix - k , 0) #finds comp? 
        seen[prefix] = seen.get(prefix, 0) + 1 #gives the count of prefix  
    return count 
# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return how many days until a
# warmer temperature for each day. Return 0 if no warmer day exists.
#
# Example:
#   temps = [30, 40, 50, 60]
#   Output: [1, 1, 1, 0]
# -----------------------------------------------------------------------------

def q4(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop() #needs a greater weather 
            result[idx] = i - idx #today minus day that needs greater weather 
        stack.append(temps[i])
    return result   


# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given two strings s and t, return true if t is an anagram of s.
# Write it manually without Counter.
#
# Example:
#   s = "listen", t = "silent"
#   Output: True
# -----------------------------------------------------------------------------

def q5(s, t):
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
# 6.
# -----------------------------------------------------------------------------
# A sorted array has been rotated at an unknown pivot. Given a target,
# return its index or -1 if not found. Must be O(log n).
#
# Example:
#   nums = [4, 5, 6, 7, 0, 1, 2], target = 0
#   Output: 4
# -----------------------------------------------------------------------------

def q6(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]: #left is sorted, check if target is in between them
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[right] >= target > nums[mid]:
                left = mid + 1 
            else:
                right = mid - 1
    return -1 

# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given an array of integers, find all unique triplets that sum to zero.
#
# Example:
#   nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1, -1, 2], [-1, 0, 1]]
# -----------------------------------------------------------------------------

def q7(nums):
     nums.sort()
     result = []
     for i in range(len(nums)):
         if i > 0 and nums[i] == nums[i - 1]:
            continue 
         if nums[i] > 0: 
             break 
         
         left, right = i + 1, len(nums) - 1
         while left < right:
             total = nums[left] + nums[right] + nums[i]
             if total == 0:
                 result.append([nums[i], nums[left], nums[right]])
                 left += 1 
                 right -= 1
                 while left < right and nums[left] == nums[left - 1]:
                    left += 1
                 while left < right and nums[right] == nums[right + 1]:
                    right -= 1
             elif total < 0:  
                 left += 1
             else:
                 right -=1 
     return result 

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
    maxlen = 0
    left = 0
    seen = set()
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
# Given an array, return the element that appears more than n // 2 times.
#
# Example:
#   nums = [3, 2, 3]
#   Output: 3
# -----------------------------------------------------------------------------

def q9(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    return max(count, key=count.get)

# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# Given a sorted array, remove duplicates in place. Return count of uniques.
#
# Example:
#   nums = [1, 1, 2, 2, 3]
#   Output: 3
# -----------------------------------------------------------------------------

def q10(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
             slow += 1
             nums[slow] = nums[fast]
    return slow + 1 


# -----------------------------------------------------------------------------
# 11.
# -----------------------------------------------------------------------------
# Given piles of bananas and h hours, find the minimum eating speed k
# such that Koko can finish all piles within h hours.
#
# Example:
#   piles = [3, 6, 7, 11], h = 8
#   Output: 4
# -----------------------------------------------------------------------------

def q11(piles, h):
    def hours_needed(speed): #gives total sum of hours 
        for pile in piles:
            return sum(-(-pile // speed)) #round down 

    left, right = 0, len(piles) - 1
    while left <= right:
        mid = (left + right) // 2
        total = hours_needed(mid) #gets total hours 
        if total <= h: #if hours is less 
            right = mid #good, but could fine even less hours 
        else:
            left = mid + 1 #not within hour frame 
    return left 

# -----------------------------------------------------------------------------
# 12.
# -----------------------------------------------------------------------------
# Given a string of brackets, return true if it is valid.
#
# Example:
#   s = "{[]}"    Output: True
#   s = "(]"      Output: False
# -----------------------------------------------------------------------------

def q12(s):
    pass

# -----------------------------------------------------------------------------
# 13.
# -----------------------------------------------------------------------------
# Given an array of integers, return an array where each element is the
# product of all others. No division. O(n).
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
# -----------------------------------------------------------------------------

def q13(nums):
    result = [1] * len(nums)
    suffix = 1 

    for i in range(1, len(nums)):
        result[i] = result[i-1] * nums[i-1]
    
    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * suffix 
        suffix = suffix * nums[i]
    return result 

# -----------------------------------------------------------------------------
# 14.
# -----------------------------------------------------------------------------
# Given an array of positive integers and a target, return the minimum
# length subarray whose sum >= target. Return 0 if none.
#
# Example:
#   target = 7, nums = [2, 3, 1, 2, 4, 3]
#   Output: 2
# -----------------------------------------------------------------------------

def q14(target, nums):
    window_sum = 0
    left = 0 
    seen = {}
    minlen = float('inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            minlen = min(minlen, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return minlen  

# -----------------------------------------------------------------------------
# 15.
# -----------------------------------------------------------------------------
# Given two strings where '#' means backspace, return true if they are
# equal after processing.
#
# Example:
#   s = "ab#c", t = "ad#c"
#   Output: True
# -----------------------------------------------------------------------------

def q15(s, t):
    def build(word):
        stack = []
        for letter in word:
            if letter != '#':
                stack.append(letter)
            else:
                stack.pop()
        return stack
    return build(s) == build(t)

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


# 1. Valid Palindrome — TWO POINTERS (opposite ends)
# skip non-alphanumeric from both ends. compare lowercased chars.
# Time: O(n) | Space: O(1)

def q1_answer(s):
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


# 2. Search Insert Position — BINARY SEARCH (find boundary)
# same as classic but return left when not found.
# Time: O(log n) | Space: O(1)

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
    return left


# 3. Subarray Sum Equals K — HASHING (prefix sum + hashmap)
# prefix tracks running total. {0:1} handles subarrays from index 0.
# Time: O(n) | Space: O(n)

def q3_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


# 4. Daily Temperatures — STACK (monotonic, stores indices)
# stack holds indices waiting for warmer day.
# pop when current temp beats top. record distance i - idx.
# Time: O(n) | Space: O(n)

def q4_answer(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


# 5. Valid Anagram — HASHING (one dict, increment/decrement)
# length check first. increment for s, decrement for t.
# Time: O(n) | Space: O(1)

def q5_answer(s, t):
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


# 6. Search in Rotated Sorted Array — BINARY SEARCH (modified)
# one half always sorted. check if target in sorted half.
# if yes search there, if no search other half.
# Time: O(log n) | Space: O(1)

def q6_answer(nums, target):
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


# 7. 3Sum — TWO POINTERS (sort + fix + opposite ends)
# sort first. fix nums[i], two pointer rest for sum == -nums[i].
# skip duplicates at both levels to avoid duplicate triplets.
# Time: O(n^2) | Space: O(n)

def q7_answer(nums):
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


# 8. Longest Substring Without Repeating Characters — SLIDING WINDOW (variable)
# seen set tracks current window. shrink left on duplicate. track max len.
# Time: O(n) | Space: O(n)

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


# 9. Majority Element — HASHING (frequency count, max value)
# count frequencies. return key with highest count.
# Time: O(n) | Space: O(n)

def q9_answer(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return max(count, key=count.get)


# 10. Remove Duplicates from Sorted Array — TWO POINTERS (slow/fast)
# slow tracks last unique written. increment slow BEFORE writing.
# Time: O(n) | Space: O(1)

def q10_answer(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


# 11. Koko Eating Bananas — BINARY SEARCH (search on answer)
# binary search over speeds 1 to max(piles).
# ceiling division to calculate hours needed at each speed.
# find minimum speed where hours <= h.
# Time: O(n log m) | Space: O(1)

def q11_answer(piles, h):
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


# 12. Valid Parentheses — STACK (matching)
# push openers. on closer, check top matches. pop if yes, False if no.
# stack must be empty at end.
# Time: O(n) | Space: O(n)

def q12_answer(s):
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


# 13. Product of Array Except Self — ARRAYS (prefix + suffix)
# left pass fills prefix products. suffix pass multiplies running suffix.
# Time: O(n) | Space: O(1) excluding output

def q13_answer(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    return answer


# 14. Minimum Size Subarray Sum — SLIDING WINDOW (variable)
# expand right, add to sum. when sum >= target, record and shrink left.
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


# 15. Backspace String Compare — STACK (simulate)
# push chars, pop on '#', guard empty stack. compare final stacks.
# Time: O(n) | Space: O(n)

def q15_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build(s) == build(t)