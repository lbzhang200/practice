# =============================================================================
# DAILY LEETCODE PRACTICE — Arrays/Hashing/Strings Review + Two Pointers Intro
# =============================================================================
# Instructions: attempt each problem before scrolling to the answer key.
# New topic today: TWO POINTERS — read the intro below before starting.
# =============================================================================


# =============================================================================
# TWO POINTERS — WHAT IT IS AND WHEN TO USE IT
# =============================================================================
#
# The idea is simple: instead of one loop variable, you use TWO pointers
# (usually called left and right, or i and j) that move toward each other
# or in the same direction through an array or string.
#
# This turns many O(n²) brute force problems into O(n) solutions.
#
# WHEN TO REACH FOR TWO POINTERS:
# ─────────────────────────────────────────────────────────────────────
# 1. "Find a pair that satisfies some condition" in a SORTED array
#    → left starts at 0, right starts at end, they move toward each other
#    → example: two sum on sorted array, container with most water
#
# 2. "Remove/filter elements in place"
#    → slow pointer tracks where to write, fast pointer scans forward
#    → example: remove duplicates, move zeroes
#
# 3. "Is this string/array a palindrome?"
#    → left from start, right from end, compare and move inward
#    → example: valid palindrome (you've done this one!)
#
# 4. Sliding window (next topic after this) is a subset of two pointers
#    where the window expands and shrinks dynamically
#
# THE CORE MOVES:
# ─────────────────────────────────────────────────────────────────────
#
#   OPPOSITE ENDS — move toward each other:
#   left, right = 0, len(arr) - 1
#   while left < right:
#       if condition:
#           left += 1
#       else:
#           right -= 1
#
#   SAME DIRECTION — slow/fast pointers:
#   slow = 0
#   for fast in range(len(arr)):
#       if some condition on arr[fast]:
#           arr[slow] = arr[fast]
#           slow += 1
#
# SIGNAL WORDS IN PROBLEMS:
# "sorted array", "pair", "in-place", "without extra space",
# "two indices", "palindrome", "reverse"
#
# =============================================================================


# =============================================================================
# SECTION 1 — HASHING/ARRAYS/STRINGS REVIEW
# =============================================================================


# -----------------------------------------------------------------------------
# LC 1 — Two Sum (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Given an array and target, return indices of two numbers that sum to target.
#
# Example:
#   nums = [3, 4, 5, 6], target = 7
#   Output: [0, 1]
#
# Pattern: complement lookup, seen dict storing indices
# -----------------------------------------------------------------------------

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n 
        if comp in seen:
            return [seen[n], i]
        seen[n] = i


# -----------------------------------------------------------------------------
# LC 217 — Contains Duplicate (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Return true if any value appears at least twice.
#
# Example:
#   nums = [1, 2, 3, 1]
#   Output: True
#
# Pattern: seen set, check before adding
# -----------------------------------------------------------------------------

def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return False 
        seen.add(n)
    return True 


# -----------------------------------------------------------------------------
# LC 242 — Valid Anagram (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Return true if t is an anagram of s. One dict, no Counter.
#
# Example:
#   s = "racecar", t = "carrace"
#   Output: True
#
# Pattern: length check, increment for s, decrement for t
# -----------------------------------------------------------------------------

def is_anagram(s, t):
    if len(s) != len(t):
        return False 
    
    count = {}

    for sletter in s:
        count[s] = count.get(sletter, 0) + 1

    for tletter in t:
        if tletter in count:
            count[tletter] = count.get(tletter, 0) - 1
            if count < 0:
                return False 
    return True 

# -----------------------------------------------------------------------------
# LC 347 — Top K Frequent Elements (Medium) | REVIEW
# -----------------------------------------------------------------------------
# Return the k most frequent elements. Use bucket sort approach.
#
# Example:
#   nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
#
# Pattern: frequency dict → buckets by frequency → scan right to left
# -----------------------------------------------------------------------------

