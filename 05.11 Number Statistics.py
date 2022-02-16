n = int(input("Enter a number (Zero to quit): "))

if n == 0:
    print("Divide By Zero")
    quit()

count = 1
sum = 0
avg = 0
min = n
max = 0

while True:
    if n == 0:
        break
    sum = sum + n
    n = int(input("Enter a number (Zero to quit): "))
    if n > 0:
        count += 1
    if n > max:
        max = n
    else: n == min

            
    

avg = sum / count 



print("Count:" ,count)
print("Sum:", sum)
print("Average:", avg)
print("Minimum:", min)
print("Maximum:", max)







