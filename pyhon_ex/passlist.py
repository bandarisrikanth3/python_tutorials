

list = []

count_list = int(input("Enter number of names"))
i = 0
count=0
for i in range(count_list):
    name = input('enter name')
    list.append(name)
    if len(name) > 5:
        count += 1

print("List:{} and count > 5 is {}".format(list,count))

