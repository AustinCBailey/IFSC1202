def IsEven(n): 
    if (n % 2) == 0:
        Even = ("True")
    else:Even = ("False")
    print("Even=",Even)

def IsOdd(n):
    if (n % 2) == 0:
        Odd = ("False")
    else: Odd = ("True")
    print("Odd=",Odd)
    
        
def IsPrime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                Prime = ("False")
                break
            else: Prime = ("True")
        print("Prime=",Prime)

IsEven(n)
IsOdd(n)
IsPrime(n)

    