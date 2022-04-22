a = int(input())
b, c, d = 0, 0, 0
x, y, z = map(int, input().split())
while True:
    if a >= 12:
        a -= 12
        b += x
    if b >= 8:
        b -= 8
        c += y
    if c >= 5:
        c -= 5
        d += z
    
    if a < 12 and b < 8 and c < 5:
        break

print(d)