def top_k_frequent(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    buckets=[]
    for i in range(len(nums) + 1): #creates array for buckets 
        buckets = []
    for num, freq in (count.items()):
        buckets[freq] = num # higher index means higher frequency number 

    seen = []
    for freq in range(len(buckets)-1, -1, -1): #loops through buckets backawards 
        for num in buckets[freq]: #gets the number 
            seen.append(num)
            if len(seen) == k:
                return seen 
        

# -----------------------------------------------------------------------------
# LC 128 — Longest Consecutive Sequence (Medium) | REVIEW
# -----------------------------------------------------------------------------
# Return length of longest consecutive integer sequence. Must be O(n).
#
# Example:
#   nums = [100, 4, 200, 1, 3, 2]
#   Output: 4
#
# Pattern: convert to set, only count from sequence starts (n-1 not in set)
# -----------------------------------------------------------------------------

def longest_consecutive(nums):
    seen = set(nums)
    for n in nums:
        if (n-1) not in seen:
            length = 1
            while (length + n in seen):
                length += 1
            best = max(best, length)
    return best 

# =============================================================================
# SECTION 2 — TWO POINTERS (NEW)
# =============================================================================
# Read the intro at the top before attempting these.
# These are ordered easiest to hardest — do them in order.
# =============================================================================


# -----------------------------------------------------------------------------
# LC 167 — Two Sum II (Easy) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given a SORTED array and a target, return the 1-indexed positions of the
# two numbers that add up to target. Exactly one solution exists.
# Must use O(1) extra space — no hashmap allowed.
#
# Example:
#   numbers = [2, 7, 11, 15], target = 9
#   Output: [1, 2]   (1-indexed)
#
#   numbers = [2, 3, 4], target = 6
#   Output: [1, 3]
#
# Hint: array is sorted. left starts at 0, right at end.
#       if sum is too big → move right left
#       if sum is too small → move left right
#       if sum == target → found it
# -----------------------------------------------------------------------------

def two_sum_ii(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right += 1

# -----------------------------------------------------------------------------
# LC 283 — Move Zeroes (Easy) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given an array, move all zeroes to the end while maintaining the relative
# order of non-zero elements. Must do it in-place.
#
# Example:
#   nums = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]
#
#   nums = [0, 0, 1]
#   Output: [1, 0, 0]
#
# Hint: slow pointer tracks where to write the next non-zero.
#       fast pointer scans through everything.
#       when fast finds a non-zero, write it to slow's position.
#       fill the rest with zeroes at the end.
# -----------------------------------------------------------------------------

def move_zeroes(nums):

    #slow stores index one by one, fast looks through the array 
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1 
    while slow < len(nums): #replace rest with zeroes 
        nums[slow] = 0
        slow += 1

def move_zeroes2(nums):

    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1

# -----------------------------------------------------------------------------
# LC 26 — Remove Duplicates from Sorted Array (Easy) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given a sorted array, remove duplicates IN PLACE and return the count
# of unique elements. The relative order must be kept.
#
# Example:
#   nums = [1, 1, 2]
#   Output: 2  (nums becomes [1, 2, ...])
#
#   nums = [0, 0, 1, 1, 1, 2, 2, 3]
#   Output: 4  (nums becomes [0, 1, 2, 3, ...])
#
# Hint: slow pointer tracks the last unique element written.
#       fast pointer scans forward.
#       when fast finds a new unique value (different from slow),
#       write it to slow+1 and advance slow.
# -----------------------------------------------------------------------------

def remove_duplicates(nums):
    slow = 0 
    for fast in range(1, len(nums)): #start at one to compare withp previous  
        if nums[fast] != nums[slow]:
            slow += 1 #add it to the next unique element 
            nums[slow] = nums[fast]
    return slow + 1 #want the total count- len is +! 

def removeduplicates2(nums):
    slow = 0 
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow+=1 
            nums[slow] = nums[fast]
    return slow + 1 

# -----------------------------------------------------------------------------
# LC 344 — Reverse String (Easy) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Reverse a list of characters IN PLACE. Must be O(1) extra space.
#
# Example:
#   s = ["h","e","l","l","o"]
#   Output: ["o","l","l","e","h"]
#
# Hint: left and right pointers from both ends.
#       swap them and move inward. stop when they meet.
# -----------------------------------------------------------------------------

def reverse_string(s):
    left = 0 
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left+=1 
        right -= 1

    return s


# -----------------------------------------------------------------------------
# LC 11 — Container With Most Water (Medium) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given an array of heights, find two lines that together with the x-axis
# form a container that holds the most water. Return the max area.
#
# Example:
#   height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
#   Output: 49
#
# Area formula: min(height[left], height[right]) * (right - left)
#
# Hint: left=0, right=end. Calculate area at each step.
#       always move the pointer with the SHORTER height inward.
#       why? moving the taller one can only make things worse.
# -----------------------------------------------------------------------------

def max_water(height):
    pass


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


# --- SECTION 1 ANSWERS ---


# LC 1 — Two Sum
# complement = target - n. if seen → return indices. else store index.
# Time: O(n) | Space: O(n)

def two_sum_answer(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


# LC 217 — Contains Duplicate
# check before adding to seen set. short circuit on first duplicate.
# Time: O(n) | Space: O(n)

def contains_duplicate_answer(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# LC 242 — Valid Anagram
# length check first. increment for s, decrement for t.
# return False the moment any count goes negative.
# Time: O(n) | Space: O(1)

def is_anagram_answer(s, t):
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


# LC 347 — Top K Frequent Elements (bucket sort)
# frequency dict → place in bucket by freq → scan right to left for top k
# Time: O(n) | Space: O(n)

def top_k_frequent_answer(nums, k):
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


# LC 128 — Longest Consecutive Sequence
# set for O(1) lookup. only count from starts (n-1 not in set).
# walk forward while chain continues, track best length.
# Time: O(n) | Space: O(n)

def longest_consecutive_answer(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            best = max(best, length)
    return best


# --- SECTION 2 ANSWERS ---


# LC 167 — Two Sum II
# sorted array means we can use two pointers instead of a hashmap.
# sum too big → shrink from right. sum too small → grow from left.
# return 1-indexed positions when found.
# Time: O(n) | Space: O(1)

def two_sum_ii_answer(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]    # +1 because 1-indexed
        elif total < target:
            left += 1                        # need bigger sum
        else:
            right -= 1                       # need smaller sum


# LC 283 — Move Zeroes
# slow tracks where to write next non-zero value.
# fast scans everything. when non-zero found, write to slow and advance.
# fill remaining positions with 0 after the loop.
# Time: O(n) | Space: O(1)

def move_zeroes_answer(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1


# LC 26 — Remove Duplicates from Sorted Array
# slow points to last unique value written. fast scans forward.
# when fast finds a value different from slow, write it to slow+1.
# return slow+1 as the count of unique elements.
# Time: O(n) | Space: O(1)

def remove_duplicates_answer(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


# LC 344 — Reverse String
# classic opposite-ends two pointer. swap and move inward until they meet.
# Time: O(n) | Space: O(1)

def reverse_string_answer(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


# LC 11 — Container With Most Water
# area = min(heights) * width. always move the shorter pointer inward.
# moving the taller one can only decrease or keep area the same.
# track max area seen at each step.
# Time: O(n) | Space: O(1)

def max_water_answer(height):
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