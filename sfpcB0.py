boxes = [1, 3, 5, 10]
kg = 21
n = 0
while True:
    n += 1
    if kg >= 10:
        kg -= boxes[3]
    elif kg >= 5:
        kg -= boxes[2]
    elif kg >= 3:
        kg -= boxes[1]
    else:
        kg -= boxes[0]
    
    if kg == 0:
        break

print(n)