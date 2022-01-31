E1 = int(input("Enter First Number Here: "))
E2 = int(input("Enter Second Number Here: "))

n1 = E1 % 100 // 10
n2 = E2 % 100 // 10

n3 = E1 % 10
n4 = E2 % 10

x = (n1 * 1000) + (n2 * 100)
y = (n3 * 10) + n4

print("{}".format(x + y))

