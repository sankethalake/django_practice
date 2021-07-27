#   Questions
# id of array same
# numArray.sort()   in reverse

import numpy as np

li1 = [1,2,3,4,5]
ar1 = np.array(li1)
print(ar1)
print(type(ar1))

li2 = [1,2,3,4,5]
ar2 = np.array(li2)

print(ar1 + ar2)            # possible for array

li3 = [1,2,3]
li4 = [5,6,7]
ar3 = np.array([li3,li4])
print(ar3)                 # matrix
print(type(ar3))

arrayOfOnes = np.ones(9, dtype=int)         # default dtype= float
print(arrayOfOnes)

arrayOfZeros= np.zeros(7)
print(arrayOfZeros)

print(type(arrayOfOnes[0]))             # numpy.int32

li5 = np.arange(1,25)                   # array with elements form 1 to 24
print(li5)

reshaped = li5.reshape(4,6)             # reshape(row,col)
print(reshaped)

li6 = np.arange(1,51)
print(li6.max())
print(li6.mean())
print(li6.min())

li7 = np.array([[1,2,3,4,5], [11,22,33,44,55]])
print(li7)

for i in li7:           # traversing 2 d array
    for j in i:
        print(j)

EmptyArray = np.empty(3)
print(EmptyArray)       # no garbage values(python not support garbage values)
                                # empty values
EmptyArray[0] = 99      # if we not assign all values it assigns none
EmptyArray[1] = 98
EmptyArray[2] = 97

print(id(EmptyArray))

print(id(EmptyArray[0]))
print(id(EmptyArray[1]))
print(id(EmptyArray[2]))

numpyArray = np.array([12,2,3,14,5,6,0,8])
numpyArray.sort()
print(numpyArray)

print(numpyArray.ndim)

li8 = [1,2,3,4,5]
li9 = [1,2,3,4,5]
numpyArray2 = np.array([li8,li9])
print(numpyArray2.ndim)             # dimension of array
print(numpyArray2.size)             # no of elements
print(numpyArray2.shape)            # (rows, column)

li10 = np.arange(30,45)
print(li10[0:5])        # use of slicing with array

print(li10[li10>30])    # query: in li10 print values which are grreater than 30
print(li10>30)          # it checks condition for each value of array and give bool o/p for eacjh value


li11 = [1,2,3,4,5,1,2,3,4]
arrayLast = np.array(li11)
print(np.unique(arrayLast))     # eliminate the duplicates

