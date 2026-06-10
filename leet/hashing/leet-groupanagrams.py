#return array of strings grouped with same letters 
from collections import defaultdict

def groupAnagrams(self, strs):

    hashmap = defaultdict(list)

    for st in strs:
        key = "".join(sorted(st))
        hashmap[key].append(st)

    return list(hashmap.values())
