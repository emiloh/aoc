import re
with open("../inputs/day05.txt") as f:
    lines = f.readlines()
    stacks = []
    first = True
    counter = 0
    for line in lines:
        if "[" in line:
            crates = [line[x] for x in range(1, len(line), 4)]
            if first: 
                stacks = [[] for x in range(len(crates))]
                first = False
            for i in range(len(crates)):
                if crates[i] != " ":
                    stacks[i].insert(0,crates[i])
            print(stacks)
        else:
            if counter != 2:
                counter += 1
                continue
            stat = [int(x) for x in re.findall(r"\d+", line)]
            index = len(stacks[stat[2]-1])
            for i in range(stat[0]):
                crate = stacks[stat[1]-1].pop()
                stacks[stat[2]-1].insert(index,crate)
            print(stacks)
    for i in range(len(stacks)):
        print(stacks[i].pop(), end="")