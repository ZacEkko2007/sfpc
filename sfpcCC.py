numList = [4, 2, 3, 1, 10, 3, 1, 3, 4, 5, 9, 7, 4, 1, 3, 8, 2, 5, 1, 9]
v = 0
for i in range(2,7):
    v += numList[i]
    
result = 0
n = 0
for i in range(len(numList)):
    for j in range(len(numList)):
        for k in numList[i:j]:
            result += k
        if result == v:
            n += 1
            result = 0
        elif result > v:
            result = 0
            break
        else:
            result = 0

print(n)