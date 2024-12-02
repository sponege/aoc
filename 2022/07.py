filesystem = {}
curPath = []

def getCurPath(cPath):
    return '/' + '/'.join(cPath[1:])

def getFromFS(path):
    try:
        thing = filesystem
        for d in path:
            thing = thing[d]
        return thing
    except:
        if type(thing) is list:
            return thing
        else:
            thing[d] = {}
        return thing[d]

def getDirSize(p):
    paths = [p]
    size = 0
    while len(paths) > 0:
        path = paths.pop()
        if type(path) is dict:
            for d in path:
                paths.append(path[d])
        else:
            size += path
    return size

## linear version
def traverseFS(function):
    cPaths = [[]]
    while len(cPaths) > 0:
        cPath = cPaths.pop()
        for d in getFromFS(cPath):
            ls = getFromFS(cPath + [d])
            if type(ls) is dict:
                cPaths.append(cPath + [d])
            else:
                cPath.append(d)
                function(cPath)
                cPath.pop()

dir_sizes = {}
def getDirSizes(cPath):
    global part_1
    path = getCurPath(cPath)
    dir_paths = [getCurPath(cPath[:-i]) for i in range(1, len(cPath))]
    #print(dir_paths)
    size = getDirSize(getFromFS(cPath))
    for dir_path in dir_paths:
        if dir_sizes.get(dir_path) is None:
            dir_sizes[dir_path] = size
        else:
            dir_sizes[dir_path] += size
    print(path, size)


while True:
    try:
        line = input()
    except EOFError:
        break
    if line == '':
        break
    if line.startswith('$ '):
        line = line[2:]
        case = line.split(' ')[0]
        if case == 'cd':
            path = line.split(' ')[1]
            if path == '..':
                curPath.pop()
            else:
                curPath.append(path)
                getFromFS(curPath)
        elif case == 'ls':
           continue
    else:
       operands = line.split(' ')
       if operands[0] == 'dir':
           continue
       else:
          fileSize = int(operands[0])
          fileName = operands[1]
          getFromFS(curPath)[fileName] = fileSize
#print(filesystem)
traverseFS(getDirSizes)
print("Directory sizes:")
part_1 = 0
for d in dir_sizes:
    dir_name = d
    dir_size = dir_sizes[d]
    if dir_size <= 100000:
        part_1 += dir_size
    print(dir_name, dir_size)
free_space = 70000000 - dir_sizes['/']
needed_space = 30000000 - free_space
dirs_to_remove = {d: dir_sizes[d] for d in dir_sizes if dir_sizes[d] >= needed_space}
# sort by size
dirs_to_remove = sorted(dirs_to_remove.items(), key=lambda x: x[1])
print("Root directory size:", dir_sizes['/'])
print("Directories to remove:", dirs_to_remove)
dir_to_remove = dirs_to_remove[0]
dir_name = dir_to_remove[0]
dir_size = dir_to_remove[1]
print("Minimum size that needs to be removed:", needed_space)
print("Directory to remove:", dir_name)
print("Answer for part 1:", part_1)
print("Answer for part 2:", dir_size)

