# =============================================================================
# LEETCODE PRACTICE SET — Arrays, Hashing, Strings
# =============================================================================
# Instructions: try each problem on your own first.
# Answer key is at the bottom — don't scroll until you've attempted it!
# =============================================================================


# -----------------------------------------------------------------------------
# LC 1 — Two Sum (Easy) | REPEAT
# -----------------------------------------------------------------------------
# Given an array of integers and a target, return the indices of the two
# numbers that add up to the target. Each input has exactly one solution.
#
# Example:
#   nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]  (because nums[0] + nums[1] = 9)
#
# Pattern: complement lookup, seen dict
# -----------------------------------------------------------------------------

def two_sum(nums, target):
    
    seen = set()
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[n], i]
        seen[n] = i

    

# -----------------------------------------------------------------------------
# LC 125 — Valid Palindrome (Easy) | REPEAT
# -----------------------------------------------------------------------------
# A phrase is a palindrome if it reads the same forward and backward after
# lowercasing and removing all non-alphanumeric characters.
#
# Example:
#   s = "A man, a plan, a canal: Panama"
#   Output: True
#
#   s = "race a car"
#   Output: False
#
# Pattern: two pointers, string cleaning
# -----------------------------------------------------------------------------

def is_palindrome(s):
    left = s[0]
    right = len(s) - 1

    while left < right:
        if left < right and not s[left].isalnum():
            left += 1
        if right > left and not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False 
        left += 1
        right -= 1

    return True 


# -----------------------------------------------------------------------------
# LC 383 — Ransom Note (Easy) | REPEAT
# -----------------------------------------------------------------------------
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed using letters from magazine (each letter can only be used once).
#
# Example:
#   ransomNote = "aa", magazine = "aab"
#   Output: True
#
# Pattern: frequency count, one dict (no Counter — write it manually!)
# -----------------------------------------------------------------------------

def can_construct(ransomNote, magazine):
    count = {}
    for c in ransomNote:
        count[c] = count.get(c, 0) + 1 #number of occurences for letter
    
    for c in magazine:
        count[c] = count.get(c, 0) - 1
        if (count[c] < 0):
            return False 
        
    return True 



# -----------------------------------------------------------------------------
# LC 387 — First Unique Character in a String (Easy) | NEW
# -----------------------------------------------------------------------------
# Given a string s, find the first non-repeating character and return its
# index. If it does not exist, return -1.
#
# Example:
#   s = "leetcode"
#   Output: 0  (l appears once, and is first)
#
#   s = "aabb"
#   Output: -1
#
# Pattern: frequency count, two pass
# -----------------------------------------------------------------------------

def first_uniq_char(s):
    count = {}
    for sletter in s:
        count[sletter] = count.get(sletter, 0) + 1

    for i, n in enumerate(s):
        if (count[n] == 1):
            return i
    return -1 

def first_uniq_char(s):
    count = {}
    for sletter in s:
        count[sletter] = count.get(sletter, 0) + 1

    for i, n in enumerate(s):
        


# -----------------------------------------------------------------------------
# LC 412 — Fizz Buzz (Easy) | NEW
# -----------------------------------------------------------------------------
# Given an integer n, return a list of strings for each number from 1 to n:
#   - "FizzBuzz" if divisible by both 3 and 5
#   - "Fizz" if divisible by 3
#   - "Buzz" if divisible by 5
#   - the number as a string otherwise
#
# Example:
#   n = 5
#   Output: ["1", "2", "Fizz", "4", "Buzz"]
#
# Pattern: modulo, conditionals (watch the order!)
# -----------------------------------------------------------------------------

def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result 
        

# -----------------------------------------------------------------------------
# LC 219 — Contains Duplicate II (Medium) | REPEAT
# -----------------------------------------------------------------------------
# Given an integer array and an integer k, return true if there are two
# distinct indices i and j such that nums[i] == nums[j] and abs(i - j) <= k.
#
# Example:
#   nums = [1, 2, 3, 1], k = 3
#   Output: True  (nums[0] == nums[3] and abs(0-3) = 3 <= k)
#
#   nums = [1, 2, 3, 1, 2, 3], k = 2
#   Output: False
#
# Pattern: seen dict storing last-seen index, enumerate
# -----------------------------------------------------------------------------

def contains_nearby_duplicate(nums, k):
    seen = set()
    for i, n in enumerate(nums):
        if n in seen and abs(seen[n] - i) <= k:
            return True 
        seen[n] = i

    return False 



