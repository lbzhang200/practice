def unique(self, s): #hashing + count
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1

    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    
    return -1 
from collections import Counter 

def unique2(self, s): #uses Counter 

    count = Counter(s)

    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1 



