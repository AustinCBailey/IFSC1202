x = input("Enter Values Seperated By Spaces: ")

lst = []

for x in x.split(" "):
    lst.append(int(x))

for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        print(lst[i])
        