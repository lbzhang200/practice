import numpy as np

data = [1, 2, 3, 4]
doubled = [x * 2 for x in data] #loops in python

arr = np.array([1, 2, 3, 4])
doubled = arr * 2 #much faster 

#arrays can be 1d, 2d

np.array([1, 2, 3]) #making an array 
np.array([1, 2], [3,4]) 

np.zeroes((3,4)) #3x4 block of zeroes 

np.arrange(0, 20, 2) #[0, 2, 4, 18]


#three characteristics of an array

np.array([1,2,3], 
         [4,5,6])

arr.shape #(2, 3) - 2 rows, 3 cols 
arr.ndim #2 
arr.dtype #dtype('int64)

#indexing through an array
a = np.array([10, 20, 30, 40, 50])

a[0] #10 
a[-1] #50 
a[1:4] #array([20, 30, 40])

#2d array 
m = np.array([[1,2,3],[4,5,6],[7,8,9]])
m[0, 2] #3 (row 0, col 2)
m[:2, 1:] #rows 0-1, cols 1-2 -> [[2,3], [5,6]]

a = np.array([10, 20, 30, 40, 50])
a[a>25] #array ([30, 40, 50])


#operations for an array

a = np.array([1., 2., 3.])
b = np.array([4., 5., 6.])

a+b #adds respective columns
a*b #multiplies
a**2 #to the power of 2
np.sqrt(a)

#summarize arrays 
arr = np.array([1, 2, 3],
               [4, 5, 6])
arr.sum()
arr.sum(axis=0) #add by column [5, 7, 9]
arr.sum(axis=1) #add by row [6, 15]

arr.mean()
arr.max()
arr.min()

#slicing returns a view not a copy 

original = np.array([0, 1, 2, 3, 4])
view = original[1:4] #not a copy 

view[0] = 99 
print(original) #[0, 99, 2, 3, 4] - changed

safe = original[1:4].copy()
safe[0] = 99
print(original) #[0, 99, 2, 3, 4] - unchanged 



