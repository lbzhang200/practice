# =============================================================================
# RANDOM MIX #2 — 20 more, spread across everything you've practiced
# (arrays/hashing, strings, two pointers, sliding window, stack, binary search)
# =============================================================================
# Shuffled order, unlabeled — figure out the pattern yourself.
# Answer key + explanations are below the scroll buffer.
# =============================================================================


def q1(nums):
    """
    Return True if any value appears at least twice in the array.
    Example: q1([1,2,3,1]) -> True
             q1([1,2,3,4]) -> False
    """
    pass


def q2(s, p):
    """
    Return True if s is a permutation of p (i.e. some substring
    of s is an anagram of p). Only need to return True/False.
    Example: q2("eidbaooo", "ab") -> True  (contains "ba")
             q2("eidboaoo", "ab") -> False
    """
    pass


def q3(nums):
    """
    Return the length of the longest run of consecutive integers
    (order doesn't matter in the input, and don't sort — O(n)).
    Example: q3([100,4,200,1,3,2]) -> 4  (the run is 1,2,3,4)
    """
    pass


def q4(nums):
    """
    Return the element that appears more than n/2 times.
    (Guaranteed to exist.) Try to do it in O(1) space.
    Example: q4([2,2,1,1,1,2,2]) -> 2
    """
    pass


def q5(nums, k):
    """
    Return the total number of subarrays whose elements sum to k.
    (Subarrays can be negative numbers too.)
    Example: q5([1,1,1], 2) -> 2
    """
    pass


def q6(prices):
    """
    You're given daily stock prices. Buy once, sell once (sell must
    be after buy). Return the max profit possible, or 0 if none.
    Example: q6([7,1,5,3,6,4]) -> 5  (buy at 1, sell at 6)
    """
    pass


def q7(nums):
    """
    Move all 0s in nums to the end, in place, while keeping the
    relative order of the non-zero elements. Return nothing
    (modify nums directly).
    Example: nums = [0,1,0,3,12] -> becomes [1,3,12,0,0]
    """
    pass


def q8(nums):
    """
    Dutch National Flag — nums has only 0s, 1s, and 2s. Sort it
    in place in one pass, O(1) extra space.
    Example: nums = [2,0,2,1,1,0] -> becomes [0,0,1,1,2,2]
    """
    pass


def q9(s):
    """
    Return the longest palindromic substring in s.
    Example: q9("babad") -> "bab" (or "aba", either is valid)
    """
    pass


def q10(board):
    """
    Return True if a 9x9 Sudoku board is valid so far (partially
    filled is fine — just check no row/col/3x3-box has a repeated
    digit among the filled cells). '.' means empty.
    """
    pass


def q11(strs):
    """
    Design an algorithm to encode a list of strings into a single
    string, and decode it back into the original list. Must handle
    strings containing any character, including delimiters you pick.
    Example: encode(["ab","cd"]) -> some string;
             decode(that string) -> ["ab","cd"]
    """
    pass


def q12(s, k):
    """
    You can replace up to k characters in s with any other
    character. Return the length of the longest substring you can
    make consisting of a single repeated character.
    Example: q12("ABAB", 2) -> 4  (replace both A's or both B's)
    """
    pass


