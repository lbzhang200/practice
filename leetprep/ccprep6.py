# =============================================================================
# DAILY LEETCODE PRACTICE 5 — Arrays, Hashing, Strings, Two Pointers
# =============================================================================
# Mix of review and new problems. Attempt before scrolling to the answer key.
# =============================================================================


# =============================================================================
# SECTION 1 — HASHING/ARRAYS/STRINGS REVIEW
# =============================================================================


# -----------------------------------------------------------------------------
# LC 1346 — Check If N and Its Double Exist (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Check if there exist i != j such that arr[i] == 2 * arr[j].
#
# Example:
#   arr = [10, 2, 5, 3]
#   Output: True   (10 == 2*5)
#
# Pattern: seen set, check 2*n and n//2 (guard n//2 with n % 2 == 0)
# -----------------------------------------------------------------------------

def check_if_exist(arr):
    seen = set()
    for n in arr:
        if (2 * n in seen) or (n// 2 and n % 2 == 0):
            return True 
        seen.add(n)
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
# Pattern: sorted word as dict key
# -----------------------------------------------------------------------------

def group_anagrams(strs):
    groups = {}
    for words in strs:
        key = "".join(sorted(words))
        groups[key] = groups.get(key, []) + [words]

    return list(groups.values())


# -----------------------------------------------------------------------------
# LC 560 — Subarray Sum Equals K (Medium) | REVIEW
# -----------------------------------------------------------------------------
# Return the number of subarrays that sum to k.
#
# Example:
#   nums = [1, 2, 3], k = 3
#   Output: 2
#
# Pattern: prefix sum + hashmap, seen = {0: 1} to start
# -----------------------------------------------------------------------------

def subarray_sum(nums, k):


    count = 0 
    prefix = 0 #prefix means all the array(subarray) added to it before 
    seen = {0: 1}
    for n in nums:
        prefix += n #adds previous numbers 
        if (prefix - n) in seen: #checks if other part is in seen
            count += seen[prefix - k]
        seen[prefix] = seen.get(prefix, 0) + 1 #adds prefix to the seen 
    return count 
       
# -----------------------------------------------------------------------------
# LC 205 — Isomorphic Strings (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Determine if s and t are isomorphic (one-to-one character mapping).
#
# Example:
#   s = "egg", t = "add"
#   Output: True
#
#   s = "foo", t = "bar"
#   Output: False
#
# Pattern: two dicts, s_to_t and t_to_s, check both directions
# -----------------------------------------------------------------------------

def is_isomorphic(s, t):
    s_to_t = {}
    t_to_s = {}

    for schar, tchar in zip(s, t):
        if (schar in s_to_t) and (s_to_t[schar] != tchar):
            return False 
        elif (tchar in t_to_s) and (t_to_s[tchar] != schar):
            return False
        s_to_t[schar] = tchar
        t_to_s[tchar] = schar 
    return True 

# =============================================================================
# SECTION 2 — TWO POINTERS REVIEW
# =============================================================================


# -----------------------------------------------------------------------------
# LC 125 — Valid Palindrome (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Return true if the string is a palindrome ignoring non-alphanumeric chars
# and case.
#
# Example:
#   s = "A man, a plan, a canal: Panama"
#   Output: True
#
# Pattern: opposite ends, skip non-alphanumeric with isalnum()
# -----------------------------------------------------------------------------

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left > right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower(): 
            return False 
        left += 1
        right -= 1 
    return True 


# -----------------------------------------------------------------------------
# LC 283 — Move Zeroes (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Move all zeroes to the end, preserving order of non-zero elements. In-place.
#
# Example:
#   nums = [0, 1, 0, 3, 12]
#   Output: [1, 3, 12, 0, 0]
#
# Pattern: slow/fast pointers, slow tracks write position
# -----------------------------------------------------------------------------

def move_zeroes(nums):
    slow = 0 
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1 
    while (slow < fast):
        nums[slow] = 0 
        slow += 1

# -----------------------------------------------------------------------------
# LC 167 — Two Sum II — Input Array Is Sorted (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Given a sorted array, return 1-indexed positions of two numbers summing
# to target. O(1) space — no hashmap.
#
# Example:
#   numbers = [2, 7, 11, 15], target = 9
#   Output: [1, 2]
#
# Pattern: opposite ends, move left if sum too small, right if too big
# -----------------------------------------------------------------------------

def two_sum_ii(numbers, target):
    left = 0 
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        elif total > right:
            right -= 1
    return numbers


# =============================================================================
# SECTION 3 — NEW PROBLEMS
# =============================================================================


# -----------------------------------------------------------------------------
# LC 977 — Squares of a Sorted Array (Easy) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given a sorted array (can include negatives), return the squares,
# also sorted ascending.
#
# Example:
#   nums = [-4, -1, 0, 3, 10]
#   Output: [0, 1, 9, 16, 100]
#
# Hint: biggest squares come from the extremes (most negative or most
#       positive). Build result backward, comparing from both ends.
# -----------------------------------------------------------------------------

def sorted_squares(nums):
    left = 0 
    right = len(nums) - 1
    top = len(nums) - 1
    result = [0] * len(nums)
    while left <= right:
        if nums[left] ** 2 > nums[right] ** 2:
            result[top] = nums[left] ** 2
            top -= 1
            left += 1
        else:
            result[top] = nums[right] ** 2 
            top -= 1 
            right -= 1
    return result 

# -----------------------------------------------------------------------------
# LC 392 — Is Subsequence (Easy) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given strings s and t, return true if s is a subsequence of t
# (characters of s appear in t in the same order, not necessarily adjacent).
#
# Example:
#   s = "abc", t = "ahbgdc"
#   Output: True
#
#   s = "axc", t = "ahbgdc"
#   Output: False
#
# Hint: one pointer for s, one for t. Advance t's pointer every step.
#       Only advance s's pointer when characters match.
#       If s's pointer reaches the end, s is fully matched.
# -----------------------------------------------------------------------------

def is_subsequence(s, t):
    i, j = 0
    while i < len(s) or j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(t) #if all indexes caught, then u found it 
#slow vs fast poitner 


# -----------------------------------------------------------------------------
# LC 905 — Sort Array By Parity (Easy) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given an array, move all even numbers before all odd numbers.
# Any order within evens/odds is fine. In-place.
#
# Example:
#   nums = [3, 1, 2, 4]
#   Output: [2, 4, 3, 1]   (or any valid arrangement)
#
# Hint: opposite ends. left scans for an odd number, right scans for an
#       even number. when found, swap them.
# -----------------------------------------------------------------------------

def sort_array_by_parity(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 != 0:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
    return nums 

# -----------------------------------------------------------------------------
# LC 5 — Longest Palindromic Substring (Medium) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given a string, return the longest palindromic substring.
#
# Example:
#   s = "babad"
#   Output: "bab"  (or "aba", both valid)
#
#   s = "cbbd"
#   Output: "bb"
#
# Hint: "expand around center". For each index, treat it as a potential
#       center and expand left/right while characters match. Try both
#       odd-length centers (single char) and even-length centers (between
#       two chars). Track the longest match found.
# -----------------------------------------------------------------------------

def longest_palindrome(s):
    
    #some other day 


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


# LC 1346 — Check If N and Its Double Exist
# build seen as you go. check 2*n and n//2 (guarded by n%2==0).
# Time: O(n) | Space: O(n)

def check_if_exist_answer(arr):
    seen = set()
    for n in arr:
        if 2 * n in seen or (n % 2 == 0 and n // 2 in seen):
            return True
        seen.add(n)
    return False


# LC 49 — Group Anagrams
# sorted string as dict key groups all anagrams together.
# Time: O(n * k log k) | Space: O(n * k)

def group_anagrams_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# LC 560 — Subarray Sum Equals K
# prefix sum tracks running total. seen tracks how many times each
# prefix sum has occurred. {0: 1} handles subarrays starting at index 0.
# Time: O(n) | Space: O(n)

def subarray_sum_answer(nums, k):
    count = 0
    prefix = 0
    seen = {0: 1}
    for num in nums:
        prefix += num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


# LC 205 — Isomorphic Strings
# two dicts ensure mapping is one-to-one in BOTH directions.
# Time: O(n) | Space: O(1) — bounded by alphabet size

def is_isomorphic_answer(s, t):
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


# --- SECTION 2 ANSWERS ---


# LC 125 — Valid Palindrome
# two pointers from both ends, skip non-alphanumeric, compare lowercased.
# Time: O(n) | Space: O(1)

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


# LC 283 — Move Zeroes
# slow tracks write position for next non-zero. fast scans everything.
# fill remaining with zero after.
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


# LC 167 — Two Sum II
# sorted array → opposite ends. sum too small → left+=1. too big → right-=1.
# Time: O(n) | Space: O(1)

def two_sum_ii_answer(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1


# --- SECTION 3 ANSWERS ---


# LC 977 — Squares of a Sorted Array
# biggest squares are at the extremes. compare from both ends,
# fill result backward (largest goes at the end first).
# Time: O(n) | Space: O(n)

def sorted_squares_answer(nums):
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


# LC 392 — Is Subsequence
# i tracks position in s, j tracks position in t.
# j always advances. i only advances on a match.
# if i reaches len(s), every char of s was found in order.
# Time: O(len(t)) | Space: O(1)

def is_subsequence_answer(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


# LC 905 — Sort Array By Parity
# left scans forward for an odd number. right scans backward for an even
# number. swap them when both are found. continue until pointers cross.
# Time: O(n) | Space: O(1)

def sort_array_by_parity_answer(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        elif nums[right] % 2 == 1:
            right -= 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
    return nums


# LC 5 — Longest Palindromic Substring
# expand around center: for each index, try it as an odd-length center
# (single char) and an even-length center (between two chars).
# expand outward while characters match, track the longest found.
# Time: O(n^2) | Space: O(1)

def longest_palindrome_answer(s):
    if not s:
        return ""

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # left+1 and right-1 are the actual bounds of the palindrome
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd = expand(i, i)          # single character center
        even = expand(i, i + 1)     # between i and i+1
        longest = max(longest, odd, even, key=len)

    return longest