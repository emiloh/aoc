class File:
    def __init__(self, dir, name, size):
        self.dir = dir
        self.name = name
        self.size = size
        self.parent = None
        self.files = []
    
    def size(self):
        total = self.size
        for file in self.files:
            total += file.size
        return total 
    
    def addFile(self, File):
        File.parent = self
        self.files.append(File)

    def contains(self, name):
        for file in self.files:
            if file.name == name:
                return True
        return False
    
    def cd(self, name):
        if name == "..":
            return self.parent
        else:
            for file in self.files:
                if file.name == name:
                    return file
    
    def ls(self, indent):
        print(self)
        print((indent + 2) * " ", end="")
        for file in self.files:
            file.ls(indent + 2)

    def update_size(self):
        total_size = self.size
        for file in self.files:
            total_size += file.update_size()
        self.size = total_size
        return self.size
    
    def under(self, threshhold):
        lst = []
        if self.size <= threshhold: lst.append(self.size)
        for file in self.files:
            if file.dir:
                lst = lst + file.under(threshhold)
        return lst

    def __str__(self):
        return f"{self.name}({self.dir}) - {self.size}"
    

with open("/Users/eh/Documents/aoc/2022/inputs/day07.txt") as f:
    lines = f.readlines()
    root = None
    cwd = None
    i = 0
    while i <= len(lines)-1:
        split = (lines[i].strip()).split(" ")
        print(split)
        if "$" in split[0]:
            if "cd" in split[1]:
                if root == None:
                    root = File(True, "/", 0)
                    cwd = root
                else:
                    if split[2] == "/":
                        cwd = root
                    else: 
                        cwd = cwd.cd(split[2])
        else:
            counter = 0
            
            while counter + i < len(lines):
                nsplit = (lines[i+counter].strip()).split(" ")
                if nsplit[0] == "$":
                    break
                elif nsplit[0] == "dir":
                    cwd.addFile(File(True, nsplit[1], 0))
                else:
                    cwd.addFile(File(False, nsplit[1], int(nsplit[0])))
                counter += 1
                print(counter)
            
            i += counter - 1
        i += 1
    #update sizes
    root.update_size()
    root.ls(0)
    sizes = root.under(70000000)
    unused = 70000000
    sizes = sorted(sizes, reverse=True)
    unused -= sizes[0]
    least = 70000000
    print(sizes, unused)
    for size in sizes:
        if size + unused >= 30000000:
            least = size
    print(least)