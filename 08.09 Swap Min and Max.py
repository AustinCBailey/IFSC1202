x = input("Enter Values Seperated By Spaces: ")

list1 = x.split(" ")

max = list1 [0]

l = len(list1)

for i in range(l):
    if list1 [i] > max:
        max = list1 [i]

x = list1.index(max)

min = list1 [0]

for i in range(l):
    if list1 [i] < min:
        min = list1 [i]

y = list1.index(min)

list1 [x] = min
list1 [y] = max

Final = ' '.join(list1)
print("Swapped Min and Max", Final)