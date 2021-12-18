def flash(grid: list[list[int]], flashed: list[list[bool]], x: int, y: int):
    if flashed[x][y]:
        return

    flashed[x][y] = True
    if x > 0:
        grid[x - 1][y] += 1
        if grid[x - 1][y] > 9:
            flash(grid, flashed, x - 1, y)

        if y > 0:
            grid[x-1][y - 1] += 1
            if grid[x - 1][y - 1] > 9:
                flash(grid, flashed, x - 1, y-1)

        if y < 9:
            grid[x-1][y + 1] += 1
            if grid[x - 1][y + 1] > 9:
                flash(grid, flashed, x - 1, y+1)


    if x < 9:
        grid[x + 1][y] += 1
        if grid[x + 1][y] > 9:
            flash(grid, flashed, x + 1, y)

        if y > 0:
            grid[x+1][y - 1] += 1
            if grid[x + 1][y - 1] > 9:
                flash(grid, flashed, x + 1, y-1)

        if y < 9:
            grid[x+1][y + 1] += 1
            if grid[x + 1][y + 1] > 9:
                flash(grid, flashed, x + 1, y+1)
    
    if y > 0:
        grid[x][y - 1] += 1
        if grid[x][y - 1] > 9:
            flash(grid, flashed, x, y - 1)

    if y < 9:
        grid[x][y + 1] += 1
        if grid[x][y + 1] > 9:
            flash(grid, flashed, x, y + 1)

with open("input.txt", "r") as file:
    grid = [[int(height) for height in row.rstrip()] for row in file]

count = 0
#part 1 make range 100, part 2 make range large
for step in range(10000):
    flashed = [[False for x in range(10)] for y in range(10)]
    for i in range(10):
        for j in range(10):
            grid[i][j] += 1

    for i in range(10):
        for j in range(10):
            if grid[i][j] > 9:
                flash(grid, flashed, i,j)

    f = len([True for row in flashed for x in row if x])

    if f == 100:
        print(step)
        break
    count += f
    grid = [[0 if x > 9 else x for x in row ] for row in grid]

print(count)