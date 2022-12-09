coords = {}
tail = (0,0)
head = (0,0)

def check_adj(tail, head):
    lst = []
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            lst.append((tail[0]+x, tail[1]+y))
    if head in lst:
        return True
    else:
        return False

        
def move(coords, head, tail, step):
    for i in range(0,step[1]):
        if step[0] == "U":
            head = (head[0], head[1] + 1)
        elif step[0] == "R":
            head = (head[0] + 1, head[1])
        elif step[0] == "L":
            head = (head[0] - 1, head[1])
        else:
            head = (head[0], head[1] - 1)
        if not check_adj(tail, head):
            if tail[1] + 1 < head[1]:
                if tail[0] == head[0]:
                    tail = (tail[0], tail[1] + 1)
                elif tail[0] < head[0]:
                    tail = (tail[0] + 1, tail[1] + 1)
                else: 
                    tail = (tail[0] - 1, tail[1] + 1)
            elif tail[1] - 1 > head[1]:
                if tail[0] == head[0]:
                    tail = (tail[0], tail[1] - 1)
                elif tail[0] < head[0]:
                    tail = (tail[0] + 1, tail[1] - 1)
                else: 
                    tail = (tail[0] - 1, tail[1] - 1)
            elif tail[0] + 1 < head[0]:
                if tail[1] == head[1]:
                    tail = (tail[0] + 1, tail[1])
                elif tail[1] < head[1]:
                    tail = (tail[0] + 1, tail[1] + 1)
                else: 
                    tail = (tail[0] + 1, tail[1] - 1)
            elif tail[0] - 1 > head[0]:
                if tail[1] == head[1]:
                    tail = (tail[0] - 1, tail[1])
                elif tail[1] < head[1]:
                    tail = (tail[0] - 1, tail[1] + 1)
                else: 
                    tail = (tail[0] - 1, tail[1] - 1)
        if tail in coords:
            coords[tail] = coords[tail] + 1
        else:
            coords[tail] = 1
    return (head, tail)

with open("../inputs/day09.txt") as f:
    lines = f.readlines()
    for line in lines:
        split = (line.strip()).split(" ")
        split[1] = int(split[1])
        (h, t) = move(coords, head, tail, split)
        head = h
        tail = t
    print(len(coords))