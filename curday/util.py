#!/bin/python3

# very useful utils for aoc
import sys

# progStartTime = time.time()

oldPrint = print
print = lambda *args: oldPrint(*args, flush=1)

# list map: create list from mapping
lm=lambda f,l:list(map(f,l))
# tm=lambda f,l:t(map(f,l))

# range length, self explanatory
rl=lambda t:range(len(t))
lrl=lambda t:list(range(len(t)))

# enumerate
e=enumerate
le=lambda l:list(e(l))

# splitters!
splitter = lambda c: lambda s: s.split(c)

# nested mappings
# ex: nm(int)([['1','2','3'], ['4','5','6']])
# returns: [[1, 2, 3], [4, 5, 6]]
nm = lambda f: lambda l: lm(lambda x: f(x), l)

# index mappings
# ex: im(1, [['a', 'b', 'c'], ['d', 'e', 'f']])
# returns: ['b', 'e']
# ex: im('age', [{'name': 'bob', 'age': 20}, {'name': 'alice', 'age': 21}])
# returns: [20, 21]
im = lambda i, l: lm(lambda x: x[i], l)

# multiple mappings!
# fs - order of functions to map with it
# example: lms([splitter('x'), nm(int), tuple], ['2x3x4', '3x4x5'])
# returns: [(2, 3, 4), (3, 4, 5)]
def lms(fs, l):
    for f in fs:
        l = lm(f, l)
    return l

## regex mappings!
# ex: rm(r'\d+', ['1a2b3c', '4d5e6f'])
# returns:
# [['1', '2', '3'], ['4', '5', '6']]
# ex: rm(r'(\d+)-(\d+) (\w): (\w+)', ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: ccccccccc'])
# returns:
# [['1', '3', 'a', 'abcde'], ['1', '3', 'b', 'cdefg'], ['2', '9', 'c', 'ccccccccc']]
# ex: rm(r'([A-Za-z]*) has (\d) kids and (\d) dogs', ['Bob has 3 kids and 2 dogs', 'Alice has 2 kids and 5 dogs'])
# returns:
# [['Bob', '3', '2'], ['Alice', '2', '5']]
# note: returns tuples
def rm(r, l):
    return lm(lambda x: re.findall(r, x)[0], l)

def getArgs():
    p = 1 # part
    d = False # debug
    t = True # testing mode

    if len(sys.argv) > 1:
        p = (2 if '2' in sys.argv[1] else 1)
        d = 'd' in sys.argv[1]
        t = 't' in sys.argv[1]

    inp = sys.stdin.read()

    lines = inp.strip().splitlines()

    return (p, d, t, inp, lines)

# examples
# sqr=lambda i:i*i
# a=[3,5,9]
# a = lm(sqr,a))
# print(a, type(a))

def findLetter(l, lines):
    for _ in range(len(lines)):
        line = lines[_]
        if l in line:
            return (line.find(l), _)

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

def min_max(nums):
    return min(nums), max(nums)

def print_board(board,ret=False):
    global minx, maxx, miny, maxy
    if len(board) > 0:
        minx, maxx = min_max([x for x, _ in board])
        miny, maxy = min_max([y for _, y in board])
    else:
        minx, maxx, miny, maxy = (0, 0, -1, 1)

    out = ''

    if ret:
        def pprint(*args, **kwargs):
            nonlocal out
            out += ''.join(map(str,args))
            if len(args) == 0:
                out += '\n'
            return out
    else:
        pprint = print
    pprint('\n')

    x_offset=max(len(str(-maxy+1)),len(str(-miny)))+2

    append_zeroes = lambda x: '0'*(len(str(maxx))-len(str(x)))+str(x)
    
    for digit in range(len(str(maxx))):
        pprint(' '*x_offset, end='')
        for x in range(minx, maxx+1):
            pass
            pprint(append_zeroes(x)[digit], end='')
        pprint()

    pprint(' '*x_offset, end='')
    sand_drop_x = 500
    pprint()

    x_offset -= 2


    for y in range(miny-1, maxy+1):
        pprint(f"{(' '*(x_offset-len(str(y))))+str(y)} ", end='')
        for x in range(minx-1, maxx+2):
            c=board.get((x, y), '.')
            pprint(c if c!='^' else '.', end='')
        pprint()

    pprint()
    if ret:
        return out

def contains(pairs,oneway=False):
    prs = [pairs] if oneway else [pairs, pairs[::-1]]
    ## true if:
    ## --111------
    ## ----2222
    ## false if:
    ## -111-------
    ## ----22222--
    for p1, p2 in prs:
        if p1[0] <= p2[1] and p1[1] >= p2[0]:
            return 1
    return 0

def fully_contains(pairs,oneway=False):
    prs = [pairs] if oneway else [pairs, pairs[::-1]]
    ## true if:
    ## -----111---
    ## ----22222--
    ## false if:
    ## -111-------
    ## ----22222--
    for p1, p2 in prs:
        if p1[0] >= p2[0] and p1[1] <= p2[1]:
            return 1
    return 0

def find_seq_len(seq):
    for _ in range(1,len(seq)):
        #if _ < 10: print(seq[0:_],seq[_:2*_])
        if seq[0:_]==seq[_:2*_]:
            return _
    return 0

#print(find_seq_len([2,3,0,2,3,0]))
#print(find_seq_len([2,3,0,2,3,1]))

# some nice colors for output coloring :)
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

addP = lambda p1, p2: (p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2]) if len(p1) == 3 else (p1[0]+p2[0],p1[1]+p2[1])
