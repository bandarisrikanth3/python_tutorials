from functools import reduce

lst = list(range(1,21))

# find even numbers using filter

evens = list(filter(lambda n: n%2==0,lst))

print('even numbers are {}'.format(evens))

# find double of a number using map

doubles = list(map(lambda n : n*2,evens))

print("Doubles are {}".format(doubles))

# find the sum using reduce

sum = reduce(lambda a,b: a+b,doubles )

print("Sum : {}".format(sum))

