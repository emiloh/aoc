with open("../inputs/day06.txt") as f:
    line = f.read()
    for i in range(0,len(line)-16):
        if len({x for x in line[i:i+14]}) == 14:
            print(i+14)
            break