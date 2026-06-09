#leaders in an array - if elements are greater than all the elemnts on the right side 
"""
def leaders(arr): #dumb method 
    result = []
    n = len(arr)

    for i in range(n): #iterates through the array 

        for j in range(i+1, n): #looks at each number 

            if arr[i] < arr[j]: #j represents right numbers 
                break
            else:
                result.append(arr[i])

    return result 

def leaders2(arr): #smart method - rightmost must be a leader 
    result = []
    n = len(arr)

    maxright = arr[-1]
    result.append(maxright)

    for i in range(n-2, -1, -1): #right to left, starts at second to last element 

        if arr[i] >= maxright: #if left is greater than right 
            maxright = arr[i] #max changes, left needs to be bigger than right 
            result.append(maxright)

    result.reverse()

    return result 




"""



def leaders(arr):
    result = []
    n = len(arr)

    for i in range(n):
        for j in range(i+1, n):
            if arr[j] > arr[i]: 
                break
            else:
                result.append(arr[i])
    return result 

def leaders(arr):
    result = []
    n = len(arr)

    final = arr[-1] 
    result.append(final)

    for i in range(n-2, -1, -1): 
        if (arr[i] < final):
            break

        else:
            final = arr[i]
            result.append(arr[i])

    return result 



