class Error(Exception):
    pass

bloodType = input().split()
bT = ["AA", "AO", "AB", "BO", "BB", "OO"]
for i in bloodType:
    if i not in bT:
        raise Error()
    
babyBloodTypeL = []
for i in range(2):
    babyBloodTypeL.append(bloodType[0][0] + bloodType[1][i])
    babyBloodTypeL.append(bloodType[0][1] + bloodType[1][i])

for i in range(len(babyBloodTypeL)):
    if "AB" == babyBloodTypeL[i]:
        babyBloodTypeL[i] = "AB"
    elif "A" in babyBloodTypeL[i]:
        babyBloodTypeL[i] = "A"
    elif "B" in babyBloodTypeL[i]:
        babyBloodTypeL[i] = "B"
    else:
        babyBloodTypeL[i] = "O"

babyBloodTypeS = set(babyBloodTypeL)
babyBloodTypeL = list(babyBloodTypeS)
babyBloodTypeL.sort()
        
print(*babyBloodTypeL, sep = ' ')