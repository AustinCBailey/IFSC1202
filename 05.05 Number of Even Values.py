e = 0

while True:
    n = int(input("Enter a number (Zero to quit): "))
    if n == 0:
        break
    if n % 2 == 0: 
        e += 1
print(e)