x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))

smallest = 0

if x < y and x < z :
    smallest = x
if y < x and y < z :
    smallest = y
if z < x and z < y :
    smallest = z

print("The Smallest Number Given Was:", smallest)