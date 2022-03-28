File1 = open("06.05 CompareFileA.txt")
File2 = open("06.05 CompareFileB.txt")

List1 = []
List2 = []

for l in File1:
    List1.append(l)

for l in File2:
    List2.append(l)

Counter = 0

for i in range(len(List1)):
    if List1[i] != List2[i]:
        print(f"Line :{i+1} - {List1[i]}")
        print(f"Line :{i+1} - {List2[i]}")
        Counter += 1
print(Counter,"Differences")

File1.close()
File2.close()

