# =============================================================================
# DAILY PRACTICE 10 — 15 Problems
# =============================================================================
# No hints, no category labels. Figure out the pattern yourself.
# Covers: hashing, arrays, strings, two pointers, sliding window, stacks.
# Answer key at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1.
# -----------------------------------------------------------------------------
# Given an array of integers, return true if there exist two indices i and j
# such that nums[i] == nums[j] and abs(i - j) <= k.
#
# Example:
#   nums = [1,2,3,1], k = 3
#   Output: True
#
#   nums = [1,2,3,1,2,3], k = 2
#   Output: False
# -----------------------------------------------------------------------------

def q1(nums, k):
    seen = {}
    for i, n in enumerate(nums):
        if n in seen and abs(i - seen[n]) <= k:
            return True 
        seen[n] = i 
    return False    

# -----------------------------------------------------------------------------
# 2.
# -----------------------------------------------------------------------------
# Given a string, return true if it is a palindrome after removing
# non-alphanumeric characters and lowercasing.
#
# Example:
#   s = "race a car"
#   Output: False
#
#   s = "Never odd or even"
#   Output: True
# -----------------------------------------------------------------------------

def q2(s):
    left, right = 0, len(s) - 1
    while left < right:
        while s[left] != s[right] and not s[left].alpha():
            left += 1
        while s[left] != s[right] and not s[right].islpha():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False 
        left += 1 
        right -= 1 
    return True  

# -----------------------------------------------------------------------------
# 3.
# -----------------------------------------------------------------------------
# Given an array of integers, find all unique triplets that sum to zero.
#
# Example:
#   nums = [-1,0,1,2,-1,-4]
#   Output: [[-1,-1,2],[-1,0,1]]
# -----------------------------------------------------------------------------

