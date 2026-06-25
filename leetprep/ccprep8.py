# =============================================================================
# SLIDING WINDOW PRACTICE + STACKS INTRO & PROBLEM SET
# =============================================================================
# Two topics in one file. Work through sliding window first, then stacks.
# Answer key at the bottom for both sections.
# =============================================================================


# =============================================================================
# PART 1 — SLIDING WINDOW
# =============================================================================
#
# RECAP OF THE TWO TEMPLATES:
#
# FIXED WINDOW (size k never changes):
# ─────────────────────────────────────
#   window_sum = sum(nums[:k])       ← seed the first window
#   for right in range(k, len(nums)):
#       window_sum += nums[right]        ← add incoming element
#       window_sum -= nums[right - k]    ← remove outgoing element
#       # update answer here
#
# VARIABLE WINDOW (grows/shrinks based on condition):
# ─────────────────────────────────────────────────────
#   left = 0
#   for right in range(len(arr)):
#       # include arr[right] — update your tracker
#       while <window is invalid>:
#           # remove arr[left] from tracker
#           left += 1
#       # window [left, right] is valid — update answer
#
# SIGNAL WORDS:
#   fixed   → "subarray of length k", "k consecutive elements"
#   variable → "longest", "shortest", "at most k", "without repeating"
#
# =============================================================================


# -----------------------------------------------------------------------------
# SW1. LC 643 — Maximum Average Subarray (Easy) | FIXED WINDOW
# -----------------------------------------------------------------------------
# Find the contiguous subarray of length k with the maximum average.
#
# Example:
#   nums = [1,12,-5,-6,50,3], k = 4
#   Output: 12.75
# -----------------------------------------------------------------------------

def max_average(nums, k):
    window_sum = sum(nums[:k]) #sum of current window
    maxavg = window_sum / k
    for right in range(k, len(nums)):
        window_sum += nums[right] #rightmost 
        window_sum -= nums[right - k] #subtract leftmost 
        maxavg = max(maxavg, window_sum / k)
    
    return maxavg

def max_average(nums, k):
    window_sum = sum(nums[:k])
    maxavg = window_sum / k
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        maxavg = max(maxavg, window_sum / k)

    return maxavg 

# -----------------------------------------------------------------------------
# SW2. LC 3 — Longest Substring Without Repeating Characters (Medium) | VARIABLE
# -----------------------------------------------------------------------------
# Find the length of the longest substring with no repeating characters.
#
# Example:
#   s = "abcabcbb"
#   Output: 3
# -----------------------------------------------------------------------------

def longest_unique_substring(s):
    seen = set()
    left = 0 
    maxlen = 0
    for right in range (len(s)):
        while s[right] in seen: #if duplicate?
            seen.remove(s[left]) #then shrink left until find duplicate 
            left += 1 
        seen.add(s[right]) #add element now that the window is valid 
        maxlen = max(maxlen, right - left + 1)
    return maxlen 

def longest_uniqe_substring2(s):
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
# SW3. LC 1004 — Max Consecutive Ones III (Medium) | VARIABLE
# -----------------------------------------------------------------------------
# Given a binary array and k, return the max consecutive 1's if you can
# flip at most k zeroes.
#
# Example:
#   nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
#   Output: 6
# -----------------------------------------------------------------------------

def max_consecutive_ones(nums, k):
    left = 0 
    zerocount = 0
    maxlen = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zerocount += 1
        while zerocount > k:
            if nums[left] == 0: #if left is zero 
                zerocount -= 1 #subtract the zero count 
            left += 1  #increment up by one 
        maxlen = max(maxlen, right - left + 1)
    
    return maxlen 

def max_consecutive_ones(nums, k):
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
    
