n = 1
pre = 0
i = 0
c = 0
b = None
mc = 0

while n != 0:
    n = int(input("Enter a Number (Zero To Quit): "))
    if n != 0:
        if i == 0:
            pre = n
            c = 1
        else:
            if n == pre:
                c += 1
            else:
                if c > mc:
                    mc = c
                    b = pre
        i += 1
        pre = n

print(b, "Repeated", mc, "Times")