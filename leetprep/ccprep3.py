# =============================================================================
# LEETCODE PRACTICE SET 2 — Arrays, Hashing, Strings
# =============================================================================
# Instructions: try each problem on your own first.
# Answer key is at the bottom — don't scroll until you've attempted it!
# =============================================================================


# -----------------------------------------------------------------------------
# LC 217 — Contains Duplicate (Easy) | REPEAT
# -----------------------------------------------------------------------------
# Given an integer array, return true if any value appears at least twice.
#
# Example:
#   nums = [1, 2, 3, 1]
#   Output: True
#
#   nums = [1, 2, 3, 4]
#   Output: False
#
# Pattern: seen set, O(1) lookup
# -----------------------------------------------------------------------------

def contains_duplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True  
        seen.add(n)
    return False  


# -----------------------------------------------------------------------------
# LC 242 — Valid Anagram (Easy) | REPEAT
# -----------------------------------------------------------------------------
# Given two strings s and t, return true if t is an anagram of s.
# (Write it with ONE dict — increment for s, decrement for t)
#
# Example:
#   s = "anagram", t = "nagaram"
#   Output: True
#
#   s = "rat", t = "car"
#   Output: False
#
# Pattern: increment/decrement one dict
# -----------------------------------------------------------------------------

def is_anagram(s, t):

    if len(s) != len(t):
        return False 
    
    sgram = {}
    for sletter in s:
        sgram[sletter] = sgram.get(sletter, 0) + 1

    for tletter in t:
        if tletter in sgram:
            sgram[tletter] -= 1
            if (sgram[tletter] < 0):
                return False 
    return True 

#or 

from collections import Counter 
def is_anagram(s, t):
    return Counter(s) == Counter(t)

# -----------------------------------------------------------------------------
# LC 169 — Majority Element (Easy) | NEW
# -----------------------------------------------------------------------------
# Given an array, return the element that appears more than n // 2 times.
# You may assume the majority element always exists.
#
# Example:
#   nums = [3, 2, 3]
#   Output: 3
#
#   nums = [2, 2, 1, 1, 1, 2, 2]
#   Output: 2
#
# Pattern: frequency count — which element has the highest count?
# -----------------------------------------------------------------------------

def majority_element(nums):
    count = {}
    max = 0 
    for n in nums:
        count[n] = count.get(n, 0) + 1
    
    return (max(count, key=count.get))


# -----------------------------------------------------------------------------
# LC 206 — Reverse a String's Words (Easy) | NEW
# -----------------------------------------------------------------------------
# Wait — this is LC 557: Reverse Words in a String III
# Given a string, reverse the order of characters in each word while
# preserving whitespace and word order.
#
# Example:
#   s = "Let's take LeetCode contest"
#   Output: "s'teL ekat edoCteeL tsetnoC"
#
# Pattern: split, reverse each word, rejoin
# -----------------------------------------------------------------------------

def reverse_words(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]
        return " ".join(words)



# -----------------------------------------------------------------------------
# LC 49 — Group Anagrams (Medium) | REPEAT
# -----------------------------------------------------------------------------
# Given an array of strings, group the anagrams together.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
# Pattern: sorted string as hashmap key
# (Try it without defaultdict — use a plain dict and .get())
# -----------------------------------------------------------------------------

from collections import defaultdict #dont use
def group_anagrams(strs):
    count = {}
    for st in strs:
        key = "".join(sorted(st))
        count[key] += count.get(key, []) + [st] #checks if first time key is not there 
    return list(count.values())


#or 
def group_anagrams(strs):
    groups = defaultdict(list) #handles first time problem without thinking so u can just append 
    for st in strs:
        key = "".join(sorted(st))
        groups[key].append(st) #much easier 
    return list(groups.values())
        

# -----------------------------------------------------------------------------
# LC 347 — Top K Frequent Elements (Medium) | REPEAT
# -----------------------------------------------------------------------------
# Given an integer array and integer k, return the k most frequent elements.
#
# Example:
#   nums = [1,1,1,2,2,3], k = 2
#   Output: [1, 2]
#
# Pattern: frequency count + bucket sort
# (Try the bucket sort approach — no heap, no sort)
# -----------------------------------------------------------------------------

