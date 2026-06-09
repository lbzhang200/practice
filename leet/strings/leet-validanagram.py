#anagram means it got same exact letters 
def validanagram(self, s, t):
    if len(s) != len(t): 
        return False 
    return sorted(s) == sorted(t)
