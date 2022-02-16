n = int(input("Enter Card Ammount: "))
a = 0
x = n 

for i in range(n-1):
  n = int(input("Enter Current Cards: "))
  a += n
for i in range(x):
  x += i
  i += n
x -= a
print("Missing Card: ", x)