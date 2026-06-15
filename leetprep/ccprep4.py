# =============================================================================
# LEETCODE PRACTICE SET 3 — Arrays, Hashing, Strings (Review Focus)
# =============================================================================
# Instructions: try each problem on your own first.
# Answer key is at the bottom — don't scroll until you've attempted it!
# =============================================================================


# -----------------------------------------------------------------------------
# LC 217 — Contains Duplicate (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Given an integer array, return true if any value appears at least twice.
# Write it with a seen set — no sorting.
#
# Example:
#   nums = [1, 2, 3, 1]
#   Output: True
#
#   nums = [1, 2, 3, 4]
#   Output: False
#
# Pattern: seen set, check before adding
# -----------------------------------------------------------------------------

def contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True 
        seen.add(n)
    return False 


# -----------------------------------------------------------------------------
# LC 1 — Two Sum (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Given an array and a target, return indices of the two numbers that
# add up to the target.
#
# Example:
#   nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
#
# Pattern: complement = target - n, store indices in dict
# -----------------------------------------------------------------------------

def two_sum(nums, target):
    seen = {}

    for i, n in enumerate(nums):
        complement = target - n 
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


# -----------------------------------------------------------------------------
# LC 383 — Ransom Note (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Return true if ransomNote can be built using letters from magazine.
# Each letter in magazine can only be used once.
# Write it manually — no Counter.
#
# Example:
#   ransomNote = "aa", magazine = "aab"
#   Output: True
#
#   ransomNote = "aab", magazine = "baa"
#   Output: True
#
# Pattern: count up for magazine, count down for ransomNote
# if any value goes negative → return False
# -----------------------------------------------------------------------------

def can_construct(ransomNote, magazine):
    count = {}
    for n in magazine:
        count[n] = count.get(n, 0) + 1
    
    for n in ransomNote:
        if n in count:
            count[n] = count.get(n, 0) - 1
            if (count[n] < 0):
                return False 
    return True 

# -----------------------------------------------------------------------------
# LC 387 — First Unique Character (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Find the first non-repeating character in a string and return its index.
# Return -1 if none exists.
#
# Example:
#   s = "leetcode"
#   Output: 0
#
#   s = "aabb"
#   Output: -1
#
# Pattern: pass 1 count frequencies, pass 2 find first with count == 1
# -----------------------------------------------------------------------------

def first_uniq_char(s):
    count = {}
    for sletter in s:
        count[sletter] = count.get(sletter, 0) + 1 #counts occurences 
    
    for i, c in enumerate(s):
        if count[c] == 1:
            return i 
    return - 1

# -----------------------------------------------------------------------------
# LC 125 — Valid Palindrome (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Return true if the string is a palindrome after removing non-alphanumeric
# characters and lowercasing everything.
#
# Example:
#   s = "A man, a plan, a canal: Panama"
#   Output: True
#
#   s = "race a car"
#   Output: False
#
# Pattern: two pointers from both ends, skip non-alphanumeric with isalnum()
# -----------------------------------------------------------------------------

def is_palindrome(s):
    left = 0
    right = len(s) - 1

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



# -----------------------------------------------------------------------------
# LC 242 — Valid Anagram (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Return true if t is an anagram of s.
# One dict only — increment for s, decrement for t.
#
# Example:
#   s = "anagram", t = "nagaram"
#   Output: True
#
#   s = "rat", t = "car"
#   Output: False
#
# Pattern: length check first, then increment/decrement one dict
# -----------------------------------------------------------------------------

def is_anagram(s, t):
    if len(s) != len(t):
        return False 
    
    count = {}
    for sletter in s:
        count[sletter] = count.get(sletter, 0) + 1

    for tletter in t:
        count[tletter] = count.get(tletter, 0) - 1
        if count[tletter] < 0:
            return False 
    return True 

# -----------------------------------------------------------------------------
# LC 169 — Majority Element (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Return the element that appears more than n // 2 times.
# The majority element always exists.
#
# Example:
#   nums = [3, 2, 3]
#   Output: 3
#
#   nums = [2, 2, 1, 1, 1, 2, 2]
#   Output: 2
#
# Pattern: count frequencies, return the key with the max value
# Hint: max(count, key=count.get) returns the key with the highest value
# -----------------------------------------------------------------------------

def majority_element(nums):
    count = {} 
    for n in nums:
        count[n] = count.get(n, 0) + 1
    return max(count, key=count.get)



# -----------------------------------------------------------------------------
# LC 219 — Contains Duplicate II (Medium) | REVIEW
# -----------------------------------------------------------------------------
# Return true if there are two indices i and j such that
# nums[i] == nums[j] and abs(i - j) <= k.
#
# Example:
#   nums = [1, 2, 3, 1], k = 3
#   Output: True
#
#   nums = [1, 2, 3, 1, 2, 3], k = 2
#   Output: False
#
# Pattern: dict storing last-seen index, check gap when duplicate found
# -----------------------------------------------------------------------------

