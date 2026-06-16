# Arrays & Hashing Cheatsheet

## Data Structures — When to Use What

| Structure | Use When | Example |
|---|---|---|
| `dict` | storing one value per key | `hashmap[num] = index` |
| `defaultdict(list)` | grouping multiple values under one key | Group Anagrams |
| `defaultdict(int)` | counting frequencies | char frequency map |
| `set` | only care if something exists (not count/index) | seen before? |

---

## Pattern Recognition

- **"Have you seen this before?"** → `set` or `dict`
- **"Find two elements that satisfy X"** → `dict` to avoid O(n²) nested loops
- **"Group by shared property"** → `defaultdict(list)`
- **"Count how many times X appears"** → `defaultdict(int)` or `Counter`
- **"Elements in common between two arrays"** → set intersection `&`
- **"Need both index and value in loop"** → `enumerate`

---

## Core Snippets

### Plain dict — store last seen index
```python
hashmap = {}
for i, num in enumerate(nums):
    if num in hashmap:
        # use hashmap[num] (the previous index)
        pass
    hashmap[num] = i
```

### defaultdict(list) — grouping
```python
from collections import defaultdict
hashmap = defaultdict(list)
for word in strs:
    key = "".join(sorted(word))  # or any fingerprint
    hashmap[key].append(word)
return list(hashmap.values())
```

### defaultdict(int) — frequency count
```python
from collections import defaultdict
freq = defaultdict(int)
for char in s:
    freq[char] += 1
```

### set — membership / intersection
```python
seen = set()
seen.add(x)
if x in seen: ...

# intersection of two arrays
result = list(set(nums1) & set(nums2))
```

---

## Complexity Trade-off

| Approach | Time | Space |
|---|---|---|
| Brute force (nested loops) | O(n²) | O(1) |
| Hashing | O(n) | O(n) |

> You trade space for time — store what you've seen so you don't re-scan.

---

## Problems

### LC 49 — Group Anagrams (Medium)
```python
from collections import defaultdict

def groupAnagrams(strs):
    hashmap = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        hashmap[key].append(word)
    return list(hashmap.values())
```
**Key insight:** anagrams share the same sorted string → use as fingerprint/key.

---

### LC 349 — Intersection of Two Arrays (Easy)
```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```
**Key insight:** sets handle uniqueness automatically. `&` = intersection.

---

### LC 219 — Contains Duplicate II (Easy)
```python
def containsNearbyDuplicate(nums, k):
    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap and i - hashmap[num] <= k:
            return True
        hashmap[num] = i
    return False
```
**Key insight:** store last seen index. On revisit, check if distance ≤ k. Always update to latest index.

---

## defaultdict vs plain dict — Quick Rule
- Value is a **single thing** (index, bool, count) → plain `dict`
- Value is a **collection** you're building → `defaultdict(list)` or `defaultdict(int)`
