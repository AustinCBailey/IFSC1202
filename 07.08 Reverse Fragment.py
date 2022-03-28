x = str(input("Enter A String: "))

a = x[:x.find("h") + 1]
b = x[x.rfind("h"):]
c = x[x.find("h")+1:x.rfind("h")]

if x.count("h") >= 2:
  print(a + c[::-1] + b)
else:
  print(x.count("h"))