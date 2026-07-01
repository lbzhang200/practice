# =============================================================================
# BINARY SEARCH — FULL REVIEW + PRACTICE SET
# =============================================================================
# Read the full intro before attempting problems.
# Answer key at the bottom.
# =============================================================================


# =============================================================================
# WHAT IS BINARY SEARCH?
# =============================================================================
#
# Binary search is a way to find something in a SORTED collection in
# O(log n) time instead of O(n) — by repeatedly cutting the search space
# in half.
#
# THE INTUITION: guessing a number game
# ─────────────────────────────────────────────────────────────────────────
# Imagine someone picked a number between 1 and 100 and you're guessing.
# Bad strategy: guess 1, 2, 3, 4, 5... (that's O(n), linear search)
# Good strategy: guess 50. Too high? Now you know it's 1-49. Guess 25.
#                Too low? Now it's 26-49. Guess 37. And so on.
#
# Each guess eliminates HALF of the remaining possibilities. That's why
# it's O(log n) — for 100 numbers you need at most ~7 guesses, not 100.
#
# ─────────────────────────────────────────────────────────────────────────
# THE CORE REQUIREMENT
# ─────────────────────────────────────────────────────────────────────────
# Binary search ONLY works on sorted data, OR on a search space where you
# can answer "yes/no, am I too high or too low" at every point — this is
# called a "monotonic" condition (once it flips from False to True, it
# never flips back).
#
# SIGNAL WORDS: "sorted array", "find the target", "minimum/maximum value
# such that...", "find the boundary where condition changes"
#
# ─────────────────────────────────────────────────────────────────────────
# THE BASIC TEMPLATE
# ─────────────────────────────────────────────────────────────────────────
#
#   def binary_search(arr, target):
#       left, right = 0, len(arr) - 1
#
#       while left <= right:
#           mid = (left + right) // 2
#
#           if arr[mid] == target:
#               return mid
#           elif arr[mid] < target:
#               left = mid + 1     # target is in the right half
#           else:
#               right = mid - 1    # target is in the left half
#
#       return -1   # not found
#
# WHY left <= right (not <)?
#   You need to check the case where left == right — that's still one
#   valid element left to check. If you stop at left < right, you'd
#   miss checking that final element.
#
# WHY mid = (left + right) // 2?
#   This picks the middle index. Integer division rounds down, so it
#   always lands on a valid index even with an even number of elements.
#
# WHY left = mid + 1 / right = mid - 1 (not just mid)?
#   You've already checked mid and confirmed it's not the answer, so
#   there's no reason to check it again. Excluding it from the next
#   search keeps the loop converging properly.
#
# ─────────────────────────────────────────────────────────────────────────
# THE THREE FLAVORS YOU'LL SEE
# ─────────────────────────────────────────────────────────────────────────
#
# 1. CLASSIC SEARCH — find an exact value in a sorted array.
#    (the template above)
#
# 2. SEARCH ON ANSWER — the array itself might not be sorted, but the
#    ANSWER space is monotonic. You binary search over possible answers
#    instead of array indices.
#    Example: "find the minimum capacity such that you can ship all
#    packages within D days" — you're not searching the package array,
#    you're searching the range of possible capacities.
#
# 3. FIND BOUNDARY — find the first/last position where a condition
#    becomes true/false (like the first True in a sorted [False, False,
#    True, True, True] array). This shows up disguised as "find first
#    bad version", "find peak element", etc.
#
# ─────────────────────────────────────────────────────────────────────────
# THE BIGGEST BEGINNER MISTAKES
# ─────────────────────────────────────────────────────────────────────────
# 1. Infinite loops — forgetting to move left/right past mid, so the
#    search space never shrinks.
# 2. Off-by-one errors — using < instead of <=, or mid instead of mid+1/mid-1.
# 3. Not recognizing "search on answer" problems because there's no
#    literal sorted array in sight — the array of POSSIBLE ANSWERS is
#    what's sorted, not the input.
#
# =============================================================================


# -----------------------------------------------------------------------------
# B1. LC 704 — Binary Search (Easy) | CLASSIC
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return the index of target, or -1
# if not found.
#
# Example:
#   nums = [-1,0,3,5,9,12], target = 9
#   Output: 4
#
#   nums = [-1,0,3,5,9,12], target = 2
#   Output: -1
# -----------------------------------------------------------------------------

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return - 1 

