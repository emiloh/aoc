def check(grid, x, y):
    visible = False
    if not visible:
        largest = -1
        for i in range(0, y, 1):
            largest = max(grid[i][x], largest)
        if grid[y][x] > largest:
            visible = True  
    if not visible:
        largest = -1
        for i in range(len(grid)-1, y, -1):
            largest = max(grid[i][x], largest)
        if grid[y][x] > largest:
            visible = True
    if not visible:
        largest = -1
        for i in range(0, x, 1):
            largest = max(grid[y][i], largest)
        if grid[y][x] > largest:
            visible = True
    if not visible:
        largest = -1
        for i in range(len(grid[y])-1, x, -1):
            largest = max(grid[y][i],largest)
        if grid[y][x] > largest:
            visible = True
    return visible

with open("/Users/eh/Documents/aoc/2022/inputs/day08.txt") as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        chars = [x for x in line.strip()]
        nums = [int(x) for x in chars]
        grid.append(nums)
    sum = 0
    for y in range(1, len(grid)-1, 1):
        for x in range(1, len(grid[y])-1, 1):
            if check(grid, x, y):
                sum += 1
    edge = 2 * (len(grid)) + 2 * (len(grid[0]) - 2) 
    print(sum + edge)