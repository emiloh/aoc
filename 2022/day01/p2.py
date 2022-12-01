with open("../../inputs/day01.txt") as f:
    lines = f.readlines()
    elfs = []
    load = 0
    for line in lines:
        if line == "\n":
            elfs.append(load)
            load = 0
        else:
            load += int(line)
    elfs.append(load)
    elfs = sorted(elfs, reverse=True)
    print(elfs[0] + elfs[1] + elfs[2])
