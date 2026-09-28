# =============================================================================
# FULL REFRESHER — Arrays/Hashing, Strings, Two Pointers, Sliding Window,
#                   Stack (incl. monotonic), Binary Search (incl. search-on-answer)
# =============================================================================
# Instructions:
#   - Work top to bottom. Each problem has a `pass` stub.
#   - Don't scroll to the answer key until you've attempted it.
#   - Answer key has full solutions + explanations, separated by a scroll buffer.
#   - Reminders are embedded in the docstrings for your known trouble spots.
# =============================================================================


# =============================================================================
# SECTION 1 — ARRAYS & HASHING
# =============================================================================

def two_sum(nums, target):
    """
    Return indices of the two numbers that add up to target.
    Reminder: use a dict for O(n) — store {value: index} as you go,
    check if (target - num) has been seen already.
    Example: two_sum([2,7,11,15], 9) -> [0,1]
    """

    seen = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in seen:
            return [seen[comp], i]
        seen[n] = i
    return []


def group_anagrams(strs):
    """
    Group strings that are anagrams of each other.
    Reminder: sorted(word) as the dict key groups anagrams together.
    Example: ["eat","tea","tan","ate","nat","bat"]
      -> [["eat","tea","ate"],["tan","nat"],["bat"]]
    """
    groups = {}
    for words in strs:
        key = "".join(sorted(strs))
        if key not in groups:
            groups[key] = []
        groups[key].append(words)
    return (list(groups.values()))


def product_except_self(nums):
    """
    Return array where output[i] = product of all nums except nums[i].
    No division allowed. O(1) extra space (excluding output array).
    Reminder: prefix pass left->right, then suffix pass right->left,
    multiplying into the same output array.
    Example: [1,2,3,4] -> [24,12,8,6]
    """

    result = [1] * len(nums)
    suffix = 1
    prefix = 1

    for i in range(len(nums)):
        result[i] = result[i] * prefix
        prefix = prefix * nums[i]

    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * suffix
        suffix = suffix * nums[i]

