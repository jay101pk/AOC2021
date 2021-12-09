
file = open("input.txt", "r")
lines = file.readlines()

grid = [ [ [int(s),True] for s in line.strip() ] for line in lines ]

maxX = len(grid[0]) - 1
maxY = len(grid) - 1

sum = 0
for (i,row) in enumerate(grid):
    for (j,s) in enumerate(row):
        if i > 0 and s[0] >= grid[i - 1][j][0]:
            grid[i][j][1] = False
            continue
        if i < maxX and s[0] >= grid[i + 1][j][0]:
            grid[i][j][1] = False
            continue
        if j > 0 and s[0] >= grid[i][j-1][0]:
            grid[i][j][1] = False
            continue
        if j < maxY and s[0] >= grid[i][j+1][0]:
            grid[i][j][1] = False
            continue
        sum = sum + s[0] + 1

print(sum)
