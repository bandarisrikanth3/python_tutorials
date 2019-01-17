
x = int(input("Enter Ur Number: "))
r = x % 2
if r==0:
    print("x is even")

    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print('x is either')
else:
    print("x is odd")