def contains_nearby_duplicate(nums, k):
    seen = {}
    for i, n in enumerate(nums):
        if i in seen and abs(i - seen[n]) <= k:
            return True 
        seen[n] = i
    return False 



# -----------------------------------------------------------------------------
# LC 49 — Group Anagrams (Medium) | REVIEW
# -----------------------------------------------------------------------------
# Group strings that are anagrams of each other.
#
# Example:
#   strs = ["eat","tea","tan","ate","nat","bat"]
#   Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
#
# Pattern: sorted word as key, group under that key in a dict
# Try it with a plain dict — no defaultdict
# -----------------------------------------------------------------------------

def group_anagrams(strs):
    groups = {}
    for st in strs:
        key = "".join(sorted(st))
        # groups[key] = groups.get(key, []) + [st]
        #or 
        if key not in groups:
            groups[key] = []
        groups[key].append(st)
    return list(groups.values())



# -----------------------------------------------------------------------------
# LC 128 — Longest Consecutive Sequence (Medium) | REVIEW
# -----------------------------------------------------------------------------
# Return the length of the longest consecutive sequence in an unsorted array.
# Must be O(n).
#
# Example:
#   nums = [100, 4, 200, 1, 3, 2]
#   Output: 4  (sequence 1, 2, 3, 4)
#
# Pattern: convert to set, only start counting when (n-1) not in set
# -----------------------------------------------------------------------------

def longest_consecutive(nums):
    seen = set(nums)
    best = 0 
    
    for n in nums:
        if (n-1 not in seen):
            length = 1
            while (length + n in seen): #iterate until cant be seen anymore 
                length += 1
                best = max(length, best) 
    return length 
    


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
# Check before adding — if num is already in seen, it's a duplicate.
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
# LC 1 — Two Sum
# -----------------------------------------------------------------------------
# For each number compute complement = target - n.
# If complement is already in seen, we found our pair.
# Store index not just presence — we need to return both indices.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def two_sum_answer(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i


# -----------------------------------------------------------------------------
# LC 383 — Ransom Note
# -----------------------------------------------------------------------------
# Count up magazine chars, count down ransomNote chars.
# Return False the moment any count goes negative — ran out of that letter.
# Time: O(n) | Space: O(1) — at most 26 keys
# -----------------------------------------------------------------------------

def can_construct_answer(ransomNote, magazine):
    count = {}
    for c in magazine:
        count[c] = count.get(c, 0) + 1
    for c in ransomNote:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True


# -----------------------------------------------------------------------------
# LC 387 — First Unique Character
# -----------------------------------------------------------------------------
# Pass 1: build frequency dict.
# Pass 2: return index of first char with count == 1.
# Time: O(n) | Space: O(1) — at most 26 keys
# -----------------------------------------------------------------------------

def first_uniq_char_answer(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


# -----------------------------------------------------------------------------
# LC 125 — Valid Palindrome
# -----------------------------------------------------------------------------
# Two pointers from both ends. Skip non-alphanumeric chars on both sides.
# Compare lowercased chars — any mismatch means not a palindrome.
# Time: O(n) | Space: O(1)
# -----------------------------------------------------------------------------

def is_palindrome_answer(s):
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


# -----------------------------------------------------------------------------
# LC 242 — Valid Anagram
# -----------------------------------------------------------------------------
# Length check kills it early if lengths differ.
# Increment for s, decrement for t in one dict.
# All values should be 0 if they're anagrams.
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
        if count[c] < 0:
            return False
    return True


# -----------------------------------------------------------------------------
# LC 169 — Majority Element
# -----------------------------------------------------------------------------
# Count all frequencies then return the key with the highest count.
# max(count, key=count.get) iterates keys and picks the one with max value.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def majority_element_answer(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return max(count, key=count.get)


# -----------------------------------------------------------------------------
# LC 219 — Contains Duplicate II
# -----------------------------------------------------------------------------
# Store last-seen index for each number.
# When we see a repeat, check if the gap i - seen[n] <= k.
# Always update seen[n] = i so we have the most recent index.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def contains_nearby_duplicate_answer(nums, k):
    seen = {}
    for i, n in enumerate(nums):
        if n in seen and i - seen[n] <= k:
            return True
        seen[n] = i
    return False


# -----------------------------------------------------------------------------
# LC 49 — Group Anagrams
# -----------------------------------------------------------------------------
# Sort each word → same sorted string = same anagram group.
# Use sorted string as dict key, append word to that group.
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
# LC 128 — Longest Consecutive Sequence
# -----------------------------------------------------------------------------
# Convert to set for O(1) lookup.
# Only start counting from sequence beginnings (n-1 not in set).
# Walk forward with a while loop until the chain breaks.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

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