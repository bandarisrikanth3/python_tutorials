x = ['navin', 1, 2]

print(x)

for i in x:
    print(i)

print()
y = 'navin'

for j in y:
    print(j)

print()

print(len(y))

z = 0
while z < len(y):
    print(y[z])
    z += 1

# ascending order
for x in range(11, 21, 1):
    print(x,end=" ")
print()

# reverse order
for x in range(21,11,-1):
    print(x,end=" ")
print()

for x in range(1,21,1):
    if(x%5 == 1 and x%3 == 1 ):
        print(x ,end=" ")




