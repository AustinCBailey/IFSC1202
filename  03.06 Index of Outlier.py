a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

Index = 0

if a!=b and a==c:
    Index = 2
if b==a and b != c:
    Index = 3
if c==b and a != c:
    Index = 1
print(Index)