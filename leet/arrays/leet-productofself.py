#problem is find the porducts of everything except its index
def productexceptself(self, nums): #fails too slow 

    result = []
    n = len(nums)

    for i in range(len(nums)):
        product = 1 
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result.append(product)

    return answer

def productsexceptself2(self, nums):
    n = len(nums)

    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1] #(left side)

    suffix = 1
    for i in range(n-2, -1, -1):
        suffix = suffix * nums[i+1]  #(right side)
        answer[i] = answer[i] * suffix  #(multiply both)

    return answer 


def productexceptself2(self, nums):
    n = len(nums)

    answer = [1] * n
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]  #left side

    suffix = 1
    for i in range(n-2, -1, -1):
        suffix = suffix * nums[i+1] #right side
        answer[i] = answer[i] * suffix 

    return answer 