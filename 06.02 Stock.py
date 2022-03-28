def percentChange(todayPrice, yesterdayPrice):
    return ((todayPrice-yesterdayPrice)/(yesterdayPrice))*100

f = open("06.02 Stock.txt", "r")
s = f.read() .split("\n")
print("{0:>10s}{1:>10s}".format("Price","Change"))
print("{0:>10s}{1:>10s}".format(s[0],""))
for i in range(1, len(s)):
    print("{0:>10s}{1:>10.2f}%".format(s[i],percentChange(float(s[i]),float(s[i-1]))))