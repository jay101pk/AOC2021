import re

grid: list[list[bool]] = [[False for x in range(2000)] for y in range(2000)]
maxX: int = 0
maxY: int = 0
with open("input.txt", "r") as file:
    count = 0
    folds = False
    for row in file:
        count += 1
        if row == "\n":
            if folds:
                break
            folds = True
            continue

        if not folds:
            r = row.split(',')
            x = int(r[0])
            if x > maxX:
                maxX = x
            y = int(r[1])
            if y > maxY:
                maxY = y
            grid[x][y] = True
        else:
            a = re.search(r'([xy])=(\d+)', row)
            if a.group(1) == 'x':
                x = int(a.group(2))
                for j in range(maxY + 1):
                    for i in range(x):
                        if grid[i][j] or grid[(2 * x) - i][j]:
                            grid[i][j] = True
                maxX = x
            else:
                y = int(a.group(2))
                for j in range(maxX + 1):
                    for i in range(y):
                        grid[j][i] |= grid[j][(2 * y) - i]
                maxY = y

            s = 0
            for x in range(maxX + 1):
                for y in range(maxY + 1):
                    if grid[x][y]:
                        s += 1

            print(s)

for y in range(maxY + 1):
    for x in range(maxX + 1):
        if grid[x][y]:
            print('#', end='')
        else:
            print('.', end='')
    print()
