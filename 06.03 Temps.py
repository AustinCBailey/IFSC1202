File = open("06.03 FTemps.txt", "r") 

Records = 0

for F in File: 
    C = (float(F) - 32)*5/9 
    C = round(C,1) 
    f = open("06.03 CTemps.txt", "a") 
    f.write(str(C)) 
    f.write('\n') 
    f.close() 
    Records = Records + 1 

print(Records, "Records Written")
