x = input("Enter Values Seperated By Spaces: ")

lst = x.split(" ")

for x in range(len(lst)):
    if int(lst[x]) % 2 == 1:
        print(lst[x])