# -----------------------------------------------------------------------------
# LC 349 — Intersection of Two Arrays (Easy) | REPEAT
# -----------------------------------------------------------------------------
# Given two integer arrays, return their intersection. Each element in the
# result must be unique.
#
# Example:
#   nums1 = [1, 2, 2, 1], nums2 = [2, 2]
#   Output: [2]
#
# Pattern: set intersection (try the one-liner you learned!)
# -----------------------------------------------------------------------------

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))


# -----------------------------------------------------------------------------
# LC 438 — Find All Anagrams in a String (Medium) | NEW
# -----------------------------------------------------------------------------
# Given two strings s and p, return a list of all start indices of p's
# anagrams in s.
#
# Example:
#   s = "cbaebabacd", p = "abc"
#   Output: [0, 6]  (s[0:3]="cba" and s[6:9]="bac" are anagrams of "abc")
#
# Pattern: sliding window + frequency count
# Hint: fixed window of size len(p). Add new char, remove old char as it slides.
# -----------------------------------------------------------------------------

def find_anagrams(s, p):
    


# -----------------------------------------------------------------------------
# LC 3 — Longest Substring Without Repeating Characters (Medium) | NEW
# -----------------------------------------------------------------------------
# Given a string s, find the length of the longest substring that contains
# no repeating characters.
#
# Example:
#   s = "abcabcbb"
#   Output: 3  ("abc")
#
#   s = "bbbbb"
#   Output: 1  ("b")
#
# Pattern: sliding window, seen set, two pointers (left/right)
# Hint: expand right, shrink left when you hit a duplicate.
# -----------------------------------------------------------------------------

def length_of_longest_substring(s):
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
# LC 1 — Two Sum
# -----------------------------------------------------------------------------
# For each number, compute the complement (target - n).
# If it's already in seen, we found our pair — return both indices.
# Otherwise store the current number and its index for future lookups.
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
# LC 125 — Valid Palindrome
# -----------------------------------------------------------------------------
# Two pointers from both ends. Skip non-alphanumeric characters.
# Compare lowercased characters — if any mismatch, not a palindrome.
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
# LC 383 — Ransom Note
# -----------------------------------------------------------------------------
# Count magazine chars up, ransomNote chars down.
# If any value goes negative, we ran out of that letter.
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
# LC 387 — First Unique Character in a String
# -----------------------------------------------------------------------------
# Pass 1: build frequency dict for all characters.
# Pass 2: scan left to right — first char with count == 1 is the answer.
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
# LC 412 — Fizz Buzz
# -----------------------------------------------------------------------------
# Check divisible by 15 first — if you check 3 or 5 first you'll
# never reach the FizzBuzz case for multiples of both.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def fizz_buzz_answer(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


# -----------------------------------------------------------------------------
# LC 219 — Contains Duplicate II
# -----------------------------------------------------------------------------
# Store the last-seen index for each number.
# When we see a repeat, check if the gap is within k.
# Update the stored index every time (we always want the most recent).
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
# LC 349 — Intersection of Two Arrays
# -----------------------------------------------------------------------------
# Convert both to sets. The & operator gives elements in both.
# list() converts back to a list as required by the return type.
# Time: O(n + m) | Space: O(n + m)
# -----------------------------------------------------------------------------

def intersection_answer(nums1, nums2):
    return list(set(nums1) & set(nums2))


# -----------------------------------------------------------------------------
# LC 438 — Find All Anagrams in a String
# -----------------------------------------------------------------------------
# Maintain frequency dicts for the current window and for p.
# Slide a window of size len(p) across s — add new char, remove old char.
# When both dicts match, the window is an anagram — record the start index.
# Time: O(n) | Space: O(1) — at most 26 keys
# -----------------------------------------------------------------------------

def find_anagrams_answer(s, p):
    if len(p) > len(s):
        return []

    p_count = {}
    window = {}
    for c in p:
        p_count[c] = p_count.get(c, 0) + 1

    result = []
    for i in range(len(s)):
        # add new char on the right
        window[s[i]] = window.get(s[i], 0) + 1

        # remove char that fell out of the window on the left
        if i >= len(p):
            left_char = s[i - len(p)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

        # check if current window matches p
        if window == p_count:
            result.append(i - len(p) + 1)

    return result


# -----------------------------------------------------------------------------
# LC 3 — Longest Substring Without Repeating Characters
# -----------------------------------------------------------------------------
# Two pointers: left and right. Expand right each iteration.
# If s[right] is already in our seen set, shrink from the left
# until the duplicate is removed. Track the max window size.
# Time: O(n) | Space: O(n)
# -----------------------------------------------------------------------------

def length_of_longest_substring_answer(s):
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