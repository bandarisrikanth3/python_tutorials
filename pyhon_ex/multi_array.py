from numpy import *

arr1 = array([
                [1,2,3,4,5,6],
                [4,5,6,7,0,8]
            ])

print(arr1.ndim)

print(arr1.shape)

print(arr1.size)

arr2 = arr1.flatten()

print(arr2)

arr3 = arr2.reshape(6,2)

print(arr3)

# 3d array

print(arr2.reshape(2,2,3))

# matrix
m = matrix("1 2 3 ; 4 5 6 ; 7 8 9 ")

print(m)

print('Diagonal: ',diagonal(m))

print('minimum',m.min())

print('maximum',m.max())

m1 = matrix("1 1 1; 1 1 1; 1 1 1")
m2 = matrix("1 1 ; 1 1 ; 1 1 ")

#m3 = m1 + m2

#print("Matrix Add: ",m3)

m4 = m1 * m2

print("Matrix Multiple: ",m4)

