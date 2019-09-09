import numpy as np

#Using NumPy create random vector of size 15 having only Integers in the range 1-20. 
arr = np.random.randint(1, high=20, size=15, dtype='int')
print('random array= ', arr)
print("===============================")
#reshape the array to 3 by 5
newArr = np.reshape(arr,(3,5))
print('Array after using reshape function:\n ', newArr)

#To replace the max in each row by 0
print('=======================================')
maxArr = np.where(newArr == np.max(newArr, axis=1, keepdims= True), 0*newArr,newArr)
print("New array with 0 instead of the max number: \n", maxArr)




