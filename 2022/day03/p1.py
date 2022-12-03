lower = 1
upper = 27
with open("../inputs/day03.txt") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        first = line[0:(len(line)//2)]
        second = line[(len(line)//2):len(line)]
        commonF = set()
        commonS = set()
        for i in range(len(first)):
            commonF.add(first[i])
            commonS.add(second[i])
        both = set.intersection(commonF, commonS)
        letter = min(both)
        print(letter)
        if letter.islower():
            sum += lower + (ord(letter) - ord('a')) 
        else:
            sum += upper + (ord(letter) - ord('A'))
    print(sum)