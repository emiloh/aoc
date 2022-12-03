lower = 1
upper = 27
with open("../inputs/day03.txt") as f:
    lines = f.readlines()
    sum = 0    
    placeholder = set()
    for i in range(26):
        placeholder.add(chr(ord('a') + i))
        placeholder.add(chr(ord('A') + i))     
    all = placeholder
    counter = 0
    start = True
    for line in lines:
        rugsack = set()
        for letter in line:
            rugsack.add(letter)
        all = set.intersection(all, rugsack)
        counter += 1

        if counter == 3 and not start:
            print(all, end=" ")
            letter = all.pop()
            if letter.islower():
                sum += lower + (ord(letter) - ord('a'))
                print(sum) 
            else:
                sum += upper + (ord(letter) - ord('A'))
                print(sum)
            all = placeholder
            counter = 0
        
        start = False
        
    print(sum)