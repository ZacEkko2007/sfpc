firstDaySet = set([1, 3, 6, 8, 11, 14, 16, 19, 21])
secondDaySet = set([3, 5, 8, 10, 11, 14, 16, 18, 21])
firstDayList = list(firstDaySet)
secondDayList = list(secondDaySet)

used = firstDaySet & secondDaySet

notUsed = []
for i in range(1, 23):
    notUsed.append(i)

for j in firstDayList:
    if j in notUsed:
        notUsed.remove(j)

for j in secondDayList:
    if j in notUsed:
        notUsed.remove(j)

print(len(notUsed), len(used))
