<<<<<<< HEAD
#!/bin/python3

# this video is sponsored by taco bell

=======
>>>>>>> ee7cd9e8adec6edc9eab2467ad577fa203a410ff
import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()
<<<<<<< HEAD
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0
=======

ans=0

inp=inp.strip()
print('read everything')

# x,y=findLetter('S',lines)
# sx,sy=x,y
# ex,ey=findLetter('E',lines)
g = [list(l) for l in lines]
>>>>>>> ee7cd9e8adec6edc9eab2467ad577fa203a410ff

inp=inp.strip()
print('read everything')

<<<<<<< HEAD
from collections import deque
=======
d2=[[0,1],[0,-1],[-1,0],[1,0]]
ds='v^<>'
def check(x,y,w,h,padaa):
    return x >= 0 and x < w and y >= 0 and y < h and padaa[y][x] not in '.'
dp={}

def get(x,y):
    if (x,y) in dp: return dp[(x,y)]
    else: return float('inf')

def directions(cx,cy):
    count=0
    for dx,dy in d2:
        nx,ny=cx+dx,cy+dy
        if check(nx,ny) and g[ny][nx] not in '#': count += 1
    return count

numpad = """789
456
123
.0A"""
numpad = [list(l) for l in numpad.splitlines()]
print(numpad)
>>>>>>> ee7cd9e8adec6edc9eab2467ad577fa203a410ff

def mix(v, sn):
    return v ^ sn

def prune(sn):
    return sn % 16777216

prices = []
changes = []

# if not test: exit()

