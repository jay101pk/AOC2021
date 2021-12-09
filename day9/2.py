
from os import remove


file = open("input.txt", "r")
lines = file.readlines()

grid = [ [ [int(s),-1] for s in line.strip() ] for line in lines ]
# print(grid)

maxX = len(grid[0]) - 1
maxY = len(grid) - 1

b = 0
bc = list()
for a in range(100):
    for (i,row) in enumerate(grid):
        for (j,s) in enumerate(row):
            ele = s[1]
            if s[0] != 9:
                if i > 0:
                    bas = grid[i - 1][j][1]
                    if bas != -1 and (ele == -1 or ele > bas):
                        grid[i][j][1] = bas
                        continue
                if i < maxX:
                    bas = grid[i + 1][j][1]
                    if bas != -1 and (ele == -1 or ele > bas):
                        grid[i][j][1] = bas
                        continue
                if j > 0:
                    bas = grid[i][j-1][1]
                    if bas != -1 and (ele == -1 or ele > bas):
                        grid[i][j][1] = bas
                        continue
                if j < maxY:
                    bas = grid[i][j+1][1]
                    if bas != -1 and (ele == -1 or ele > bas):
                        grid[i][j][1] = bas
                        continue
                if ele == -1:
                    grid[i][j][1] = b
                    b = b+1

bc = [0 for _ in range(b+1)]
for row in grid:
    for s in row:
        bc[s[1]] = bc[s[1]] + 1

p = 1
sbc = sorted(bc, reverse=True)
for bs in sbc[1:4]:
    p = p * bs

print(p)