def top_k_frequent(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1 #gets count for each number 
    
    for i in range(len(nums+1)):
        buckets = [] #creates empty lists (bucket method)

    for num, freq in count.items():
        buckets[freq].append(num) #uses frequency as index - higher index means higher frequnecy 

    result = []

    for freq in range(len(buckets)-1, 0, -1): #right to left (high frequency)
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k: #append until reaches k 
                return result 


    

    

    


# -----------------------------------------------------------------------------
# LC 238 — Product of Array Except Self (Medium) | REPEAT
# -----------------------------------------------------------------------------
# Given an integer array, return an array where each element is the product
# of all elements except itself. Must be O(n) — no division allowed.
#
# Example:
#   nums = [1, 2, 3, 4]
#   Output: [24, 12, 8, 6]
#
# Pattern: prefix pass left to right, suffix pass right to left
# -----------------------------------------------------------------------------

def product_except_self(nums):
    pass


# -----------------------------------------------------------------------------
# LC 128 — Longest Consecutive Sequence (Medium) | NEW
# -----------------------------------------------------------------------------
# Given an unsorted array, return the length of the longest consecutive
# sequence of integers. Must run in O(n).
#
# Example:
#   nums = [100, 4, 200, 1, 3, 2]
#   Output: 4  (sequence is [1, 2, 3, 4])
#
# Pattern: convert to set, only start counting from sequence beginnings
# Hint: a number is the START of a sequence if (num - 1) is NOT in the set.
# -----------------------------------------------------------------------------

def longest_consecutive(nums):
    pass


# -----------------------------------------------------------------------------
# LC 560 — Subarray Sum Equals K (Medium) | REPEAT
# -----------------------------------------------------------------------------
# Given an array and integer k, return the number of subarrays that sum to k.
#
# Example:
#   nums = [1, 2, 3], k = 3
#   Output: 2  ([1,2] and [3])
#
# Pattern: prefix sum + hashmap
# Remember: initialize seen = {0: 1} before the loop
# -----------------------------------------------------------------------------

def subarray_sum(nums, k):
    pass


# =============================================================================
#
#
#
#   ANSWER KEY — scroll down only after attempting each problem!
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


# -----------------------------------------------------------------------------
# LC 217 — Contains Duplicate
# -----------------------------------------------------------------------------
# As you scan, check if the current number is already in seen.
# If yes — duplicate found. If no — add it and keep going.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def contains_duplicate_answer(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# -----------------------------------------------------------------------------
# LC 242 — Valid Anagram
# -----------------------------------------------------------------------------
# Early exit if lengths differ — can't be anagrams.
# Increment for every char in s, decrement for every char in t.
# If anagrams, everything cancels to zero.
# Time: O(n) | Space: O(1) — at most 26 keys
# -----------------------------------------------------------------------------

def is_anagram_answer(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
    return all(v == 0 for v in count.values())


# -----------------------------------------------------------------------------
# LC 169 — Majority Element
# -----------------------------------------------------------------------------
# Count frequencies. Return the key with the highest value.
# max() with key=count.get finds the key whose value is largest.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def majority_element_answer(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return max(count, key=count.get)


# -----------------------------------------------------------------------------
# LC 557 — Reverse Words in a String III
# -----------------------------------------------------------------------------
# Split on spaces to get individual words.
# Reverse each word with slicing [::-1].
# Rejoin with spaces.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def reverse_words_answer(s):
    return " ".join(word[::-1] for word in s.split())


# -----------------------------------------------------------------------------
# LC 49 — Group Anagrams
# -----------------------------------------------------------------------------
# Sort each word to get a canonical key — all anagrams share the same key.
# Group words under their key in a dict.
# Time: O(n * k log k) | Space: O(n * k)
# -----------------------------------------------------------------------------

def group_anagrams_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# -----------------------------------------------------------------------------
# LC 347 — Top K Frequent Elements (bucket sort)
# -----------------------------------------------------------------------------
# Frequency can never exceed n, so create n+1 buckets.
# Each bucket i holds numbers that appear exactly i times.
# Scan buckets from highest to lowest, collect until we have k elements.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# LC 238 — Product of Array Except Self
# -----------------------------------------------------------------------------
# Left pass: answer[i] = product of everything to the LEFT of i.
# Right pass: multiply answer[i] by running suffix (product of everything RIGHT).
# No division needed, no extra array for suffix.
# Time: O(n) | Space: O(1) excluding output array
# -----------------------------------------------------------------------------

def product_except_self_answer(nums):
    n = len(nums)
    answer = [1] * n

    for i in range(1, n):
        answer[i] = answer[i - 1] * nums[i - 1]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] = answer[i] * suffix
        suffix *= nums[i]

    return answer


# -----------------------------------------------------------------------------
# LC 128 — Longest Consecutive Sequence
# -----------------------------------------------------------------------------
# Convert to set for O(1) lookup.
# Only start counting from sequence beginnings (num - 1 not in set).
# This ensures each sequence is counted exactly once.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def longest_consecutive_answer(nums):
    num_set = set(nums)
    best = 0

    for num in num_set:
        if num - 1 not in num_set:   # only start from sequence beginnings
            length = 1
            while num + length in num_set:
                length += 1
            best = max(best, length)

    return best


# -----------------------------------------------------------------------------
# LC 560 — Subarray Sum Equals K
# -----------------------------------------------------------------------------
# prefix sum tracks running total. seen stores how many times each
# prefix sum has appeared. At each index, if (prefix - k) is in seen,
# that many subarrays ending here sum to k.
# Initialize seen = {0: 1} to handle subarrays starting from index 0.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def subarray_sum_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}

    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count