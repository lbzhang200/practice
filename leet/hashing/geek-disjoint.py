#good example check if there is no element common between two arrays

def disjoint(a, b): #dumb way

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                return False 
            
    return True 

def disjointhash(a, b): #hash method 

    seen = set()

    for lettersa in a:
        seen.add(lettersa)

    for lettersb in b:
        if lettersb in seen:
            return False 
    return True 


