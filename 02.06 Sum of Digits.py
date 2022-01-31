n = int(input("Enter Number Here: "))
n1 = n%10 
n2 = (n%100) // 10
n3 = (n%1000) // 100
print("{}".format(n1+n2+n3))