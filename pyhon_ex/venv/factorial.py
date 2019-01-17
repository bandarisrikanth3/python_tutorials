
number = int(input("Enter the number"))
def fact(number):
    f = 1
    for i in range(1,number+1):
        f  *= i
    return f

result = fact(number)
print(result)


