#check if two arrays are equal or not

def twoarrays(a, b): #dumb method

    if len(a) != len(b):
        return False
    
    return sorted(a) == sorted(b)

def twoarrayshash(a, b): #hashing

    if len(a) != len(b): 
        return False 
    
    mp = {}

    for num in a:
        mp[num] = mp.get(num, 0) + 1 #counts the number of occurences and puts it in a dictionary

    for num in b:
        if num not in mp:
            return False #if a doesn't occur in b
        if mp[num] == 0:
            return False #if b doesn't occur in a
        mp[num] -= 1

    return True 

