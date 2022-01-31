n = int(input("Enter Number Here: "))
n1 = n%10 
n2 = (n%100) // 10
n3 = (n%1000) // 100
r = 100 * n1 + 10 * n2 + n3
print("{}".format(r))