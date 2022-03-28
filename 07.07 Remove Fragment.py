x = str(input("Enter A String: "))

if x.count("h") >= 2:
    print(x[:x.find("h")] + x[x.rfind("h") + 1:])

else: print(x.count("h"))