# -----------------------------------------------------------------------------
# B2. LC 35 — Search Insert Position (Easy) | CLASSIC variant
# -----------------------------------------------------------------------------
# Given a sorted array and a target, return the index if found. If not
# found, return the index where it would be inserted to keep it sorted.
#
# Example:
#   nums = [1,3,5,6], target = 5
#   Output: 2
#
#   nums = [1,3,5,6], target = 2
#   Output: 1   (would be inserted between index 0 and 1)
#
# Hint: same as classic binary search, but when not found, "left" ends up
#       exactly at the correct insertion point. Think about why.
# -----------------------------------------------------------------------------

def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid 
        elif nums[mid] > target:
            left =  mid + 1
        else:
            right = mid - 1 
    return left #left should be natural 

# -----------------------------------------------------------------------------
# B3. LC 374 — Guess Number Higher or Lower (Easy) | CLASSIC variant
# -----------------------------------------------------------------------------
# You're guessing a number between 1 and n. A guess(num) function tells
# you -1 (too high), 1 (too low), or 0 (correct). Find the number.
#
# For practice purposes, guess() is simulated below using a hidden target.
#
# Hint: identical structure to classic binary search, just using the
#       guess() function's return value instead of direct comparison.
# -----------------------------------------------------------------------------

def guess_number(n, secret):
    def guess(num):
        if num > secret:
            return -1
        elif num < secret:
            return 1
        else:
            return 0
    # write your binary search using the guess() function above
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        result = guess(mid)

        if result == 0:
            return mid
        elif result == -1:
            right = mid - 1
        else:
            left = mid + 1
    return - 1

# -----------------------------------------------------------------------------
# B4. LC 278 — First Bad Version (Easy) | FIND BOUNDARY
# -----------------------------------------------------------------------------
# You have n versions [1, 2, ..., n]. Versions become bad starting from
# some unknown point and all versions after that are also bad.
# isBadVersion(version) tells you if a version is bad.
# Find the FIRST bad version using as few calls as possible.
#
# For practice, isBadVersion() is simulated using a hidden first_bad value.
#
# Example:
#   n = 5, first_bad = 4
#   versions: [good, good, good, bad, bad]
#   Output: 4
#
# Hint: this is a "find boundary" problem. The array conceptually looks
#       like [False, False, False, True, True] — find the index of the
#       FIRST True. When isBadVersion(mid) is True, the answer could be
#       mid OR something earlier — so search left, but don't exclude mid.
#       When False, the answer must be after mid — exclude mid.
# -----------------------------------------------------------------------------

def first_bad_version(n, first_bad):
    def isBadVersion(version):
        return version >= first_bad
    # write your binary search using isBadVersion() above
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2 
        result = isBadVersion(mid)
        if result == True:
            right = mid #found it - could be an answer
        else:
            left = mid + 1

    return - 1

# -----------------------------------------------------------------------------
# B5. LC 153 — Find Minimum in Rotated Sorted Array (Medium) | MODIFIED SEARCH
# -----------------------------------------------------------------------------
# A sorted array has been rotated at some unknown pivot. Find the minimum
# element. No duplicates. Must be O(log n).
#
# Example:
#   nums = [4,5,6,7,0,1,2]
#   Output: 0
#
#   nums = [11,13,15,17]   (rotated 0 times, still "rotated")
#   Output: 11
#
# Hint: at each mid, compare nums[mid] to nums[right]. If nums[mid] >
#       nums[right], the minimum must be somewhere in the right half
#       (search right). Otherwise the minimum is at mid or in the left
#       half (search left, but don't exclude mid — it could BE the answer).
# -----------------------------------------------------------------------------

def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        result = nums[mid] 
        if result > nums[right]:
            left = mid + 1
        else:
            right = mid - 1
    return nums[left]


# -----------------------------------------------------------------------------
# B6. LC 33 — Search in Rotated Sorted Array (Medium) | MODIFIED SEARCH
# -----------------------------------------------------------------------------
# A sorted array has been rotated at an unknown pivot. Given a target,
# return its index, or -1 if not present. Must be O(log n).
#
# Example:
#   nums = [4,5,6,7,0,1,2], target = 0
#   Output: 4
#
#   nums = [4,5,6,7,0,1,2], target = 3
#   Output: -1
#
# Hint: at each mid, one half of the array (left or right of mid) is
#       guaranteed to be properly sorted, even though the whole array
#       isn't. Figure out which half is sorted, then check if target
#       falls within that sorted half's range. If yes, search there.
#       If no, search the other half.
# -----------------------------------------------------------------------------

