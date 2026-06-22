# =============================================================================
# INTUITION TEST — 20 Problems, No Category Hints
# =============================================================================
# These are all problems you've solved before. No pattern labels this time —
# figure out which approach fits on your own.
# Answer key (with pattern + solution) is at the bottom.
# =============================================================================


# -----------------------------------------------------------------------------
# 1. Two Sum
# -----------------------------------------------------------------------------
# Given an array of integers and a target, return the indices of the two
# numbers that add up to the target.
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
            return [seen[n], i]
        seen[n] = i

# -----------------------------------------------------------------------------
# 2. Contains Duplicate
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
# 3. Valid Palindrome
# -----------------------------------------------------------------------------
# Return true if the string is a palindrome, ignoring non-alphanumeric
# characters and case.
#
# Example:
#   s = "A man, a plan, a canal: Panama"
#   Output: True
# -----------------------------------------------------------------------------

def q3(s):
    left, right = 0, len(s) - 1

    while left < right:
        while s[left] != s[right] and not s[left].isalpha(): 
            left += 1
        while s[left] != s[right] and not s[right].isalpha():
            right -= 1
        if s[left].islower() != s[right].islower(): 
            return False 
        else: 
            left += 1
            right -= 1
    return True 


# -----------------------------------------------------------------------------
# 4. Best Time to Buy and Sell Stock
# -----------------------------------------------------------------------------
# Given an array of prices where prices[i] is the price on day i, find the
# maximum profit from buying on one day and selling on a later day.
#
# Example:
#   prices = [7, 1, 5, 3, 6, 4]
#   Output: 5   (buy at 1, sell at 6)
# -----------------------------------------------------------------------------

def q4(prices):
    left, right = 0, len(s) - 1
    maxprofit = 0 
    minprice = float('inf')
    while left < right:
        if prices[left] < minprice:
            minprice = prices[left]
        if prices[right] - minprice > maxprofit:
            maxprofit = prices[right] - minprice 
        left += 1
        right -= 1

    return maxprofit         
        

# -----------------------------------------------------------------------------
# 5. Ransom Note
# -----------------------------------------------------------------------------
# Return true if ransomNote can be constructed using letters from magazine.
#
# Example:
#   ransomNote = "aa", magazine = "aab"
#   Output: True
# -----------------------------------------------------------------------------

def q5(ransomNote, magazine):
    count = {}
    for letter in magazine:
        count[letter] = count.get(letter, 0) + 1

    for letter in ransomNote:
        if letter in count:
            count[letter] = count.get(letter, 0) - 1
            if count[letter] < 0:
                return False 
    return True 


# -----------------------------------------------------------------------------
# 6. Group Anagrams
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams together.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
# -----------------------------------------------------------------------------

def q6(strs):
    groups = {}
    for words in strs:
        key = "".join(sorted(words))
        groups[key] = groups.get(key, []) + [words]
    return list(groups.values())


# -----------------------------------------------------------------------------
# 7. Intersection of Two Arrays
# -----------------------------------------------------------------------------
# Given two integer arrays, return their intersection. Each element in the
# result must be unique.
#
# Example:
#   nums1 = [1, 2, 2, 1], nums2 = [2, 2]
#   Output: [2]
# -----------------------------------------------------------------------------

def q7(nums1, nums2):
    return list(set(nums1) * set(nums2))


# -----------------------------------------------------------------------------
# 8. Product of Array Except Self
# -----------------------------------------------------------------------------
# Return an array where each element is the product of all elements except
# itself. No division allowed. Must be O(n).
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
# -----------------------------------------------------------------------------

def q8(nums):
    answer = [1] * len(nums)

    for i in range(1, len(nums)):
        answer[i] = answer[i-1] * nums[i-1] #multiplies by all elements to the left

    suffix = 1
    for i in range(len(nums) - 2, -1, -1): #all elements to the right 
        answer[i] = answer[i] * suffix #because rightmost element multiplies by one
        suffix = suffix * answer[i] #takes in right element 

    return answer

# -----------------------------------------------------------------------------
# 9. Isomorphic Strings
# -----------------------------------------------------------------------------
# Determine if s and t are isomorphic (one-to-one character mapping).
#
# Example:
#   s = "egg", t = "add"
#   Output: True
# -----------------------------------------------------------------------------