# -----------------------------------------------------------------------------
# SW4. LC 438 — Find All Anagrams in a String (Medium) | FIXED WINDOW
# -----------------------------------------------------------------------------
# Return all start indices of p's anagrams in s.
#
# Example:
#   s = "cbaebabacd", p = "abc"
#   Output: [0, 6]
#
# Hint: fixed window of size len(p). maintain frequency dict for the
#       current window. add new char, remove old char as window slides.
#       when window freq == p freq, record the start index.
# -----------------------------------------------------------------------------

def find_anagrams(s, p):
    pcount = {}
    for letter in p:
        pcount = pcount.get(letter, 0) + 1
    startindex = 0 
    for right in range(len(s)):
        while s[right] in pcount:
            pcount.remove(s[left])
            left += 1 
        #ts too hard


# -----------------------------------------------------------------------------
# SW5. LC 209 — Minimum Size Subarray Sum (Medium) | VARIABLE
# -----------------------------------------------------------------------------
# Given an array of positive integers and target, return the minimum length
# subarray whose sum is >= target. Return 0 if no such subarray exists.
#
# Example:
#   nums = [2,3,1,2,4,3], target = 7
#   Output: 2   (subarray [4,3])
#
# Hint: variable window. expand right, add to window_sum. when window_sum
#       >= target, record the window size and shrink from the left to see
#       if you can find something smaller. keep shrinking until invalid again.
# -----------------------------------------------------------------------------

def min_subarray_len(target, nums):
    window_sum = 0 
    length = 0 
    left = 0
    minlen = float('inf')
    for right in range(len(nums)):
        windowsum += nums[right]
        while windowsum >= target:
            minlen = min(minlen, right - left + 1)
            windowsum -= nums[left]
            left += 1
    return 0 if minlen == float('inf') else minlen

# =============================================================================
# PART 2 — STACKS
# =============================================================================
#
# WHAT IS A STACK?
# ─────────────────────────────────────────────────────────────────────────────
# A stack is a collection where you can only add or remove from ONE end
# — the top. Think of a stack of plates: you put new plates on top and
# take plates from the top. You never pull from the middle or bottom.
#
# The rule is called LIFO: Last In, First Out.
# Whatever you added most recently is the first thing you take back out.
#
# In Python, a regular list works perfectly as a stack:
#   stack = []
#   stack.append(x)   # push — add to top
#   stack.pop()       # pop  — remove from top
#   stack[-1]         # peek — look at top without removing
#   len(stack) == 0   # check if empty
#
# All four operations are O(1).
#
# ─────────────────────────────────────────────────────────────────────────────
# WHEN TO USE A STACK
# ─────────────────────────────────────────────────────────────────────────────
# Ask yourself: "do I need to remember what came BEFORE and undo/use it
# when I encounter something specific later?"
#
# That "remember and revisit in reverse order" property is stacks.
#
# The most common patterns:
#
# 1. MATCHING / VALIDITY
#    "does every opening thing have a matching closing thing?"
#    → push opening brackets, pop when you see the matching close
#    → example: Valid Parentheses
#
# 2. MONOTONIC STACK — "what's the next bigger/smaller thing?"
#    "for each element, find the next element that is greater/less than it"
#    → push elements, and pop when you find something that beats them
#    → example: Daily Temperatures, Next Greater Element
#
# 3. UNDO / BACKTRACK
#    "simulate a process where you might need to go back"
#    → push each state, pop to go back
#    → example: Backspace String Compare
#
# SIGNAL WORDS:
#    "matching brackets/parentheses", "valid", "next greater",
#    "previous smaller", "undo", "backspace", "evaluate expression"
#
# ─────────────────────────────────────────────────────────────────────────────
# THE MONOTONIC STACK — most important pattern to understand
# ─────────────────────────────────────────────────────────────────────────────
# "Monotonic" just means the stack stays sorted (either always increasing
# or always decreasing) as you build it.
#
# Template for "next greater element":
#
#   stack = []   ← stores indices of elements waiting for their answer
#   result = [-1] * len(nums)   ← default: no greater element found
#
#   for i in range(len(nums)):
#       while stack and nums[i] > nums[stack[-1]]:
#           idx = stack.pop()
#           result[idx] = nums[i]   ← nums[i] is the next greater for idx
#       stack.append(i)
#
# Read it in plain English:
# "As I scan, if the current element is bigger than what's sitting on
# top of the stack, the current element IS the 'next greater' answer
# for whatever's on top. Pop it and record the answer. Keep popping
# until the stack top is bigger than me, then push myself."
#
# =============================================================================


