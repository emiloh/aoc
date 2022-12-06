with open("../inputs/day06.txt") as f:
    line = f.read()
    for i in range(0,len(line)-4):
        if len({x for x in line[i:i+4]}) == 4:
            print(i+4)
            break