def q9(s, t):
    
    s_to_t = {}
    t_to_s = {}

    for schar, tchar in zip(s, t):
        if schar in s_to_t and s_to_t[schar] != tchar:
            return False 
        elif tchar in t_to_s and t_to_s[tchar] != schar:
            return False 
        s_to_t[schar] = tchar
        t_to_s[tchar] = schar         
    return True 


# -----------------------------------------------------------------------------
# 10. Check If N and Its Double Exist
# -----------------------------------------------------------------------------
# Check if there exist indices i != j such that arr[i] == 2 * arr[j].
#
# Example:
#   arr = [10, 2, 5, 3]
#   Output: True
# -----------------------------------------------------------------------------

def q10(arr):
    seen = set()
    for num in arr:
        if num * 2 in seen or (n % 2 == 0 and n // 2 in seen):
            return True 
        seen.add(num)
    return False 

# -----------------------------------------------------------------------------
# 11. Subarray Sum Equals K
# -----------------------------------------------------------------------------
# Return the number of subarrays that sum to k.
#
# Example:
#   nums = [1, 2, 3], k = 3
#   Output: 2
# -----------------------------------------------------------------------------

def q11(nums, k):
    count = 0
    prefix = 0 
    seen = {0 : 1}

    for n in nums:
        prefix += n 
        count += count.get(prefix - k, 0) #either has it or doesnt 
        seen[n] = count.get(prefix, 0) + 1 #adds current prefix for later 
    return True 

# -----------------------------------------------------------------------------
# 12. Top K Frequent Elements
# -----------------------------------------------------------------------------
# Return the k most frequent elements.
#
# Example:
#   nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q12(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    for i in range(len(nums) + 1):
        buckets = []
    for num, freq in count.items():
        buckets[freq] = num 
    
    result = []
    for freq in range(len(nums)-1, 0, -1): #iterate from most frequency 
        for num in buckets[freq]:
            result.append(num)
            if len(buckets) == k:
                break
    return result
            
        


# -----------------------------------------------------------------------------
# 13. First Unique Character in a String
# -----------------------------------------------------------------------------
# Find the index of the first non-repeating character. Return -1 if none.
#
# Example:
#   s = "leetcode"
#   Output: 0
# -----------------------------------------------------------------------------

def q13(s):
    count = {}
    for letter in s:
        count = count.get(s, 0) + 1
    for i, n in enumerate(s):
        if count[n] == 1: 
            return i 
    return - 1

# -----------------------------------------------------------------------------
# 14. Majority Element
# -----------------------------------------------------------------------------
# Return the element that appears more than n // 2 times.
#
# Example:
#   nums = [2, 2, 1, 1, 1, 2, 2]
#   Output: 2
# -----------------------------------------------------------------------------

def q14(nums):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    return max(count, key=count.get)


# -----------------------------------------------------------------------------
# 15. Move Zeroes
# -----------------------------------------------------------------------------
# Move all zeroes to the end while preserving order of non-zero elements.
# In-place.
#
# Example:
#   nums = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]
# -----------------------------------------------------------------------------

def q15(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < fast:
        nums[slow] = 0
        slow += 1 

# -----------------------------------------------------------------------------
# 16. Two Sum II — Input Array Is Sorted
# -----------------------------------------------------------------------------
# Given a SORTED array, return 1-indexed positions of two numbers summing
# to target. O(1) space.
#
# Example:
#   numbers = [2, 7, 11, 15], target = 9
#   Output: [1, 2]
# -----------------------------------------------------------------------------

def q16(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        elif total > target:
            right -= 1


# -----------------------------------------------------------------------------
# 17. Squares of a Sorted Array
# -----------------------------------------------------------------------------
# Given a sorted array (can include negatives), return the squares, sorted.
#
# Example:
#   nums = [-4, -1, 0, 3, 10]
#   Output: [0, 1, 9, 16, 100]
# -----------------------------------------------------------------------------

def q17(nums):
    left, right = 0, len(nums) - 1 
    result = []
    top = len(nums) - 1
    while left < right:
        if nums[left] ** 2 > nums[right] ** 2:
            result[top] = nums[left] ** 2
            left += 1
        if nums[left] ** 2 < nums[right] ** 2:
            result[top] = nums[right] ** 2
            right -= 1
        else:
            top -= 1            
    return result 
# -----------------------------------------------------------------------------
# 18. Container With Most Water
# -----------------------------------------------------------------------------
# Find two lines that together with the x-axis form a container holding
# the most water. Return the max area.
#
# Example:
#   height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
# -----------------------------------------------------------------------------

def q18(height):
    pass


# -----------------------------------------------------------------------------
# 19. Merge Sorted Array
# -----------------------------------------------------------------------------
# Merge nums2 into nums1 in place. nums1 has length m+n with trailing
# zeroes as placeholder space.
#
# Example:
#   nums1 = [1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
#   Output: nums1 becomes [1,2,2,3,5,6]
# -----------------------------------------------------------------------------

def q19(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p3 = m + n - 1

    while p1 >= 0 or p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
            p3 -= 1
        elif nums1[p1] < nums2[p2]:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1
        
    while p2 >= 0:
        nums1[p3] = nums2[p2] 
        p2 -= 1
        p3 -= 1

# -----------------------------------------------------------------------------
# 20. Longest Consecutive Sequence
# -----------------------------------------------------------------------------
# Return the length of the longest consecutive integer sequence in an
# unsorted array. Must be O(n).
#
# Example:
#   nums = [100, 4, 200, 1, 3, 2]
#   Output: 4
# -----------------------------------------------------------------------------

def q20(nums):
    seen = set(nums)
    best = 0
    for n in nums:
        if n - 1 not in seen:
            length = 1
            while (length + n) in seen:
                length += 1
                best = max(best, length)
    return best 


# =============================================================================
#
#
#
#   ANSWER KEY — scroll down only after attempting everything!
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


# 2. Contains Duplicate — HASHING (seen set)
def q2_answer(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# 3. Valid Palindrome — TWO POINTERS (opposite ends)
def q3_answer(s):
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


# 4. Best Time to Buy and Sell Stock — ARRAYS (single pass, track min)
def q4_answer(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


# 5. Ransom Note — HASHING (frequency count, one dict)
def q5_answer(ransomNote, magazine):
    count = {}
    for c in magazine:
        count[c] = count.get(c, 0) + 1
    for c in ransomNote:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True


# 6. Group Anagrams — HASHING (sorted string as key)
def q6_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# 7. Intersection of Two Arrays — HASHING (set intersection)
def q7_answer(nums1, nums2):
    return list(set(nums1) & set(nums2))


# 8. Product of Array Except Self — ARRAYS (prefix + suffix pass)
def q8_answer(nums):
    n = len(nums)
    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] = answer[i] * suffix
        suffix *= nums[i]
    return answer


# 9. Isomorphic Strings — HASHING (bidirectional dict mapping)
def q9_answer(s, t):
    s_to_t = {}
    t_to_s = {}
    for schar, tchar in zip(s, t):
        if schar in s_to_t and s_to_t[schar] != tchar:
            return False
        if tchar in t_to_s and t_to_s[tchar] != schar:
            return False
        s_to_t[schar] = tchar
        t_to_s[tchar] = schar
    return True


# 10. Check If N and Its Double Exist — HASHING (seen set, check 2n and n/2)
def q10_answer(arr):
    seen = set()
    for n in arr:
        if 2 * n in seen or (n % 2 == 0 and n // 2 in seen):
            return True
        seen.add(n)
    return False


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


# 12. Top K Frequent Elements — HASHING + BUCKET SORT
def q12_answer(nums, k):
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


# 13. First Unique Character — HASHING (frequency count, two pass)
def q13_answer(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


# 14. Majority Element — HASHING (frequency count, max value)
def q14_answer(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return max(count, key=count.get)


# 15. Move Zeroes — TWO POINTERS (slow/fast)
def q15_answer(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1


# 16. Two Sum II — TWO POINTERS (opposite ends, sorted array)
def q16_answer(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1


# 17. Squares of a Sorted Array — TWO POINTERS (opposite ends, build backward)
def q17_answer(nums):
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


# 18. Container With Most Water — TWO POINTERS (opposite ends, move shorter)
def q18_answer(height):
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


# 19. Merge Sorted Array — TWO POINTERS (fill backward from the end)
def q19_answer(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
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


# 20. Longest Consecutive Sequence — HASHING (set, only count from starts)
def q20_answer(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            best = max(best, length)
    return best