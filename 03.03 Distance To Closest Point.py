a = int(input("Enter Point 1: "))
b = int(input("Enter Point 2: "))
c = int(input("Enter Point 3: "))

B = b - a
C = c - a

if B > C:
    print(C)
else:
    print(B)