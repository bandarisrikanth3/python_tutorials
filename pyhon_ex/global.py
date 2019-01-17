

a = 10
print('address of a :',id(a))

# called Function
def something():

    # global declaration
    global a
    a = 15
    print('address of a :', id(a))
    print('inside: ',a)

    # changing global variable value

    # global assign values
    globals()['a'] = 20

# calling Function
something()

print('outside: ',a)