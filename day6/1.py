import re

file = open("input", "r")
lines = file.readlines()

fishs = [int(x) for x in (re.split(r',', lines[0]))]

for i in range(80):
    newFish = 0
    for (index, fish) in enumerate(fishs):
        if fish == 0:
            fishs[index] = 6
            newFish = newFish + 1
        else:
            fishs[index] = fish - 1
    for j in range(newFish):
        fishs.append(8)
print(len(fishs))