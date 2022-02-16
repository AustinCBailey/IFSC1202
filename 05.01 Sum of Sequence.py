n = 1
x = 0

while n != 0:
    n = int(input("Enter A Number (Zero To Quit): "))
    x += n 
print(x)
if n == 0:
    quit()