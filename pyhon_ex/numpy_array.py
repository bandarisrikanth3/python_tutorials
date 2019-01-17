from numpy import *

arr = array([1,2,3,4,5,6])

print(arr.dtype)

# output - float
# linespace
ls = linspace(0,15,16)

print(ls)


# logspace
log = logspace(0,15,10)

print("%.1f" %log[0])

# range
range = arange(0,50,10)

print(range)

# zeros

zr = zeros(6,int)

print(zr)

# ones

on = ones(6,int)

print(on)

# addition

arr = arr + 5
print(arr)
arr1 = array([1,2,3,4,5,6])
arr2 = array([1,2,3,4,5,6])

print(max(arr))

print(min(arr))

print(concatenate([arr2,arr1,on]))

#normal copy
arr3 = array([1,2,3,4,5])

arr4 = arr3

print(arr3,arr4,id(arr3),id(arr4))

# shallow copy

arr5 = array([1,2,3,4,5])
arr6 = arr5.view()
arr5[2] = 90
print("Shaloow Copy values changed for both: ",arr5,arr6,id(arr5),id(arr6))

# Deep copy

arr7 = array([1,2,3,4,5])
arr8 = arr7.copy()
arr7[2] = 90
print("Shaloow Copy values not changed: ",arr7,arr8,id(arr7),id(arr8))