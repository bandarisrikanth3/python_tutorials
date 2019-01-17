pos = 0

def search(lst,n):
    l = 0
    u = len(lst)-1


    while l <= u:
        mid = (l + u) // 2
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
        return False

lst = [2,36,38,48,66,72,86,94,108,115,124]
n = 108
if search(lst,n):
    print("found",pos)

else:
    print("Not Found")