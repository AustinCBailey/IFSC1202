m = 0

while True:
    a = int(input("Enter Number (Zero To Quit): "))
    if a > m:
        c = 1
        m = a
    elif a == m:
        c += 1
    elif a == 0:
        break
print("Max", m)
print("NumOfOcc", c)