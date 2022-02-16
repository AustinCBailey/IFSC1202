a = int(input("Enter Four Digit Year: "))

if a % 400 == 0 and a % 100 == 0:
    print(a, "LEAP YEAR")
if a % 4 == 0 and a % 100 != 0:
    print(a, "LEAP YEAR")
if a % 4 != 0 and a % 100 != 0:
    print("COMMON YEAR")

