bloodType = ["AB", "OO"]
babyBloodTypeL = []
for i in range(2):
    babyBloodTypeL.append(bloodType[0][0] + bloodType[1][i])
    babyBloodTypeL.append(bloodType[0][1] + bloodType[1][i])

babyBloodTypeS = set(babyBloodTypeL)
babyBloodTypeL = list(babyBloodTypeS)
babyBloodTypeL.sort()

for i in range(len(babyBloodTypeL)):
    if "AB" == babyBloodTypeL[i]:
        babyBloodTypeL[i] = "AB"
    elif "A" in babyBloodTypeL[i]:
        babyBloodTypeL[i] = "A"
    elif "B" in babyBloodTypeL[i]:
        babyBloodTypeL[i] = "B"
    else:
        babyBloodTypeL[i] = "O"
        
print(*babyBloodTypeL, sep = ' ')