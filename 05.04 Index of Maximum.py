h= 0
i = 0
hi = 0
while True:
    n = int(input('Enter a Number ( zero to quit): '))
    if(n == 0):
        break
    i += 1 
    if n > h:
        h, hi = n , i - 1


print('Maximum: {}'.format(h))
print('Index of Maximum: {}'.format(hi))