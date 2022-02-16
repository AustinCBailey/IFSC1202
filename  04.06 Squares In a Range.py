a = int(input("Enter Int A: "))
b = int(input("Enter Int B: "))
r = 0
for i in range(a, b+1):
    r = i * i 
    print(i, i, sep= "*", end= "=",)
    print(r)