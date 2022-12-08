def scenic(grid, x, y):
    scenic = 1
    counter = 0
    for i in range(y-1, -1, -1):
        counter += 1
        if grid[i][x] >= grid[y][x]:
            break
    scenic *= counter
    counter = 0
    for i in range(y+1, len(grid), 1):
        counter += 1
        if grid[i][x] >= grid[y][x]:
            break
    scenic *= counter
    counter = 0
    for i in range(x-1, -1, -1):
        counter += 1
        if grid[y][i] >= grid[y][x]:
            break
    scenic *= counter
    counter = 0 
    for i in range(x +1 , len(grid[y]), 1):
        counter += 1
        if grid[y][i] >= grid[y][x]:
            break
    scenic *= counter
    return scenic

with open("/Users/eh/Documents/aoc/2022/inputs/day08.txt") as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        chars = [x for x in line.strip()]
        nums = [int(x) for x in chars]
        grid.append(nums)
    s = 0
    for y in range(1, len(grid)-1, 1):
        for x in range(1, len(grid[y])-1, 1):
            s = max(s, scenic(grid, x, y))
    
    print(s)