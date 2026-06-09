#moves all zeroes in an array to end of array

def movezeroes(arr): 
    n = len(arr)
    result = [0] * n
    j = 0 #index for temp array

    for i in range(n): #adds all nonzero elements first 
        if arr[i] != 0:
            result[j] = arr[i] 
            j += 1 


    while j < n:
        result[j] = 0 #replaces rest with 0 
        j += 1 

    for i in range(n):
        arr[i] = result[i] #gives the elements to originial 