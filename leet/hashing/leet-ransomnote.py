#returns true if magcount has enough leters to construct ransomNote 
from collections import Counter
def canConstruct(self, ransomNote, magazine):

    magCount = Counter(magazine) #counts letters in magazine and puts in a dictionary 

    for ch in ransomNote:
        magCount[ch] = magCount[ch] - 1
        if (magCount[ch] < 0):
            return False 
    return True 

