from sys import getrecursionlimit,setrecursionlimit

setrecursionlimit(5000)
x = getrecursionlimit()
print(x)
n = int(input("Enter Number"))
def fact(n):
    if(n == 0):
        return 1
    return n * fact(n-1)

result = fact(n)
print(result)