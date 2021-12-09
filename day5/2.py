import re

file = open("input", "r")
lines = file.readlines()

vents = [[(int(x.group(1)), int(x.group(2))), (int(x.group(3)), int(x.group(4)))]
         for x in [re.search(r'(\d+),(\d+)\s+->\s+(\d+),(\d+)', y) for y in lines]]

count = [[0 for _ in range(1000)] for _ in range(1000)]

for vent in vents:
    # vertical
    if vent[0][0] == vent[1][0]:
        mini = min(vent[0][1], vent[1][1])
        maxi = max(vent[0][1], vent[1][1])
        for i in range(mini, maxi + 1):
           count[vent[0][0]][i] = count[vent[0][0]][i] + 1
    elif vent[0][1] == vent[1][1] :
        mini = min(vent[0][0], vent[1][0])
        maxi = max(vent[0][0], vent[1][0])
        for i in range(mini, maxi+1):
            count[i][vent[0][1]] = count[i][vent[0][1]] + 1
    else:
        p = -1
        direction = 1
        if vent[0][0] < vent[1][0]:
            p = 0
            mini = vent[0][0]
            maxi = vent[1][0]
            if vent[0][1] > vent[1][1]:
                direction = -1
        else:
            p = 1
            mini = vent[1][0]
            maxi = vent[0][0]
            if vent[0][1] < vent[1][1]:
                direction = -1
        for i in range(maxi - mini + 1):
            count[mini + i][vent[p][1] + (i * direction)] = count[mini + i][vent[p][1] + (i * direction)] + 1
        
spots = [x for row in count for x in row if x > 1]
print(len(spots))