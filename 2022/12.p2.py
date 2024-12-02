import sys, os, time
inp = sys.stdin.read()
lines = inp.splitlines()

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
    print()

    path=list(path)

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x,y) in path:
                loc=path.index((x,y))
                if loc%(26*2)>25:
                    loc %= 26
                    c=chr(ord('A')+loc)
                else:
                    loc %= 26
                    c=chr(ord('a')+loc)
                printCyan(c)
                continue
            print(lines[y][x],end='')
        print()

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

def findAll(l):
    for _ in range(len(lines)):
        line = lines[_]
        if l in line:
            yield (line.find(l), _)

#print(locate(goal))
sps = []
#while 1:
_=0
newpositions=[]
def travmaze():
    global paths, sps, _, newpositions
    while len(paths) > 0:
        _+=1
        #print(":)",_, len(paths))
        biggestlengthpath=0


    #    print(unique(paths))
        nps=[]
        s = 15
        px=7
        py=1
        for path in paths:
            path = list(path)
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
                    c='a'
                if nc == 'E':
                    nc='z'
                if (not posinpath(path[:-1], pos)) and nc != 'S' and ((ord(c)+1 >= ord(nc))):
                    #print(c,nc)
                    nc=ogn
                    c=og
                    if nc == 'E':
                        path.append(newPos[:])
                        sps.append(tuple(path))
                        return
                    path.append(newPos[:])
                    if len(path) > biggestlengthpath:
                        biggestlengthpath = len(path)
                    while len(newpositions) < biggestlengthpath:
                        newpositions.append(set())
                    no = newPos in newpositions[len(path)-1]
                    if no:
                        path.pop()
                        continue
                    if 0:#len(path) == 31 and newPos == (4, 2):
                        print("no" if no else "ok", len(path))
                    #print('\033[2J')
                    #fancyPrintPath(path)
                    #time.sleep(.5)

                    newpositions[len(path)-1].add(newPos)
                    nps.append(tuple(path[:]))
                    path.pop()
        paths=nps
        #print(paths)
    #for path in paths:
    #    print(path, [locate(pos) for pos in path])
    #print(sps)
    #print([locate(pos) for pos in cp]) 

def part2():
    global paths
    startelevationpositions = [pos for pos in findAll('a')]
    sep = startelevationpositions

    #print(sep)
    #print([locate(p) for p in sep])

    nps=newpositions
    fancyPrintPath(sep)
    
    for sp in sep:
        paths = []
        paths.append((tuple(sp),))
        travmaze()

part2()


print()
if len(sps)==0:
    print("Algorithm failed")
else:
    sps=list(sps)
    sps=sorted(sps,key=len)
    print("Shortest path:", len(sps[0])-1)


    fancyPrintPath(sps[0])
