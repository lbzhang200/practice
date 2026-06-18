# =============================================================================
# DAILY LEETCODE PRACTICE 6 — Arrays, Hashing, Strings, Two Pointers + Sliding Window
# =============================================================================
# Mix of review and new. Attempt before scrolling to the answer key.
# Two pointers: try these COLD, no hints, time yourself.
# Sliding window: new topic, hints provided.
# =============================================================================


# =============================================================================
# SECTION 1 — HASHING/ARRAYS/STRINGS REVIEW
# =============================================================================


# -----------------------------------------------------------------------------
# LC 387 — First Unique Character in a String (Easy) | REVIEW
# -----------------------------------------------------------------------------
# Find the index of the first non-repeating character. Return -1 if none.
#
# Example:
#   s = "leetcode"
#   Output: 0
#
# Pattern: frequency count, two pass
# -----------------------------------------------------------------------------

def first_uniq_char(s):
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    for i, n in enumerate(s):
        if count[n] == 1:
            return i
    return - 1

# -----------------------------------------------------------------------------
# LC 128 — Longest Consecutive Sequence (Medium) | REVIEW
# -----------------------------------------------------------------------------
# Return length of longest consecutive integer sequence. O(n).
#
# Example:
#   nums = [100, 4, 200, 1, 3, 2]
#   Output: 4
#
# Pattern: set, only count from sequence starts (n-1 not in set)
# -----------------------------------------------------------------------------
def longest_consecutive(nums):
    seen = set(nums)
    best = 0 
    for n in nums:
        if n-1 not in seen:
            length = 1
            while length + n in seen:
                length += 1
                best = max(best, length)
    return best 


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
        keys = "".join(sorted(words))
        groups[keys] = groups.get(keys, []) + [words] 
    return list(groups.values())



# =============================================================================
# SECTION 2 — TWO POINTERS — TRY COLD, NO HINTS, TIME YOURSELF
# =============================================================================


# -----------------------------------------------------------------------------
# LC 26 — Remove Duplicates from Sorted Array (Easy) | COLD
# -----------------------------------------------------------------------------
# Remove duplicates in place from a sorted array, return count of uniques.
#
# Example:
#   nums = [0,0,1,1,1,2,2,3]
#   Output: 4
# -----------------------------------------------------------------------------

def remove_duplicates(nums):
    slow = 0 
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


# -----------------------------------------------------------------------------
# LC 977 — Squares of a Sorted Array (Easy) | COLD
# -----------------------------------------------------------------------------
# Given sorted array (can include negatives), return sorted squares.
#
# Example:
#   nums = [-4,-1,0,3,10]
#   Output: [0,1,9,16,100]
# -----------------------------------------------------------------------------

def sorted_squares(nums):
    left = 0
    right = len(nums) - 1
    top = len(nums) - 1
    result = [0] * len(nums)
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
# LC 11 — Container With Most Water (Medium) | COLD
# -----------------------------------------------------------------------------
# Find two lines that form a container holding the most water.
#
# Example:
#   height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
# -----------------------------------------------------------------------------

def max_water(height):
    left, right = 0, len(height) - 1
    best = 0 
    while left < right: 
        maxheight = min(height[left], height[right]) / (right - left)
        best = max(best, maxheight)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best 

# -----------------------------------------------------------------------------
# LC 15 — 3Sum (Medium) | NEW — Two Pointers
# -----------------------------------------------------------------------------
# Given an array, find all unique triplets that sum to 0.
#
# Example:
#   nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1,-1,2],[-1,0,1]]
#
# Hint: sort the array first. Fix one number, then use two pointers
#       (opposite ends) on the rest to find pairs that complete the sum to 0.
#       Watch out for duplicate triplets — skip over repeated values.
# -----------------------------------------------------------------------------

def three_sum(nums):
    nums = nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 & nums[i] == nums[i+1]:
            continue 

        if nums[i] > 0: 
            break

        left, right = 0, len(nums) - 1
        while left < right:
            target = nums[left] + nums[right] + nums[i]
            if target == 0:
                result.append(nums[i], nums[left], nums[right])
                left += 1
                right -= 1
                if nums[left] < nums[right] & nums[left] != nums[left - 1]:
                    left += 1
                elif nums[left] < nums[right] & nums[right] != nums[right + 1]:
                    right -= 1
            elif target < 0:
                left += 1
            else:
                right -= 1
        return result 

# =============================================================================
# SECTION 3 — SLIDING WINDOW (NEW TOPIC)
# =============================================================================
#
# RECAP FROM EARLIER:
# Sliding window = two pointers moving in the SAME direction, maintaining
# a "window" between them.
#
# FIXED WINDOW — size never changes, just slides across
#   used for: "subarray/substring of size k"
#
# VARIABLE WINDOW — grows and shrinks based on a condition
#   used for: "longest/shortest subarray/substring that satisfies X"
#
# THE TEMPLATE FOR VARIABLE WINDOW:
#   left = 0
#   for right in range(len(arr)):
#       # expand: include arr[right] in the window
#       while <window is invalid>:
#           # shrink from the left until valid again
#           left += 1
#       # window [left, right] is now valid — update your answer here
#
# =============================================================================


