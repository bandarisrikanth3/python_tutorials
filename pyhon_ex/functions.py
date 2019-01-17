
def greet():
    print("Hello")
    print("Good Morning")

greet()

def add(x,y):
    c = x + y
    print(c)

add(4,5)

add(10,12)

def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d

r1,r2 = add_sub(9,6)

print(r1,r2)

# multiple valu key pairs

def person(**data):
    for i,j in data.items():
        print(i,j)


person(name='srikanth',age=28)