def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid 

        if nums[left] < nums[mid]:
            if nums[left] < target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1  
    return - 1



# -----------------------------------------------------------------------------
# B7. LC 875 — Koko Eating Bananas (Medium) | SEARCH ON ANSWER
# -----------------------------------------------------------------------------
# Koko has piles of bananas and h hours to eat them all. She picks a
# speed k (bananas per hour). Each hour she eats up to k bananas from
# one pile (if a pile has less than k, she finishes it and stops that
# hour without eating more). Find the MINIMUM k such that she can eat
# all bananas within h hours.
#
# Example:
#   piles = [3,6,7,11], h = 8
#   Output: 4
#
# Hint: this is "search on answer" — you're not searching the piles
#       array, you're searching the range of possible eating speeds
#       (1 to max(piles)). For a given speed k, you can calculate hours
#       needed: sum of ceil(pile/k) for each pile. Binary search for the
#       minimum k where hours_needed <= h.
# -----------------------------------------------------------------------------

def min_eating_speed(piles, h):
    #idk bruh


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


# B1. Binary Search — CLASSIC
# standard template. mid found → return. else narrow to correct half.
# Time: O(log n) | Space: O(1)

def search_answer(nums, target):
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


# B2. Search Insert Position — CLASSIC variant
# same template. if never found, "left" naturally lands on the
# correct insertion point when the loop ends.
# Time: O(log n) | Space: O(1)

def search_insert_answer(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left   # insertion point


# B3. Guess Number Higher or Lower — CLASSIC variant
# same template, using guess() return value instead of direct comparison.
# Time: O(log n) | Space: O(1)

def guess_number_answer(n, secret):
    def guess(num):
        if num > secret:
            return -1
        elif num < secret:
            return 1
        else:
            return 0

    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == 1:
            left = mid + 1   # guessed too low, search higher
        else:
            right = mid - 1  # guessed too high, search lower
    return -1


# B4. First Bad Version — FIND BOUNDARY
# when isBadVersion(mid) is True, answer could be mid or earlier —
# search left INCLUDING mid (right = mid, not mid - 1).
# when False, answer must be after mid — search right EXCLUDING mid.
# Time: O(log n) | Space: O(1)

def first_bad_version_answer(n, first_bad):
    def isBadVersion(version):
        return version >= first_bad

    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid       # mid could be the answer, keep it in range
        else:
            left = mid + 1    # mid is definitely not the answer
    return left   # left == right at this point, pointing to first bad version
 

# B5. Find Minimum in Rotated Sorted Array — MODIFIED SEARCH
# compare nums[mid] to nums[right]. if mid > right, min is in right half.
# otherwise min is at mid or in left half (keep mid in range).
# Time: O(log n) | Space: O(1)

def find_min_answer(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1     # min is in the right portion
        else:
            right = mid        # min is at mid or in left portion, keep mid
    return nums[left]


# B6. Search in Rotated Sorted Array — MODIFIED SEARCH
# determine which half (left or right of mid) is properly sorted.
# check if target falls within that sorted half's range to decide
# which side to search next.
# Time: O(log n) | Space: O(1)

def search_rotated_answer(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:   # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1        # target is in the sorted left half
            else:
                left = mid + 1         # target must be in the right half
        else:                          # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1         # target is in the sorted right half
            else:
                right = mid - 1        # target must be in the left half

    return -1


# B7. Koko Eating Bananas — SEARCH ON ANSWER
# binary search over possible eating speeds (1 to max(piles)).
# for each candidate speed, calculate hours needed using ceiling division.
# find the minimum speed where hours needed <= h.
# Time: O(n log m) where m = max pile size | Space: O(1)

def min_eating_speed_answer(piles, h):
    def hours_needed(speed):
        total = 0
        for pile in piles:
            total += -(-pile // speed)   # ceiling division trick
        return total

    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= h:
            right = mid        # mid works, try to find something smaller
        else:
            left = mid + 1     # mid too slow, need a faster speed
    return left