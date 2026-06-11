#mix of problems to test knowledge

def containsduplicate(nums):
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False
 


def validanagram(s, t):
    if len(s) != len(t):
        return False 
    return sorted(s) == sorted(t)

#or 

def validanagramhash(s, t):
    if len(s) != len(t):
        return False 
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[t] = count.get(t, 0) + 1

    return all(v == 0 for v in count.values())

#or 
from collections import Counter 
from collections import defaultdict
def validanagramcount(s, t):
    return Counter(s) == Counter(t)


def checkifn(nums): #check if i is not equal to j such that nums[i] == 2*nums[j]
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if i != j:
                if nums[i] == nums[j] * 2:
                    return True 
                
    return False 
                
def checkifn2(nums): #smarter

    seen = set()
    for n in nums:
        if 2 * n in seen or (n % 2 == 0 and n // 2 in seen): #if n is divisble by 2 and is in seen
            return True 
    seen.add(n)

    return False 

def isomorphicstrings(s, t): #can be mapped one to one - this is hard
    stot = {}
    ttos = {}

    for schar, tchar, in zip(s, t):
        if schar in stot and stot[schar] != tchar:
            return False 
        if tchar in ttos and ttos[tchar] != schar:
            return False 
        
        stot[schar] = tchar
        ttos[tchar] = schar 

def groupanagrams(nums): #group anagrams together given array of strings 

    hashmap = defaultdict(list)

    for n in nums:
        key = "".join(sorted(n))
        hashmap[key].append(n)

    return list(hashmap.values())

def subarraysum(nums, k): #return number of subarrays whose sum equals k

    count = 0 
    prefix = 0
    seen = {0: 1}

    for num in nums:
        prefix = prefix + num
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count 

#review this one 

def topkelements(nums, k): #return the k most frequent elements
    #use Counter

    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result



        
    