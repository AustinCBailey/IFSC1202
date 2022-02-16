n = int(input("Enter Factorial: "))
a = 1
sum = 0
for i in range(1, n+1):
    a = a * i 
    sum += a 
print(sum)