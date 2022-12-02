with open("../inputs/day02.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        print(sum)
        split = [x.strip() for x in line.split()]
        print(split)
        if split[0] == "A":
            if split[1] == "X":
                sum += 3 + 0
            if split[1] == "Y":
                sum += 1 + 3
            if split[1] == "Z":
                sum += 2 + 6
        if split[0] == "B":
            if split[1] == "X":
                sum += 1 + 0
            if split[1] == "Y":
                sum += 2 + 3
            if split[1] == "Z":
                sum += 3 + 6
        if split[0] == "C":
            if split[1] == "X":
                sum += 2 + 0
            if split[1] == "Y":
                sum += 3 + 3
            if split[1] == "Z":
                sum += 1 + 6
    print(sum)