def q3(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue 
        if nums[i] > 0:
            break
        left, right = i+1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append(nums[i], nums[left], nums[right])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            else: 
                if total < 0: #if too small, make smaller number bigger  
                    left += 1
                else:
                    right -= 1 # if too big, make bigger number smaller 
    return result 

# -----------------------------------------------------------------------------
# 4.
# -----------------------------------------------------------------------------
# Given an array of prices where prices[i] is the stock price on day i,
# return the maximum profit from one buy and one sell. You must buy
# before you sell. Return 0 if no profit is possible.
#
# Example:
#   prices = [7,1,5,3,6,4]
#   Output: 5
#
#   prices = [7,6,4,3,1]
#   Output: 0
# -----------------------------------------------------------------------------

def q4(prices):
     #dont have to use two pointers 

    maxprofit = 0 
    minprice = float('inf')

    for price in prices:
        minprice = min(minprice, price)
        maxprice = max(maxprice, price - minprice)

    return maxprofit 
# -----------------------------------------------------------------------------
# 5.
# -----------------------------------------------------------------------------
# Given a string, return all start indices of anagrams of p found in s.
#
# Example:
#   s = "cbaebabacd", p = "abc"
#   Output: [0, 6]
# -----------------------------------------------------------------------------

def q5(s, p):
    pass


# -----------------------------------------------------------------------------
# 6.
# -----------------------------------------------------------------------------
# Given a sorted array, remove duplicates in place and return the count
# of unique elements.
#
# Example:
#   nums = [1,1,1,2,2,3,3,3]
#   Output: 3   (nums becomes [1,2,3,...])
# -----------------------------------------------------------------------------

def q6(nums):
    pass


# -----------------------------------------------------------------------------
# 7.
# -----------------------------------------------------------------------------
# Given an array of integers, return the number of subarrays that sum to k.
#
# Example:
#   nums = [1,2,1,2,1], k = 3
#   Output: 4
# -----------------------------------------------------------------------------

def q7(nums, k):
    pass


# -----------------------------------------------------------------------------
# 8.
# -----------------------------------------------------------------------------
# Given a string where '#' means backspace, and another string where '#'
# means backspace, return true if they are equal after processing.
#
# Example:
#   s = "xywrrmp", t = "xywrrmu#p"
#   Output: True
# -----------------------------------------------------------------------------

def q8(s, t):
    pass


# -----------------------------------------------------------------------------
# 9.
# -----------------------------------------------------------------------------
# Given an array of heights, find two lines that form a container that
# holds the most water. Return the max area.
#
# Example:
#   height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
# -----------------------------------------------------------------------------

def q9(height):
    pass


# -----------------------------------------------------------------------------
# 10.
# -----------------------------------------------------------------------------
# Given a string, find the index of the first non-repeating character.
# Return -1 if none exists.
#
# Example:
#   s = "aadadaad"
#   Output: -1
#
#   s = "abcab"
#   Output: 2   ('c' is first unique)
# -----------------------------------------------------------------------------

def q10(s):
    pass


# -----------------------------------------------------------------------------
# 11.
# -----------------------------------------------------------------------------
# Given a binary array and k, return the max consecutive 1s after
# flipping at most k zeros.
#
# Example:
#   nums = [0,0,1,1,1,0,0], k = 0
#   Output: 3
#
#   nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
#   Output: 10
# -----------------------------------------------------------------------------

def q11(nums, k):
    pass


# -----------------------------------------------------------------------------
# 12.
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return how many days until a
# warmer temperature for each day. Return 0 if no warmer day exists.
#
# Example:
#   temps = [30,40,50,60]
#   Output: [1,1,1,0]
#
#   temps = [30,60,90]
#   Output: [1,1,0]
# -----------------------------------------------------------------------------

def q12(temps):
    pass


# -----------------------------------------------------------------------------
# 13.
# -----------------------------------------------------------------------------
# Given two integer arrays, return their intersection where each element
# in the result appears only once.
#
# Example:
#   nums1 = [1,2,2,1], nums2 = [2,2]
#   Output: [2]
#
#   nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#   Output: [9,4]
# -----------------------------------------------------------------------------

def q13(nums1, nums2):
    pass


# -----------------------------------------------------------------------------
# 14.
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return the 1-indexed positions of
# the two numbers that sum to target. Use O(1) extra space.
#
# Example:
#   numbers = [2,3,4], target = 6
#   Output: [1,3]
# -----------------------------------------------------------------------------

def q14(numbers, target):
    pass


# -----------------------------------------------------------------------------
# 15.
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams together.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# -----------------------------------------------------------------------------

def q15(strs):
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


# 1. Contains Duplicate II — HASHING (last seen index dict)
# store last seen index. when duplicate found, check gap <= k.
# always update to most recent index.
# Time: O(n) | Space: O(n)

def q1_answer(nums, k):
    seen = {}
    for i, n in enumerate(nums):
        if n in seen and i - seen[n] <= k:
            return True
        seen[n] = i
    return False


# 2. Valid Palindrome — TWO POINTERS (opposite ends)
# skip non-alphanumeric from both ends. compare lowercased.
# Time: O(n) | Space: O(1)

def q2_answer(s):
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


# 3. 3Sum — TWO POINTERS (sort + fix one + opposite ends on rest)
# sort first. fix nums[i], two pointer rest for pairs summing to -nums[i].
# skip duplicates to avoid duplicate triplets.
# Time: O(n^2) | Space: O(n)

def q3_answer(nums):
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


# 4. Best Time to Buy and Sell Stock — ARRAYS (single pass, track min)
# track min price seen so far. profit = current price - min price.
# Time: O(n) | Space: O(1)

def q4_answer(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


# 5. Find All Anagrams in a String — SLIDING WINDOW (fixed)
# fixed window of size len(p). maintain freq dict. compare to p_count.
# Time: O(n) | Space: O(1)

def q5_answer(s, p):
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


# 6. Remove Duplicates from Sorted Array — TWO POINTERS (slow/fast)
# slow tracks last unique written. increment slow BEFORE writing.
# Time: O(n) | Space: O(1)

def q6_answer(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


# 7. Subarray Sum Equals K — HASHING (prefix sum + hashmap)
# prefix tracks running total. {0:1} handles subarrays from index 0.
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


# 8. Backspace String Compare — STACK (simulate)
# push chars, pop on '#', guard empty stack. compare final stacks.
# Time: O(n) | Space: O(n)

def q8_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack
    return build(s) == build(t)


# 9. Container With Most Water — TWO POINTERS (opposite ends)
# always move shorter pointer inward. track max area.
# Time: O(n) | Space: O(1)

def q9_answer(height):
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


# 10. First Unique Character — HASHING (frequency count, two pass)
# pass 1: count frequencies. pass 2: first index with count == 1.
# Time: O(n) | Space: O(1)

def q10_answer(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


# 11. Max Consecutive Ones III — SLIDING WINDOW (variable)
# track zero_count. shrink when exceeds k. only decrement on actual zero.
# Time: O(n) | Space: O(1)

def q11_answer(nums, k):
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


# 12. Daily Temperatures — STACK (monotonic, stores indices)
# stack holds waiting indices. pop when current temp beats stack top.
# record distance i - idx for each popped index.
# Time: O(n) | Space: O(n)

def q12_answer(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


# 13. Intersection of Two Arrays — HASHING (set intersection)
# convert both to sets, & gives common elements.
# Time: O(n + m) | Space: O(n + m)

def q13_answer(nums1, nums2):
    return list(set(nums1) & set(nums2))


# 14. Two Sum II — TWO POINTERS (opposite ends, sorted array)
# sum too small → left+=1. sum too big → right-=1. return 1-indexed.
# Time: O(n) | Space: O(1)

def q14_answer(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1


# 15. Group Anagrams — HASHING (sorted string as key)
# sorted word is canonical key. group under that key.
# Time: O(n * k log k) | Space: O(n * k)

def q15_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())