def top_k_frequent(nums, k):
    """
    Return the k most frequent elements.
    Reminder: Counter + sort, or bucket sort for O(n).
    Example: top_k_frequent([1,1,1,2,2,3], 2) -> [1,2]
    """

    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    buckets = [[]for _ in range(len(nums+1))]

    for num, freq in count.items():
        buckets[freq].append(num) #append depending on frequency

    result = []
    for freq in range(len(buckets) - 1, -1, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result

# =============================================================================
# SECTION 2 — STRINGS
# =============================================================================

def is_isomorphic(s, t):
    """
    Two strings are isomorphic if characters in s can be replaced to get t,
    with a consistent one-to-one mapping in BOTH directions.
    Reminder: you need TWO dicts (s->t and t->s) to enforce the mapping
    is one-to-one, not just one-to-many.
    Example: is_isomorphic("egg", "add") -> True
             is_isomorphic("foo", "bar") -> False
    """

    s_to_t = {}
    t_to_s = {}
    for sc, tc in zip(s, t):
        if sc in s_to_t and s_to_t[sc] != tc:
            return False
        if tc in t_to_s and t_to_s[tc] != sc:
            return False
        s_to_t[sc] = tc
        t_to_s[tc] = sc
    return True


def ransom_note(ransom_note_str, magazine):
    """
    Return True if ransom_note_str can be built from letters in magazine
    (each letter in magazine used at most once).
    Reminder: frequency count on magazine, decrement as you use letters.
    Example: ransom_note("aa", "aab") -> True
    """

    count = {}
    for letter in magazine:
        count[letter] = count.get(letter, 0) + 1
    for letter in ransom_note_str:
        count[letter] = count.get(letter, 0) - 1
        if count[letter] < 0:
            return False
    return True

def first_unique_char(s):
    """
    Return the index of the first non-repeating character, or -1.
    Reminder: two passes — build frequency map, then scan again for
    the first count == 1.
    Example: first_unique_char("leetcode") -> 0
    """
    count = {}
    for word in s:
        count[word] = count.get(word, 0) + 1
    for i, n in enumerate(s):
        if count[n] == 1:
            return i
    return -1
# =============================================================================
# SECTION 3 — TWO POINTERS
# =============================================================================

def is_palindrome(s):
    """
    Check if s is a palindrome, ignoring non-alphanumeric chars and case.
    Reminder: left/right pointers moving inward, skip non-alphanumeric.
    Example: is_palindrome("A man, a plan, a canal: Panama") -> True
    """
    left, right = 0, len(s) - 1
    while left < right:
        if left < right and not s[left].isalnum():
            left += 1
        if left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def max_area(height):
    """
    Container With Most Water — given heights, find two lines that
    together with the x-axis form the container with the most water.
    Reminder: start pointers at both ends, always move the SHORTER
    line inward (moving the taller one can only hurt you).
    Example: max_area([1,8,6,2,5,4,8,3,7]) -> 49
    """

    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left] , height[right])
        best = max(best, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


def three_sum(nums):
    """
    Return all unique triplets that sum to 0.
    Reminder: sort first, fix one number, two-pointer on the rest.
    Skip duplicates for both the fixed number and the two pointers.
    Example: three_sum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]
    """

    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i + 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result



# =============================================================================
# SECTION 4 — SLIDING WINDOW
# =============================================================================

def length_of_longest_substring(s):
    """
    Length of the longest substring without repeating characters.
    Reminder: seen = set() NOT {} — this is your most common bug.
    Shrink from the left while the new char is already in the window.
    Example: length_of_longest_substring("abcabcbb") -> 3
    """
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        best = max(best, right - left + 1)
        seen.add(s[right])
    return best

def min_window_substring(s, t):
    """
    Minimum Window Substring — smallest substring of s containing
    all characters of t (with matching frequency).
    Reminder: expand right until valid, then shrink left while still
    valid, tracking the best window seen. min_len = float('inf'),
    not 0, so any real window beats the initial value.
    Example: min_window_substring("ADOBECODEBANC", "ABC") -> "BANC"
    """




def max_sum_subarray_k(nums, k):
    """
    Fixed-size sliding window: max sum of any subarray of length k.
    Reminder: compute the first window sum, then slide by
    subtracting the outgoing element and adding the incoming one.
    Example: max_sum_subarray_k([2,1,5,1,3,2], 3) -> 9
    """
    current_sum = sum(nums[:k])
    best = current_sum
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k]
        best = max(best, current_sum)
    return best

# =============================================================================
# SECTION 5 — STACK (incl. monotonic stack)
# =============================================================================

def is_valid_parens(s):
    """
    Valid Parentheses — check brackets are matched and properly nested.
    Reminder: push opens; on a close, check `elif stack:` before
    popping, or you'll crash on an empty stack.
    Example: is_valid_parens("()[]{}") -> True
             is_valid_parens("(]") -> False
    """

    stack = []
    things = {'}': '{', ')': '(', ']': '['}

    for ch in s:
        if ch in things.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != things[ch]:
                return False
            stack.pop()
    return True


def daily_temperatures(temperatures):
    """
    For each day, how many days until a warmer temperature? 0 if never.
    Reminder: monotonic decreasing stack of INDICES, not temperatures.
    Pop while the current temp is greater than temps[stack top].
    Example: daily_temperatures([73,74,75,71,69,72,76,73])
      -> [1,1,4,2,1,1,0,0]
    """
    stack = []
    n = len(temperatures)
    result = [0] * n

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev = stack.pop()
            result[prev] = i - prev
        stack.append(i)
    return result