# -----------------------------------------------------------------------------
# S1. LC 20 — Valid Parentheses (Easy) | STACK — matching
# -----------------------------------------------------------------------------
# Given a string of brackets, return true if it is valid. Every opening
# bracket must be closed by the same type in the correct order.
#
# Example:
#   s = "()"       Output: True
#   s = "()[]{}"   Output: True
#   s = "(]"       Output: False
#   s = "([)]"     Output: False
#
# Hint: push opening brackets onto the stack. when you see a closing
#       bracket, check if the top of the stack is the matching opener.
#       if it is, pop it. if not (or stack is empty), return False.
#       at the end, the stack should be empty if everything matched.
# -----------------------------------------------------------------------------

def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False 
            stack.pop()
    return len(stack) ==0 

def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False 
            stack.pop()
    return len(stack) == 0 


# -----------------------------------------------------------------------------
# S2. LC 844 — Backspace String Compare (Easy) | STACK — simulate
# -----------------------------------------------------------------------------
# Given two strings s and t where '#' means backspace, return true if
# they are equal after processing all the backspaces.
#
# Example:
#   s = "ab#c", t = "ad#c"
#   Output: True   ("ac" == "ac")
#
#   s = "ab##", t = "c#d#"
#   Output: True   ("" == "")
#
# Hint: simulate a text editor. push regular chars, pop on '#'.
#       build the final string for each, then compare.
# -----------------------------------------------------------------------------

def backspace_compare(s, t):
    string1 = ""
    string2 = ""

    stack = []
    for letter in s:
        if letter != '#':
            stack.append(letter)
        else:
            stack.pop()
    


# -----------------------------------------------------------------------------
# S3. LC 739 — Daily Temperatures (Medium) | STACK — monotonic
# -----------------------------------------------------------------------------
# Given an array of daily temperatures, return an array where result[i]
# is the number of days until a warmer temperature. If no warmer day
# exists, result[i] = 0.
#
# Example:
#   temps = [73,74,75,71,69,72,76,73]
#   Output: [1,1,4,2,1,1,0,0]
#
# Hint: monotonic stack storing INDICES. for each temp, while the current
#       temp is warmer than the temp at stack[-1], pop and record the
#       distance (i - popped_index). push the current index.
# -----------------------------------------------------------------------------

def daily_temperatures(temps):
    pass


# -----------------------------------------------------------------------------
# S4. LC 496 — Next Greater Element I (Easy) | STACK — monotonic
# -----------------------------------------------------------------------------
# nums1 is a subset of nums2. For each element in nums1, find the next
# greater element in nums2. Return -1 if none exists.
#
# Example:
#   nums1 = [4,1,2], nums2 = [1,3,4,2]
#   Output: [-1,3,-1]
#   (4 has no greater in nums2, 1's next greater in nums2 is 3, 2 has none)
#
# Hint: run a monotonic stack on nums2 first to build a dict mapping
#       each value → its next greater element in nums2.
#       then just look up each nums1 value in that dict.
# -----------------------------------------------------------------------------

def next_greater_element(nums1, nums2):
    pass


# -----------------------------------------------------------------------------
# S5. LC 150 — Evaluate Reverse Polish Notation (Medium) | STACK — evaluate
# -----------------------------------------------------------------------------
# Evaluate an expression in Reverse Polish Notation (postfix).
# Operators come AFTER their operands.
#
# Example:
#   tokens = ["2","1","+","3","*"]
#   Output: 9    ((2+1)*3 = 9)
#
#   tokens = ["4","13","5","/","+"]
#   Output: 6    (4 + (13/5) = 4+2 = 6)
#
# Hint: push numbers onto the stack. when you see an operator (+,-,*,/),
#       pop the top TWO numbers, apply the operator, push the result back.
#       the final answer is the one remaining value on the stack.
#       note: for division, use int(a/b) not a//b to handle negatives correctly.
# -----------------------------------------------------------------------------

