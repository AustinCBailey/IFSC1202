n = int(input("Enter a number (Zero to quit): "))

if n == 0:
    print("Division By Zero")
    quit()
t = 0
a = 0
i = 0

while n != 0:
    t = t + n
    n = int(input("Enter a number (Zero to quit): "))
    i = i + 1
a = t /i
print(a)


    
        

    


