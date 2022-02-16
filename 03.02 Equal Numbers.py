x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

Matching = 0
if x == y and y == z:
    Matching = 3
if x != y and y != z:
    Matching = 0
if x == z and z != y:
    Matching = 2
if x == y and y != z:
    Matching = 2
if y == z and y != x:
    Matching = 2

print(Matching)