class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the
    minimum element, all in O(1) time.
    Example: push(3), push(5), get_min() -> 3, push(1), get_min() -> 1,
             pop(), get_min() -> 3
    """
    def __init__(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def get_min(self):
        pass


def q13(tokens):
    """
    Evaluate a Reverse Polish Notation (postfix) expression.
    Tokens are numbers and operators (+, -, *, /). Integer division
    truncates toward zero.
    Example: q13(["2","1","+","3","*"]) -> 9  ((2+1)*3)
    """
    pass


def q14(position, speed, target):
    """
    Car Fleet — cars are driving toward `target` on a one-lane road.
    Each has a position and speed. A car catches up to a slower car
    ahead and they become one "fleet" (can't pass). Return the
    number of distinct fleets that arrive at the target.
    Example: q14([10,8,0,5,3], [2,4,1,1,3], 12) -> 3
    """
    pass


def q15(nums, target):
    """
    Search for target in a rotated sorted array (no duplicates).
    Return its index, or -1 if not found. Must be O(log n).
    Example: q15([4,5,6,7,0,1,2], 0) -> 4
    """
    pass


def q16(nums):
    """
    Find any peak element (an element strictly greater than both
    its neighbors) and return its index. Array edges count as
    -infinity neighbors. Must be O(log n).
    Example: q16([1,2,3,1]) -> 2  (index of the 3)
    """
    pass


class TimeMap:
    """
    Design a time-based key-value store. set(key, value, timestamp)
    stores a value at a given time. get(key, timestamp) returns the
    value set at the largest timestamp <= the given timestamp
    (or "" if none exists).
    """
    def __init__(self):
        pass

    def set(self, key, value, timestamp):
        pass

    def get(self, key, timestamp):
        pass


def q17(nums):
    """
    nums is sorted, but contains negative numbers. Return an array
    of the squares of each number, also sorted in non-decreasing
    order. Try to do it in O(n), not O(n log n).
    Example: q17([-4,-1,0,3,10]) -> [0,1,9,16,100]
    """
    pass


# =============================================================================
# =============================================================================
#
#                    ⬇ SCROLL BUFFER — DON'T PEEK EARLY ⬇
#
# =============================================================================
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
# ANSWER KEY + EXPLANATIONS
# =============================================================================

# --- q1: Contains Duplicate (Arrays & Hashing) -------------------------------
def q1_SOLUTION(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
# Pattern: set lookup is O(1) — one pass, no need to sort first.


# --- q2: Permutation in String (Sliding Window, fixed size) -----------------
def q2_SOLUTION(s, p):
    from collections import Counter
    if len(p) > len(s):
        return False
    need = Counter(p)
    window = Counter(s[:len(p)])
    if window == need:
        return True
    for i in range(len(p), len(s)):
        window[s[i]] += 1
        left_char = s[i - len(p)]
        window[left_char] -= 1
        if window[left_char] == 0:
            del window[left_char]
        if window == need:
            return True
    return False
# Pattern: fixed-size window (size len(p)) sliding across s,
# comparing the window's character counts to p's each step.


# --- q3: Longest Consecutive Sequence (Arrays & Hashing) ---------------------
def q3_SOLUTION(nums):
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num - 1 not in num_set:  # only start counting from run-starts
            length = 1
            while num + length in num_set:
                length += 1
            best = max(best, length)
    return best
# Pattern: set for O(1) lookup. Only start counting a run from its
# true start (no num-1 in the set) so each number is visited O(1)
# amortized times total, keeping it O(n) instead of O(n^2).


# --- q4: Majority Element (Boyer-Moore Voting) -------------------------------
def q4_SOLUTION(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
# Pattern: Boyer-Moore voting. The majority element "outvotes"
# everything else combined, so a running +1/-1 tally always
# survives with the majority element as the final candidate.


# --- q5: Subarray Sum Equals K (Prefix Sum + Hashing) ------------------------
def q5_SOLUTION(nums, k):
    from collections import defaultdict
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # empty prefix
    total = 0
    running_sum = 0
    for num in nums:
        running_sum += num
        total += prefix_counts[running_sum - k]  # NOT k - running_sum
        prefix_counts[running_sum] += 1
    return total
# Pattern: running_sum - k tells you "is there an earlier prefix
# that, if removed, leaves exactly k?" prefix_counts[0] = 1 handles
# subarrays that start at index 0. Order matters: check before you
# add the current running_sum to the map, or you'd count a subarray
# against itself.


# --- q6: Best Time to Buy and Sell Stock (Two Pointers / Greedy) ------------
def q6_SOLUTION(prices):
    min_price = float('inf')
    best_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        best_profit = max(best_profit, price - min_price)
    return best_profit
# Pattern: track the lowest price seen so far; at each day, check
# the profit if you sold today. One pass, O(1) space.


# --- q7: Move Zeroes (Two Pointers) ------------------------------------------
def q7_SOLUTION(nums):
    insert_pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
    # no return — modifies nums in place
# Pattern: insert_pos tracks where the next non-zero should land.
# Swapping (not just overwriting) keeps zeros shuffled to the back
# without needing extra space.


# --- q8: Sort Colors / Dutch National Flag (Three Pointers) -----------------
def q8_SOLUTION(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
            # NOTE: mid does NOT advance here — the swapped-in value
            # from the high end hasn't been checked yet
    # no return — modifies nums in place
# Pattern: three regions (low=0s, mid=unprocessed, high=2s) shrink
# toward each other in one pass. The 2-swap doesn't advance mid
# since the new value at mid is unverified.


# --- q9: Longest Palindromic Substring (Two Pointers, expand around center) -
def q9_SOLUTION(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # back off one, the match broke here

    best = ""
    for i in range(len(s)):
        odd = expand(i, i)        # odd-length palindromes, center = i
        even = expand(i, i + 1)   # even-length palindromes, center = i,i+1
        best = max(best, odd, even, key=len)
    return best
# Pattern: every palindrome has a center (one char for odd length,
# a gap between two chars for even length). Try every possible
# center, expand outward with two pointers while it stays a match.


# --- q10: Valid Sudoku (Arrays & Hashing) ------------------------------------
def q10_SOLUTION(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue
            box_id = (r // 3) * 3 + (c // 3)
            if val in rows[r] or val in cols[c] or val in boxes[box_id]:
                return False
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_id].add(val)
    return True
# Pattern: one set per row, column, and 3x3 box. box_id maps a
# (row, col) to which of the 9 boxes it belongs to. Check-then-add
# in a single pass catches any duplicate the moment it appears.


# --- q11: Encode and Decode Strings (Strings) --------------------------------
def encode(strs):
    return "".join(f"{len(s)}#{s}" for s in strs)

def decode(s):
    result = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        length = int(s[i:j])
        result.append(s[j + 1:j + 1 + length])
        i = j + 1 + length
    return result
# Pattern: length-prefix each string ("length#content") instead of
# using a delimiter character, since the strings themselves could
# contain any character, including whatever delimiter you'd pick.
# Decode by reading the length digits up to '#', then slicing
# exactly that many characters.


# --- q12: Longest Repeating Character Replacement (Sliding Window) ----------
def q12_SOLUTION(s, k):
    from collections import defaultdict
    count = defaultdict(int)
    left = 0
    max_freq = 0
    best = 0
    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        window_size = right - left + 1
        if window_size - max_freq > k:  # too many chars need replacing
            count[s[left]] -= 1
            left += 1
        else:
            best = max(best, window_size)
    return best
# Pattern: window is valid as long as (window size - most frequent
# char's count) <= k, i.e. you can replace everything else within
# your budget. max_freq is allowed to be "stale" (never decreases)
# without breaking correctness — the window just won't shrink below
# the best length already found, which is fine.


# --- MinStack: Min Stack (Stack design) --------------------------------------
class MinStack_SOLUTION:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # tracks the min at each corresponding depth

    def push(self, val):
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]
# Pattern: a second, parallel stack tracks "the min so far" at each
# depth. Popping both stacks together keeps get_min() correct after
# any pop, since the min_stack's top always reflects the current
# remaining elements — no rescanning needed.


# --- q13: Evaluate Reverse Polish Notation (Stack) ---------------------------
def q13_SOLUTION(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(token))
    return stack[0]
# Pattern: push numbers; on an operator, pop the two most recent
# operands (b first, then a — order matters for - and /), apply
# the op, push the result back. The final stack has exactly one
# value: the answer.


# --- q14: Car Fleet (Monotonic Stack) ----------------------------------------
def q14_SOLUTION(position, speed, target):
    cars = sorted(zip(position, speed), reverse=True)  # closest to target first
    stack = []
    for pos, spd in cars:
        time_to_target = (target - pos) / spd
        if not stack or time_to_target > stack[-1]:
            stack.append(time_to_target)  # new fleet, slower than the one ahead
        # else: catches up to the fleet ahead, merges — don't push
    return len(stack)
# Pattern: sort by position (closest to target first), compute each
# car's solo arrival time. If a car behind would arrive later than
# the fleet in front of it, it's stuck behind (merges, doesn't form
# a new fleet) — only push a new "fleet time" when it's slower than
# every fleet ahead of it so far, which is what the stack tracks.


# --- q15: Search in Rotated Sorted Array (Binary Search) --------------------
def q15_SOLUTION(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:  # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
# Pattern: at every mid, one half (left-to-mid or mid-to-right) is
# guaranteed fully sorted. Check which half is sorted, then check
# if target falls in that half's range — if so, search there,
# otherwise search the other half.


# --- q16: Find Peak Element (Binary Search) ----------------------------------
def q16_SOLUTION(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid       # peak is at mid or to the left
        else:
            left = mid + 1    # peak is to the right
    return left
# Pattern: if nums[mid] < nums[mid+1], you're on an upward slope,
# so a peak must exist somewhere to the right (the array "runs out
# of room to keep climbing" eventually). If nums[mid] > nums[mid+1],
# mid could BE a peak, so keep it in range with right = mid.


# --- TimeMap: Time Based Key-Value Store (Binary Search + Hashing) ----------
class TimeMap_SOLUTION:
    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value), timestamps increasing

    def set(self, key, value, timestamp):
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        entries = self.store[key]
        left, right = 0, len(entries) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if entries[mid][0] <= timestamp:
                result = entries[mid][1]  # valid candidate, look for a later one
                left = mid + 1
            else:
                right = mid - 1
        return result
# Pattern: set() calls arrive with increasing timestamps, so each
# key's list is naturally sorted — binary search for the largest
# timestamp <= the query, updating `result` every time you find a
# valid (but possibly not optimal) candidate, same shape as the
# classic "search on answer" binary search.


# --- q17: Squares of a Sorted Array (Two Pointers) ---------------------------
def q17_SOLUTION(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    for i in range(n - 1, -1, -1):  # fill result from the back
        if abs(nums[left]) > abs(nums[right]):
            result[i] = nums[left] ** 2
            left += 1
        else:
            result[i] = nums[right] ** 2
            right -= 1
    return result
# Pattern: the largest square is always at one of the two ends
# (biggest positive or most-negative value), never in the middle.
# Two pointers from both ends, filling the output array from the
# back forward, always placing the bigger square next.

# =============================================================================
# END OF FILE
# =============================================================================