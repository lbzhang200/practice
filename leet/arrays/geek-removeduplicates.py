def removeduplicates(arr): #removes all duplicates of an array and prints out array with no duplicates 

    if not arr: 
        return 0
    
    n = len(arr)
    
    i = 0

    for j in range(1, n):
        if arr[j] != arr[i]: #if the first element is not the same as previous element
            i = i + 1 
            arr[i] = arr[j] #old array spot becoms new one if no duplicates

arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
newSize = removeduplicates(arr)

for i in range(newSize):
    print(arr[i], end= " ")

#another way

def removeDuplicates(arr): #hashing
    seen = set()
    idx = 0
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1
    
    return idx 

for i in range(newSize):
    print(arr[i], end= " ")