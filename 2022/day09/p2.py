coords = {}
rope = [(0,0) for i in range(10)]

def check_adj(tail, head):
    lst = []
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            lst.append((tail[0]+x, tail[1]+y))
    if head in lst:
        return True
    else:
        return False

def move_head(head, dir):
    if dir == "U":
        head = (head[0], head[1] + 1)
    elif dir == "R":
        head = (head[0] + 1, head[1])
    elif dir == "L":
        head = (head[0] - 1, head[1])
    else:
        head = (head[0], head[1] - 1)
    return head

def move_body(head, tail, dir):
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
    return (head, tail)

def move_rope (rope, step):
    for k in range(step[1]):
        rope[0] = move_head(rope[0], step[0])
        for i in range(0, len(rope)-1, 1):
            (h,t) = move_body(rope[i], rope[i+1], step[0])
            rope[i] = h
            rope[i+1] = t
        tail = rope[len(rope)-1]
        if tail in coords:
            coords[tail] = coords[tail] + 1
        else:
            coords[tail] = 1
    return rope

with open("../inputs/day09.txt") as f:
    lines = f.readlines()
    for line in lines:
        split = (line.strip()).split(" ")
        split[1] = int(split[1])
        rope = move_rope(rope, split)
    print(len(coords))