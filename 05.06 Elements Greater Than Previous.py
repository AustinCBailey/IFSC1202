n = 1
p = 0
i = 0
c = 0

while n != 0:
    n = int(input("Enter a Number (zero to quit): "))
    if n != 0:
        if i == 0:
            p = n
        if n > p:
            c += 1
        i += 1
        p = n
print("Number of Values Greater Than the Previous:", c)