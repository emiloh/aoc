with open("../inputs/day10.txt") as f:
    lines = f.readlines()
    x = 1
    cycles = 1
    mods = 20
    sum = 0
    for line in lines:
        op = (line.strip()).split(" ")
        if op[0] == "noop":
            cycles += 1
            if cycles == mods:
                sum += x * cycles
                mods += 40
        else:
            if cycles + 2 > mods:
                sum += x * (cycles + (mods - cycles))
                mods += 40
            x += int(op[1])
            cycles += 2
    print(sum)