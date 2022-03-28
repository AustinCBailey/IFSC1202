
def IsEven(n): 
    if (n % 2) == 0:
        return True
    else:
        return False


def IsOdd(n):
    if (n % 2) == 0:
        return False
    else: 
        return True
    
    
        
def IsPrime(n):
    if n > 1:
        for i in range(2, (n//2 + 1)):
            if (n % i) == 0:
                return False
        return True 
                

EvenCount = 0
OddCount = 0
PrimeCount = 0
ReadCount = 0

File = open("06.06 Numbers.txt", "r")
FileEven = open("06.06 Even Numbers.txt", "w")
FileOdd = open("06.06 Odd Numbers.txt", "w")
FilePrime = open("06.06 Prime Numbers.txt", "w")

n = (File.readline())

while n != '':
    ReadCount += 1
    x = int(n)
    if (IsEven(x)):
        EvenCount += 1
        FileEven.write(str(x) +  "\n")

    if (IsPrime(x)):
        PrimeCount += 1
        FilePrime.write(str(x) + "\n")

    if (IsOdd(x)):
        OddCount += 1
        FileOdd.write(str(x) + "\n")


    n = (File.readline())    
print(ReadCount, "Numbers Read")
print(EvenCount, "Even Numbers")
print(OddCount, "Odd Numbers")
print(PrimeCount, "Prime Numbers")
File.close()
FileEven.close()
FileOdd.close()
FilePrime.close()