# =============================================================================
# DSA PATTERN RECOGNITION — 20 QUESTIONS
# Patterns: Hashing | Two Pointers | Sliding Window | Stack | Strings
# =============================================================================


# 1. Given a sorted array, find two numbers that add up to a target.
#    Example: nums = [2, 7, 11, 15], target = 9 → [0, 1]
def q1(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[n], i]
        seen[n] = i

# 2. Given a string, find the longest substring without repeating characters.
#    Example: s = "abcabcbb" → 3  ("abc")
def q2(s):
    seen = set()
    best = 0 
    left = 0
    for right in range(len(s)):
        while s[right] in seen: # if there is a duplicate 
            seen.remove(s[left]) #shrink 
            left += 1
        seen.add(s[left])
        best = max(best, right - left + 1)

# 3. Given an array, return true if any value appears at least twice.
#    Example: nums = [1, 2, 3, 1] → True
def q3(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True 
        seen.add(n)
    return False 

# 4. Given a string, check if it reads the same forwards and backwards.
#    Example: s = "racecar" → True
def q4(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[right] != s[left]:
            return False
        else:
            left += 1
            right -= 1
    return True 



# 5. Given an array of temperatures, find how many days until a warmer one.
#    Example: temps = [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
def q5(temps):
    stack = []
    result = []
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop() #weather day 
            result[idx] = i - idx #today minus the weather day 
        stack.append(i)
    return result  


# 6. Given a string of brackets, check if it's valid.
#    Example: s = "{[]}" → True  |  s = "([)]" → False
def q6(s):
    pass #another time  


# 7. Given an array and k, find the maximum sum subarray of size k.
#    Example: nums = [2,1,5,1,3,2], k = 3 → 9  (5+1+3)
def q7(nums, k):
    window_sum = sum(nums[:k])
    maxavg = window_sum / k
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        maxavg = max(maxavg, window_sum / k)
    return maxavg


# 8. Given two strings, check if one is an anagram of the other.
#    Example: s = "anagram", t = "nagaram" → True
def q8(s, t):
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    for letter in t:
        count[letter] = count.get(letter, 0) - 1
        if count[letter] < 0:
            return False 
    return True 


# 9. Given an array, find the next greater element for each number.
#    Example: nums = [2,1,2,4,3] → [4,2,4,-1,-1]
def q9(nums):
     


# 10. Given a string, find the minimum window substring that contains
#     all characters of another string t.
#     Example: s = "ADOBECODEBANC", t = "ABC" → "BANC"
def q10(s, t):
    pass


# 11. Given a sorted array, remove duplicates in place and return new length.
#     Example: nums = [1,1,2,3,3] → 3  (array becomes [1,2,3,...])
def q11(nums):
    pass


# 12. Given an array of integers, return the k most frequent elements.
#     Example: nums = [1,1,1,2,2,3], k = 2 → [1, 2]
def q12(nums, k):
    pass


# 13. Given a string, find the longest palindromic substring.
#     Example: s = "babad" → "bab"
def q13(s):
    pass


# 14. Given an array, find all unique pairs that sum to zero.
#     Example: nums = [-3,-1,0,1,2,3] → [(-3,3), (-1,1)]
def q14(nums):
    pass


# 15. Given a string of brackets, check if you can empty it by
#     removing valid adjacent pairs.
#     Example: s = "abbaca" → True  (remove bb → "aaca" → remove aa → "ca"... )
#     Wait, this one uses any matching adjacent pair, not just brackets.
#     Example: s = "abba" → True  |  s = "abbc" → False
def q15(s):
    pass


# 16. Given an array of positive integers and a target, find the
#     minimum length subarray with sum >= target. Return 0 if none.
#     Example: target = 7, nums = [2,3,1,2,4,3] → 2  ([4,3])
def q16(target, nums):
    pass


# 17. Given a list of words, group all anagrams together.
#     Example: words = ["eat","tea","tan","ate","nat","bat"]
#              → [["eat","tea","ate"], ["tan","nat"], ["bat"]]
def q17(words):
    pass


# 18. Given an array, find the length of the longest subarray
#     with at most k distinct values.
#     Example: nums = [1,2,1,2,3], k = 2 → 4  ([1,2,1,2])
def q18(nums, k):
    pass


# 19. Given asteroids as integers, find which survive after collisions.
#     Positive moves right, negative moves left. Same direction = no collision.
#     Example: asteroids = [5,10,-5] → [5,10]  (-5 gets destroyed by 10)
def q19(asteroids):
    pass


# 20. Given two strings, check if they're equal after processing
#     backspaces (# means backspace).
#     Example: s = "ab#c", t = "ad#c" → True  (both become "ac")
def q20(s, t):
    pass


# =============================================================================
# ANSWER KEY — don't peek!
# =============================================================================


def q1_ans(nums, target):
    # Two pointers — sorted array + pair sum
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1
    return []


def q2_ans(s):
    # Sliding window — longest substring, no repeats
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best


def q3_ans(nums):
    # Hashing — fast duplicate lookup
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


def q4_ans(s):
    # Two pointers — compare from both ends
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def q5_ans(temps):
    # Stack — monotonic stack for next greater element
    stack = []
    result = [0] * len(temps)
    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


def q6_ans(s):
    # Stack — push openers, match closers
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    return len(stack) == 0


def q7_ans(nums, k):
    # Sliding window — fixed size window
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)
    return best


def q8_ans(s, t):
    # Hashing — compare character frequency counts
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count:
            return False
        count[c] -= 1
        if count[c] < 0:
            return False
    return True


def q9_ans(nums):
    # Stack — same monotonic stack pattern as daily temperatures
    stack = []
    result = [-1] * len(nums)
    for i, n in enumerate(nums):
        while stack and n > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = n
        stack.append(i)
    return result


def q10_ans(s, t):
    # Sliding window — minimum window containing all chars
    from collections import Counter
    need = Counter(t)
    have = {}
    formed = 0
    required = len(need)
    left = 0
    best = float('inf')
    best_window = ""
    for right in range(len(s)):
        c = s[right]
        have[c] = have.get(c, 0) + 1
        if c in need and have[c] == need[c]:
            formed += 1
        while formed == required:
            if right - left + 1 < best:
                best = right - left + 1
                best_window = s[left:right + 1]
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    return best_window


def q11_ans(nums):
    # Two pointers — slow tracks unique position, fast scans ahead
    if not nums:
        return 0
    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1


def q12_ans(nums, k):
    # Hashing + bucket sort by frequency
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for n, freq in count.items():
        buckets[freq].append(n)
    result = []
    for freq in range(len(nums) - 1, -1, -1):
        for n in buckets[freq]:
            result.append(n)
            if len(result) >= k:
                return result
    return result


def q13_ans(s):
    # Two pointers — expand outward from each center
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    best = ""
    for i in range(len(s)):
        odd = expand(i, i)
        even = expand(i, i + 1)
        if len(odd) > len(best):
            best = odd
        if len(even) > len(best):
            best = even
    return best


def q14_ans(nums):
    # Hashing — check if negation exists in set
    seen = set()
    result = set()
    for n in nums:
        if -n in seen:
            result.add(tuple(sorted((n, -n))))
        seen.add(n)
    return list(result)


def q15_ans(s):
    # Stack — push, pop when top matches current char
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


def q16_ans(target, nums):
    # Sliding window — variable window, shrink when valid
    window_sum = 0
    left = 0
    best = float('inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return best if best != float('inf') else 0


def q17_ans(words):
    # Hashing — sorted word as key, group matches
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        groups[key] = groups.get(key, []) + [word]
    return list(groups.values())


def q18_ans(nums, k):
    # Sliding window — track distinct count with a map
    count = {}
    left = 0
    best = 0
    for right in range(len(nums)):
        count[nums[right]] = count.get(nums[right], 0) + 1
        while len(count) > k:
            count[nums[left]] -= 1
            if count[nums[left]] == 0:
                del count[nums[left]]
            left += 1
        best = max(best, right - left + 1)
    return best


def q19_ans(asteroids):
    # Stack — pop when right-moving asteroid gets destroyed
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            if stack[-1] < -a:
                stack.pop()
                continue
            elif stack[-1] == -a:
                stack.pop()
            break
        else:
            stack.append(a)
    return stack


def q20_ans(s, t):
    # Stack — build final string by processing backspaces
    def process(string):
        stack = []
        for c in string:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return stack
    return process(s) == process(t)