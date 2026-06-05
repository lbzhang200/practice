#calcualtes gcd:
def gcd(num1, num2):

    smaller = min(num1, num2) #find the smaller of the two numbers 
    for i in range(smaller, 0, -1): #work backward 
        if num1 % i == 0 & num2 % i == 0: 
            return i
        
def smallestsumInteger(num):
    if num is None:
        return -1
    
    sum = 0 
    count = 0 
    while (sum < num):
        count = count + 1
        sum = sum + count

    return count 


