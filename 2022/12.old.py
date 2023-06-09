import sys
inp = sys.stdin.read()
lines = inp.splitlines()


def posinpath(path, pos):
    for p in path:
        if p[0] == pos[0] and p[1] == pos[1]:
            return True
    return False

def locate(pos,debug=0):
    y = pos[1]
    x = pos[0]
    if debug:
        print(lines)
        print(lines[y])
    try:
        if x < 0 or y < 0:
            raise Exception("out of range")
        return lines[y][x]
    except:
        return '~'

addPos = lambda p1, p2: (p1[0]+p2[0], p1[1]+p2[1])
cmpPos = lambda p1, p2: p1[0]==p2[0] and p1[1]==p2[1]

def findLetter(l):
    for _ in range(len(lines)):
        line = lines[_]
        if l in line:
            return (line.find(l), _)

me = findLetter('S')
goal = findLetter('E')

paths = set()
paths.add((tuple(me),))
print(locate(goal))
sps = set()
#while 1:
_=0
while len(paths) > 0:
    _+=1
    print(":)",_, len(paths))
#    print(unique(paths))
    nps = []
    path = list(paths.pop())
    s = 15
    px=7
    py=1
    if 0:#len(path) >= s and path[s-1] == (px, py):
        print("AAA", path)
        print(locate(path[-1]))

    for dir in [tuple(l) for l in [[0, 1], [0, -1], [-1, 0], [1, 0]]]:
        pos = path[-1]
        newPos = addPos(pos, dir)
        c = locate(pos)
        nc = locate(newPos)
        #print(c, pos, newPos, locate(pos), locate(newPos))
        #print(ord(locate(pos)), ord(locate(newPos)))
        #print(posInPath(path[:-1], pos))
        if 0:#nc == 'r' and c == 'c':
            print(c, nc, ord(c), ord(nc), not posinpath(path[:-1], pos) and (c == 'S' or c == 'E' or (ord(c) <= ord(nc) + 1 and ord(c) != ord(nc))))
        ## we want c to be able to steup one higher (nc+1)
        ogn=nc
        og=c
        if c == 'S':
            print(c)
            c='a'
        if nc == 'E':
            nc='z'
        if (not posinpath(path[:-1], pos)) and nc != 'S' and ((ord(c)+1 >= ord(nc))):
            #print(c,nc)
            nc=ogn
            c=og
            if nc == 'E':
                cp = path
                path.append(newPos[:])
                sps.add(tuple(path))
            no = 0
            path.append(newPos[:])
            for np in nps:
                if cmpPos(np[-1], path[-1]):
                    #print(np[-1], path[-1])
                    no = 1
                    continue
            if no: continue
            paths.add(tuple(path[:]))
            path.pop()
    #print(paths)
#for path in paths:
#    print(path, [locate(pos) for pos in path])
#print(sps)
#print([locate(pos) for pos in cp])

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printCyan(a):
    print(bcolors.OKCYAN + bcolors.BOLD + a + bcolors.ENDC, end='')

def fancyPrintPath(path):
    me='█'

    print() 
    for line in lines:
        print(line)
    print()

    path=list(path)

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x,y) in path:
                loc=path.index((x,y))
                if loc>25:
                    loc -= 26
                    c=chr(ord('A')+loc)
                else:
                    c=chr(ord('a')+loc)
                printCyan(c)
                continue
            print(lines[y][x],end='')
        print()
    

sps=list(sps)
sps=sorted(sps,key=len)
print(len(sps[0])-1)

fancyPrintPath(sps[0])