# -----------------------------------------------------------------------------
# LC 643 — Maximum Average Subarray I (Easy) | NEW — Sliding Window (fixed)
# -----------------------------------------------------------------------------
# Given an array and integer k, find the contiguous subarray of length k
# that has the maximum average value.
#
# Example:
#   nums = [1,12,-5,-6,50,3], k = 4
#   Output: 12.75   (subarray [12,-5,-6,50], sum=51, 51/4=12.75)
#
# Hint: fixed window of size k. Keep a running window_sum.
#       Add the new element on the right, remove the element that fell
#       off the left, once the window reaches size k.
# -----------------------------------------------------------------------------

def find_max_average(nums, k):
    #build first window manually (First four)
    window_sum = sum(nums[:k]) #sums first four 
    maxavg = window_sum / k  #find max avg 

    for right in range(k, len(nums)): # increment window by one starting from k
        window_sum += nums[right] #subtracts the most right 
        window_sum -= nums[right - k] #subtracts the furthest left 
        maxavg = max(maxavg, window_sum / k )

def find_max_average2(nums, k):
    window_sum = sum(nums[:k])
    maxavg = window_sum / k

    for right in range(k, len(nums)):
        window_sum += nums[right] 
        window_sum -= nums[right - k]
        maxavg = max(maxavg, window_sum / k)

# -----------------------------------------------------------------------------
# LC 3 — Longest Substring Without Repeating Characters (Medium) | NEW — Sliding Window (variable)
# -----------------------------------------------------------------------------
# Find the length of the longest substring without repeating characters.
#
# Example:
#   s = "abcabcbb"
#   Output: 3   ("abc")
#
# Hint: variable window. Expand right. If s[right] is already in your
#       window (seen set), shrink from the left until the duplicate
#       is removed. Track the max window size as you go.
# -----------------------------------------------------------------------------

def length_of_longest_substring(s):
    seen = set()
    left = 0
    maxlen = 0 

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        maxlen = max(maxlen, right - left + 1)
    return maxlen 

# -----------------------------------------------------------------------------
# LC 1004 — Max Consecutive Ones III (Medium) | NEW — Sliding Window (variable)
# -----------------------------------------------------------------------------
# Given a binary array and integer k, return the max number of consecutive
# 1's if you can flip at most k zeros to 1's.
#
# Example:
#   nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#   Output: 6   (flip the two 0's at index 3,4 → [1,1,1,1,1,1,1,1,1,1,0])
#
# Hint: variable window. Track how many zeroes are currently in the window.
#       If zero count exceeds k, shrink from the left until it's back to k.
#       Track max window size at each step.
# -----------------------------------------------------------------------------

def longest_ones(nums, k):
    left = 0 
    zerocount = 0 
    maxlen = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zerocount += 1
        
        while zerocount > k:
            if nums[left] == 0:
                zerocount -= 1
            left += 1
        maxlen = max(maxlen, right - left + 1)
    return maxlen 


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


# LC 387 — First Unique Character
# pass 1: count frequencies. pass 2: return first index with count==1.
# Time: O(n) | Space: O(1)

def first_uniq_char_answer(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


# LC 128 — Longest Consecutive Sequence
# set for O(1) lookup. only count from sequence starts.
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


# LC 49 — Group Anagrams
# sorted word as dict key.
# Time: O(n * k log k) | Space: O(n * k)

def group_anagrams_answer(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


# --- SECTION 2 ANSWERS ---


# LC 26 — Remove Duplicates from Sorted Array
# slow tracks last unique value written. compare fast to nums[slow].
# Time: O(n) | Space: O(1)

def remove_duplicates_answer(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1


# LC 977 — Squares of a Sorted Array
# compare from both ends, fill result backward, largest squares first.
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


# LC 11 — Container With Most Water
# always move the shorter pointer inward — moving the taller one
# can only decrease or maintain the area, never improve it.
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


# LC 15 — 3Sum
# sort first. fix nums[i], then two-pointer the rest for pairs summing
# to -nums[i]. skip duplicate values to avoid duplicate triplets.
# Time: O(n^2) | Space: O(n) for sort

def three_sum_answer(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue   # skip duplicate "fixed" values

        if nums[i] > 0:
            break   # sorted array, can't sum to 0 with positives only from here

        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1   # skip duplicates
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1  # skip duplicates
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# --- SECTION 3 ANSWERS ---


# LC 643 — Maximum Average Subarray I
# fixed window of size k. maintain running sum, slide window by
# adding new right element and removing element that fell off the left.
# Time: O(n) | Space: O(1)

def find_max_average_answer(nums, k):
    window_sum = sum(nums[:k])
    max_avg = window_sum / k

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        max_avg = max(max_avg, window_sum / k)

    return max_avg


# LC 3 — Longest Substring Without Repeating Characters
# variable window. expand right, shrink left on duplicate, track max.
# Time: O(n) | Space: O(n)

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


# LC 1004 — Max Consecutive Ones III
# variable window. track zero count in window. shrink when zero count
# exceeds k. track max window size at each step.
# Time: O(n) | Space: O(1)

def longest_ones_answer(nums, k):
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