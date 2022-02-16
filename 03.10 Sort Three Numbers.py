a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if a > b and b > c:
    print(c, b, a)
if c > b and b > a:
    print(a, b, c)
if b > c and c > a:
    print(a, c, b)
if b < a and c > a:
    print(b, a, c)
    