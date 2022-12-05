with open("../inputs/day04.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        split = [x.strip() for x in line.split(",")]
        r1 = [int(x) for x in split[0].split("-")]
        r2 = [int(x) for x in split[1].split("-")]
        r1 = {x for x in range(r1[0], r1[1]+1)}
        r2 = {x for x in range(r2[0], r2[1]+1)}
        both = set.intersection(r1,r2)
        if len(both) > 0:
            sum += 1
        
    print(sum)