def backspace_compare(s, t):
    """
    Compare two strings typed into an empty text editor, where '#'
    is a backspace. Return True if they end up equal.
    Reminder: build each result with a stack; guard pop with
    `elif stack:` for the '#' case.
    Example: backspace_compare("ab#c", "ad#c") -> True
    """
    pass




# =============================================================================
# SECTION 6 — BINARY SEARCH (classic + search-on-answer)
# =============================================================================

def binary_search(nums, target):
    """
    Classic binary search on a sorted array. Return index or -1.
    Reminder: while left <= right (not <), and right = mid - 1
    on the "too high" branch (not right = mid). Don't forget the
    final return -1 if the loop exits without finding target.
    Example: binary_search([-1,0,3,5,9,12], 9) -> 4
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left += 1
        else:
            right -= 1
    return -1


def find_min_rotated(nums):
    """
    Find the minimum element in a rotated sorted array (no duplicates).
    Reminder: compare nums[mid] to nums[right] to decide which half
    is unsorted / contains the minimum.
    Example: find_min_rotated([4,5,6,7,0,1,2]) -> 0
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


def koko_eating_bananas(piles, h):
    """
    Search-on-answer pattern. Find the minimum eating speed k such
    that Koko can finish all piles within h hours.
    Reminder: binary search over the ANSWER (possible speeds), not
    the array. left = 1, right = max(piles). while left < right.
    "Can Koko finish at speed k?" is the monotonic yes/no check.
    Example: koko_eating_bananas([3,6,7,11], 8) -> 4
    """



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

# --- SECTION 1: ARRAYS & HASHING -------------------------------------------

def two_sum_SOLUTION(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
# Explanation: one pass. For each num, check if its complement was
# already seen. If not, record num's index for future lookups. O(n).


def group_anagrams_SOLUTION(strs):
    groups = {}
    for word in strs:
        key = "".join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())
# Explanation: anagrams share the same sorted letters, so the sorted
# string is a natural bucket key. O(n * k log k) where k = word length.


def product_except_self_SOLUTION(nums):
    n = len(nums)
    output = [1] * n
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]
    return output
# Explanation: output[i] should be (product of everything left of i)
# times (product of everything right of i). First pass fills in the
# left products, second pass multiplies in the right products.


def top_k_frequent_SOLUTION(nums, k):
    from collections import Counter
    counts = Counter(nums)
    return [num for num, _ in counts.most_common(k)]
# Explanation: Counter.most_common(k) is the O(n log k) shortcut.
# For true O(n), use bucket sort: buckets indexed by frequency,
# then walk buckets from highest frequency down.


# --- SECTION 2: STRINGS ------------------------------------------------------

def is_isomorphic_SOLUTION(s, t):
    if len(s) != len(t):
        return False
    map_st, map_ts = {}, {}
    for cs, ct in zip(s, t):
        if cs in map_st and map_st[cs] != ct:
            return False
        if ct in map_ts and map_ts[ct] != cs:
            return False
        map_st[cs] = ct
        map_ts[ct] = cs
    return True
# Explanation: without the second dict, "ab" -> "aa" would pass
# (a->a, b->a) even though two different s-chars map to the same
# t-char, which breaks the one-to-one requirement.


def ransom_note_SOLUTION(ransom_note_str, magazine):
    from collections import Counter
    mag_counts = Counter(magazine)
    for ch in ransom_note_str:
        if mag_counts[ch] <= 0:
            return False
        mag_counts[ch] -= 1
    return True
# Explanation: count what's available, spend it down as you use it.
# Equivalent shortcut: Counter(ransom_note_str) - Counter(magazine)
# should have no positive counts left.


def first_unique_char_SOLUTION(s):
    from collections import Counter
    counts = Counter(s)
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
# Explanation: first pass builds frequency map (order doesn't
# matter here), second pass finds the first char whose count is 1.


# --- SECTION 3: TWO POINTERS -------------------------------------------------

def is_palindrome_SOLUTION(s):
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
# Explanation: skip non-alphanumeric chars from both ends, compare
# lowercase versions, move both pointers inward until they meet.