for t in lines:
    sn = int(t)
    first_2000 = []
    
    first_2000.append(sn%10)
    for i in range(2000):
        sn = prune(mix(sn*64, sn))
        sn = mix(sn//32, sn)
        sn = prune(sn)
        sn = mix(sn*2048, sn)
        sn = prune(sn)
        
        first_2000.append(sn%10)
    prices += [first_2000]
    changes += [[first_2000[i]-first_2000[i-1] for i in range(1, 2001)]]

    if test: print(sn)
    # ans += sn
# print(changes[0])
maxbananas = 0

# if not test: exit()
from collections import defaultdict
lut = defaultdict(int)

for j,cl in enumerate(changes):
    seen = set()
    for i in range(1997):
        key = (cl[i], cl[i+1], cl[i+2], cl[i+3])
        if key in seen: continue
        lut[key] += prices[j][i+4]
        seen.add(key)

# if test: print([a for a in lut.values() if len(a) > 2])

# print(lut[(-2,1,-1,3)])
# lut.sort(key=lambda x: sum(x[1]), reverse=True)
# lut = list(lut.values())
# lut.sort(key=sum)
# print(lut[-1])
maxbananas = max(lut.values())

# for x in range(-10, 10):
#     print(f'{x=}')
#     for y in range(-10, 10):
#         print(f'{y=}')
#         for z in range(-10, 10):
#             print(f'{z=}')

#             for a in range(-10, 10):
                
#                 bananas = 0
#                 for j,cl in enumerate(changes):
#                     for i in range(1997):
#                         if cl[i] == x and cl[i+1] == y and cl[i+2] == z and cl[i+3] == a:
#                             bananas += prices[j][i+4]
#                             break
#                 # if bananas > maxbananas:
#                 #     print(x, y, z, a, bananas)
#                 maxbananas = max(bananas, maxbananas)
ans = maxbananas

<<<<<<< HEAD
=======
robotpad = """.^A
<v>"""
robotpad = [list(l) for l in robotpad.splitlines()]
print(robotpad)
# w=len(robotpad[0])
# h=len(robotpad)

import itertools

#v<<A^>>A<A>A<AAv>A^A<Av>A^<A>AvA^<AA>Av<AAA^>A
#v<<A>>^A<A>AvA<^AA>A<vAAA>^A

def entercode(padaa, paths, ssx, ssy, debug=False):
    global d2
    w=len(padaa[0])
    h=len(padaa)
    all_paths = []
    # print(codes)

    x, y = [ssx,ssy]
    for fuck in paths:
        for codes in fuck:
            all_possible_part_paths = [[] for j in range(len(codes))] # FOR MULTIPLE CHARACTERS
            # all_possible_part_paths = [] # FOR MULTIPLE CHARACTERS

            for j,code_parts in enumerate(codes):
                # print('parts', code_parts)
                rx,ry=x,y
                for part in code_parts:

                    all_current_paths = [[] for i in range(len(part))] # FOR ONE CHARACTER
                    x,y=rx,ry
                    if debug: print('part', part)


                    for i,c in enumerate(part):
                        paths = set()

                        # print(f'doing {c} from {x},{y}')
                        ps = deque([[x,y,'',set()]])
                        # print(padaa)
                        gx, gy = findLetter(c, padaa)
                        # print(gx, gy)
                        # seen=set()
                        while ps:
                            # print(ps)
                            cx,cy,path,seen = ps.popleft()
                            if all(z in path for z in '^v') or all(z in path for z in '<>'): continue
                            if padaa[cy][cx] == c:
                                # x,y = cx,cy
                                # print(path)
                                # path += 'A'
                                # full_path += path
                                # print(padaa[cy][cx], path, x, y)
                                # paths += [''+path]
                                # print('paths',paths)
                                paths.add(path + 'A')
                                # break
                                continue
                                # all_paths += [path]
                                


                            if (cx,cy) in seen: continue
                            # seen.add((cx,cy))
                            for dx,dy in d2:
                                nx,ny = cx+dx,cy+dy
                                # print(nx,ny)
                                if check(nx,ny,w,h,padaa):
                                    pass
                                    ps.append([nx,ny, path + ds[d2.index([dx,dy])], seen|set({(cx,cy)})])
                                    # ps.append([nx,ny, path + [[dx,dy,nx,ny]]])
                        x,y=gx,gy
                        paths=list(paths)
                        # paths = list(filter(lambda p: len(p) == smallest, paths))
                        # print('a', paths)
                        # all_paths += [paths]
                        all_current_paths[i] += paths
                    all_possible_part_paths[j] += [all_current_paths]
                    if debug: print('current paths', j, all_current_paths)
                if debug: print(f'part path {j} is finished: {all_possible_part_paths}')
            if debug: print('part paths', all_possible_part_paths)
            all_paths += all_possible_part_paths
    # all_paths.sort(key=len)
    # smallest=len(all_paths[0])
    # all_paths = list(filter(lambda p: len(p) == smallest, all_paths))
    # print('return', all_paths)
    return all_paths

#vA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# --------------------
# [['vA'], ['^A']]
# --------------------
# [['v<<A', '<v<A', '<<vA'], ['^>>A', '>^>A', '>>^A']]
# --------------------
# [['A']]
# --------------------
# [['v<A', '<vA'], ['>A'], ['^A']]
# [['vA'], ['<A'], ['^>A', '>^A']]
# --------------------
# [['<A'], ['>A']]
# --------------------
# [['v<<A', '<v<A', '<<vA'], ['^>>A', '>^>A', '>>^A']]
# --------------------
# [['v<A', '<vA'], ['>A'], ['^A']]
# [['vA'], ['<A'], ['^>A', '>^A']]
# --------------------
# [['<A'], ['v<A', '<vA'], ['^>>A', '>^>A', '>>^A']]
# [['v<<A', '<v<A', '<<vA'], ['^>A', '>^A'], ['>A']]
# --------------------
# [['vA'], ['^A']]
# --------------------
# [['v<A', '<vA'], ['^>A', '>^A']]
# --------------------
# [['<A'], ['v<A', '<vA'], ['^>>A', '>^>A', '>>^A']]
# [['v<<A', '<v<A', '<<vA'], ['^>A', '>^A'], ['>A']]
# --------------------
# [['A']]
# --------------------
# [['vA'], ['^A']]
# --------------------
# [['v<A', '<vA'], ['<A'], ['^>>A', '>^>A', '>>^A']]
# [['v<<A', '<v<A', '<<vA'], ['>A'], ['^>A', '>^A']]
# --------------------
# [['A']]
# --------------------
# [['A']]
# --------------------
# [['<A'], ['v>A', '>vA'], ['^A']]
# [['vA'], ['^<A', '<^A'], ['>A']]

for code in lines[:1]:
    codes = entercode(numpad, code, 2, 3)
    # print(codes)
    codes2 = entercode(robotpad, codes, 2, 0, debug=0)
    # print(codes2)
    # # # codes2 = entercode(robotpad, ['<A^A>^^AvvvA'], 2, 0)
    # # # codes3 = codes2
    codes3 = entercode(robotpad, codes2, 2, 0, debug=0)
    # codes3 = entercode(robotpad, codes3)

    f = ''
    for i,part in enumerate(codes3):
        # print('asdf', part)
        # print(f'asdf part {i}')

        current = None
        # current = ''
        print('-'*20)
        for path in part:
            print(path)
            # path = ''.join([[p[i] for i in range(len(p))][0] for p in path])
            path = ''.join(p[0] for p in path)
            if current is None or len(current) >= len(path): current = path

            # print('parts',path)
        # for path_index in range(len(part[0])):
        #     cur = ''
        #     for p in part:
        #         pass
        #         # print(f'{p=} {path_index=}')
        #         # cur += p[0]
        #     if current is None or len(current) > len(cur): current = cur
        f += current
            # f += part[0]
    # f = ''.join(codes3)
    # 179A issues
    # print(''.join(codes3))

    print(len(f), ints(code))
    print(f'{code}: {f}')
    ans += len(f) * ints(code)[0]
    # for i,code in enumerate(codes):
    #     print(code)

>>>>>>> ee7cd9e8adec6edc9eab2467ad577fa203a410ff
print(f'ans:{ans}')

# v<<A^>>A<A>A<AAv>A^Av<AAA^>A
# v<<A>>^A<A>AvA<^AA>A<vAAA>^A

#v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#v<<A^>>A<A>AvA^<AA>Av<AAA^>A 

#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v<A<AA^>>A<Av>AA^Av<<A^>>AvA^Av<<A^>>AAv<A>A^A<A>Av<A<A^>>AAA<Av>A^A

# #^A
# <v>
#<A^A>^^AvvvA

#>^A


#v<<A^>>A<A>A<AAv>A^Av<AAA^>A
#v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#v<<A^>>A<A>AvA<^AA>Av<AAA^>A

#<A^A>^^AvvvA
#<A^A^^>AvvvA

#v<<AA^>A>A<AA>AvAA^Av<AAA^>A

# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#789
#456
#123
#.0A

#<A^A>^^AvvvA

#v<<AA^>A>A<AA>AvAA^Av<AAA^>A
#v<A<AA^>>AA<Av>A^AvA^Av<<A^>>AAvA^Av<A^>AA<A>Av<A<A^>>AAA<Av>A^A

#

#


#.^A
#<v>

#<A^A^^>A

#>^^ better for 2 to 9

#^A<Av>A^<A>AvA^<AA>Av<AAA^>A
#v<<A>^>A<A>A<AAv>A^A<Av>A^<A>AvA^<AA>Av<AAA^>A
#REAL ABOVE


#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v<A<AA>^>Av<<A>A<A>^>AvA^<Av>A^AvAA^<A>Av<<A>^>AvA^Av<<A>^>AAv<A>A^AvA<A^>A<A>Av<<A>^>Av<A>A^AvA<A^>A<Av<A>^>Av<<A>^A>AvA^Av<A^>A<Av<A>^>Av<<A>^A>AAvA^Av<A<A>^>Av<<A>A^>AAA<Av>A^AvA^<A>A