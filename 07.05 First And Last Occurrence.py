x = str(input("Enter A String: "))

if x.__contains__("f"):
    print(x.index("f"))
    print(len(x)- 1 - x[::-1].index("f"))
else: print("0")