n = int(input("Enter Fibonnaci Sequence Number: "))
a = 0
b = 1
if n < 0:
    print("Incorrect input")
for i in range(2,n+1):
    c = a + b
    a = b
    b = c
print("Fibonacci Number:", c)