a = 100
b = 0
c = 0
d = 0
while True:
    if a >= 12:
        a -= 12
        b += 5
    if b >= 8:
        b -= 8
        c += 3
    if c >= 5:
        c -= 5
        d += 2
    
    if a < 12:
        break

print(d)