def max_area_SOLUTION(height):
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        best = max(best, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best
# Explanation: area is limited by the shorter line, so moving the
# taller line inward can never help (width shrinks, height caps the
# same). Always move the shorter side — it's the only way area
# might improve.


def three_sum_SOLUTION(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # skip duplicate "fixed" values
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
# Explanation: sorting lets you fix one number and two-pointer the
# rest like a "two sum on sorted array." The duplicate-skipping
# logic is what makes triplets unique.


# --- SECTION 4: SLIDING WINDOW ----------------------------------------------

def length_of_longest_substring_SOLUTION(s):
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
# Explanation: seen = set() (not {}) is the fix for your recurring
# bug. Expand right always; shrink left only while there's a
# duplicate in the window.


def min_window_substring_SOLUTION(s, t):
    from collections import Counter
    if not s or not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best_left, best_len = 0, float('inf')
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:
            if right - left + 1 < best_len:
                best_left, best_len = left, right - left + 1
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if best_len == float('inf') else s[best_left:best_left + best_len]
# Explanation: `missing` tracks how many required chars are still
# unsatisfied. Once it hits 0 the window is valid — shrink from the
# left to find the tightest valid window before it breaks again.
# min_len/best_len starts at float('inf') so any real window wins.


def max_sum_subarray_k_SOLUTION(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        best = max(best, window_sum)
    return best
# Explanation: fixed-size window — compute once, then slide by
# adding the new right edge and subtracting the old left edge.
# O(n) instead of recomputing each window sum from scratch.


# --- SECTION 5: STACK ---------------------------------------------------------

def is_valid_parens_SOLUTION(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
# Explanation: push opens, and on a close check `if not stack`
# BEFORE popping — that's the guard that prevents crashing on
# unmatched closers.


def daily_temperatures_SOLUTION(temperatures):
    n = len(temperatures)
    result = [0] * n
    stack = []  # indices, monotonic decreasing temps
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_i = stack.pop()
            result[prev_i] = i - prev_i
        stack.append(i)
    return result
# Explanation: store INDICES (your known bug spot), not temps.
# When you find something warmer than the stack's top, that's the
# top's answer — pop it and record the day gap.


def backspace_compare_SOLUTION(s, t):
    def build(string):
        stack = []
        for ch in string:
            if ch != '#':
                stack.append(ch)
            elif stack:
                stack.pop()
        return "".join(stack)
    return build(s) == build(t)
# Explanation: same `elif stack:` guard pattern — only pop if
# there's something to pop when you hit a '#'.


# --- SECTION 6: BINARY SEARCH -------------------------------------------------

def binary_search_SOLUTION(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1  # NOT right = mid
    return -1  # don't forget this
# Explanation: <= because a single-element range (left == right)
# still needs to be checked. right = mid - 1 excludes mid once
# you've confirmed it's too high.


def find_min_rotated_SOLUTION(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1   # min is to the right of mid
        else:
            right = mid      # mid could BE the min, keep it in range
    return nums[left]
# Explanation: compare mid to the right edge. If nums[mid] is
# bigger than nums[right], the rotation point (and min) is to the
# right. Otherwise mid is a candidate, so right = mid (not mid - 1).


def koko_eating_bananas_SOLUTION(piles, h):
    def hours_needed(speed):
        return sum((pile + speed - 1) // speed for pile in piles)
    left, right = 1, max(piles)
    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= h:
            right = mid       # mid works, try slower
        else:
            left = mid + 1    # mid too slow, need faster
    return left
# Explanation: binary search over possible SPEEDS (1 to max(piles)),
# not over the array. "hours_needed(speed) <= h" is the monotonic
# check — as speed increases, hours needed only decreases (or stays
# the same), which is what makes binary search valid here.

# =============================================================================
# END OF FILE
# =============================================================================