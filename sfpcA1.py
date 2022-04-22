class Error(Exception):
    pass

n, firstDayCN, secondDayCN = map(int, input().split())
firstDayPN_L = input().split()
secondDayPN_L = input().split()
firstDayPN_S = set(firstDayPN_L)
secondDayPN_S = set(secondDayPN_L)

if len(firstDayPN_L) != firstDayCN or len(secondDayPN_L) != secondDayCN:
    raise Error()

for i in range(len(firstDayPN_L)):
    firstDayPN_L[i] = int(firstDayPN_L[i])
for i in range(len(secondDayPN_L)):
    secondDayPN_L[i] = int(secondDayPN_L[i])

used = firstDayPN_S & secondDayPN_S

notUsed = []
for i in range(1, n+1):
    notUsed.append(i)

i = 0
for j in firstDayPN_L:
    if j in notUsed:
        notUsed.remove(j)
        i += 1
i = 0
for j in secondDayPN_L:
    if j in notUsed:
        notUsed.remove(j)
        i += 1

print(len(notUsed), len(used))