m = 0

while True:
    a = int(input("Enter Number (Zero to Quit): "))
    if a > m:
        s = a
        m = a
    elif a > m:
        a = s
    elif a == 0:
        break
print("Maximum", m)
print("Second Maximum", s)

