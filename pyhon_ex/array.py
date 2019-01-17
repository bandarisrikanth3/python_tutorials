from array import *

vals = array('i',[-1,2,3,4])

vals.reverse()
print(vals)

for i in range(len(vals)):
    print(vals[i])

for  j in vals:
    print(j)

n = int(input("Enter array size"))
arr = array('i',[])
for z in range(n):
    arr.append(int(input("Enter array Values")))

print(arr)


# index number

val = int(input("Enter user value"))
k = 0
for e in arr:
    if(e == val):
        print(k)
        break
    k += 1
print(arr.index(val))