def eval_rpn(tokens):
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


# =============================================================================
# SLIDING WINDOW ANSWERS
# =============================================================================


# SW1. Maximum Average Subarray — FIXED WINDOW
# seed first window, then slide by adding new and removing old element.
# Time: O(n) | Space: O(1)

def max_average_answer(nums, k):
    window_sum = sum(nums[:k])
    max_avg = window_sum / k
    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right - k]
        max_avg = max(max_avg, window_sum / k)
    return max_avg


# SW2. Longest Substring Without Repeating Characters — VARIABLE WINDOW
# seen set tracks what's in current window. expand right, shrink left
# when duplicate found, track max window size.
# Time: O(n) | Space: O(n)

def longest_unique_substring_answer(s):
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


# SW3. Max Consecutive Ones III — VARIABLE WINDOW
# zero_count tracks zeroes in window. shrink when zero_count > k.
# only decrement zero_count when an actual zero leaves the window.
# Time: O(n) | Space: O(1)

def max_consecutive_ones_answer(nums, k):
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


# SW4. Find All Anagrams in a String — FIXED WINDOW
# fixed window of size len(p). maintain freq dict for current window.
# when window_freq == p_freq, record start index i - len(p) + 1.
# Time: O(n) | Space: O(1) — at most 26 keys

def find_anagrams_answer(s, p):
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


# SW5. Minimum Size Subarray Sum — VARIABLE WINDOW
# expand right, add to window_sum. when window_sum >= target, record size
# and shrink left as far as possible while still meeting target.
# Time: O(n) | Space: O(1)

def min_subarray_len_answer(target, nums):
    left = 0
    window_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return 0 if min_len == float('inf') else min_len


# =============================================================================
# STACK ANSWERS
# =============================================================================


# S1. Valid Parentheses — STACK (matching)
# push openers. on closer, check top of stack for match. pop if match.
# return False on mismatch or empty stack. at end, stack must be empty.
# Time: O(n) | Space: O(n)

def is_valid_answer(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in '({[':
            stack.append(c)
        else:
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    return len(stack) == 0


# S2. Backspace String Compare — STACK (simulate)
# build each string by pushing chars and popping on '#'.
# compare the resulting stacks.
# Time: O(n) | Space: O(n)

def backspace_compare_answer(s, t):
    def build(string):
        stack = []
        for c in string:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()
        return stack

    return build(s) == build(t)


# S3. Daily Temperatures — STACK (monotonic, stores indices)
# stack stores indices of days waiting for a warmer day.
# when current temp > temp at stack top, pop and record distance.
# Time: O(n) | Space: O(n)

def daily_temperatures_answer(temps):
    stack = []
    result = [0] * len(temps)
    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


# S4. Next Greater Element I — STACK (monotonic on nums2, then lookup)
# build a map of value → next greater using monotonic stack on nums2.
# then look up each nums1 value in the map.
# Time: O(n + m) | Space: O(n)

def next_greater_element_answer(nums1, nums2):
    stack = []
    next_greater = {}
    for n in nums2:
        while stack and n > stack[-1]:
            next_greater[stack.pop()] = n
        stack.append(n)
    return [next_greater.get(n, -1) for n in nums1]


# S5. Evaluate Reverse Polish Notation — STACK (evaluate)
# push numbers. on operator, pop two, apply, push result.
# use int(a/b) not a//b — handles negative division correctly in Python.
# Time: O(n) | Space: O(n)

def eval_rpn_answer(tokens):
    stack = []
    for token in tokens:
        if token not in '+-*/':
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
    return stack[0]