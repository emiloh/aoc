def update_crt(x):
    crt = [x-1, x, x+1]
    return crt
with open("../inputs/day10.txt") as f:
    lines = f.readlines()
    x = 1
    drawing = ["." for x in range(240)]
    crt = [0, 1, 2]
    cycles = 0
    for line in lines:
        op = (line.strip()).split(" ")
        if op[0] == "noop":
            if cycles % 40 in crt:
                drawing[cycles-1] = "#"
            cycles += 1
        else:
            if cycles % 40 in crt:
                drawing[cycles-1] = "#"
            cycles += 1
            if cycles % 40 in crt:
                drawing[cycles-1] = "#"
            cycles += 1
            x += int(op[1])
            crt = update_crt(x)
    for i in range(1, len(drawing)+1):
        print(drawing[i-1], end="")
        if i % 40 == 0:
            print()