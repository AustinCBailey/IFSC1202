l = 0
f = True
while True:
    n = int(input("Enter a number (Zero to quit): "))
    if n == 0:
        break
    if f or l < n:
        l = n
    f = False
print('Maximum:', l)