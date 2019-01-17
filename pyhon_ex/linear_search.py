pos = 0

def search(lst, n):
    for i in lst:
        if i == n:
            return True
        globals()['pos'] += 1
    return False

lst = [4,5,3,9,8]

n = 5

if search(lst, n):
    print("Found",pos)
else:
    print("Not Found")