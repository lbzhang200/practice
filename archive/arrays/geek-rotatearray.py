#rotate clockwise by certain amount of times 
def rotatearray(arr, d): #rotate it one by one 
    n = len(arr)

    for i in range(d): #rotated d amount of times 

        last = arr[n-1] #sets last 
        for i in range(n-1, 0, -1):
            arr[i] = arr[i-1] #rotates each by one
        arr[0] = last #first becomes last 




def rotatearray(arr, d):
    n = len(arr)
    for i in range(d):

        last = arr[n-1]
        for i in range(n-1, 0, - 1):
            arr[i] = arr[i-1]

        arr[0] = last 
