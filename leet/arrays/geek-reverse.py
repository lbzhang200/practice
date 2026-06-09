#generates an array such that the array is reversed 

def reverse(arr): #kind of dumb method 
    n = len(arr)
    result = []


    for j in range(n-1, -1, -1):
        result.append(arr[j])

    return result 



def reverse2(arr): #smarter
    left = 0 
    right = len(arr) - 1 #index of rightmost 

    while left < right:
         temp = arr[left]
         arr[left] = arr[right]
         arr[right] = temp

         left = left + 1
         right = right - 1
    return arr

arr = [1, 4, 3, 2, 6, 5]
print(reverse2(arr))