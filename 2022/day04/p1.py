with open("../inputs/day04.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        split = [x.strip() for x in line.split(",")]
        r1 = [int(x) for x in split[0].split("-")]
        r2 = [int(x) for x in split[1].split("-")]
        if r1[0] <= r2[0] and r2[1] <= r1[1]:
            sum += 1
        elif r2[0] <= r1[0] and r1[1] <= r2[1]:
            sum += 1
        
    print(sum)