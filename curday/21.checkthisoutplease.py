#!/bin/python3

# this video is sponsored by taco bell

import sys, re
from util import *
from collections import deque, defaultdict

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip()
print('read everything')

# x,y=findLetter('S',lines)
# sx,sy=x,y
# ex,ey=findLetter('E',lines)
g = [list(l) for l in lines]


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


robotpad = """.^A
<v>"""
robotpad = [list(l) for l in robotpad.splitlines()]
print(robotpad)
# w=len(robotpad[0])
# h=len(robotpad)

import itertools

def entercode(padaa, codes, ssx, ssy):
    global d2
    w=len(padaa[0])
    h=len(padaa)
    all_paths = []
    # print(codes)

    x, y = [ssx,ssy]
    for code_parts in codes:
        # print('parts', code_parts)
        rx,ry=x,y
        for part in code_parts:
            x,y=rx,ry
            # print('part', part)


            for c in part:
                paths = set()

                # print(f'doing {c} from {x},{y}')
                ps = deque([[x,y,'',set()]])
                # print(padaa)
                gx, gy = findLetter(c, padaa)
                # print(gx, gy)
                seen=set()
                while ps:
                    # print(ps)
                    cx,cy,path,seen = ps.popleft()
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
                paths.sort(key=len)
                smallest=len(paths[0])
                paths = list(filter(lambda p: len(p) == smallest, paths))
                # print('a', paths)
                all_paths += [paths]
    # print('return', all_paths)
    return all_paths

for code in lines:
    codes = entercode(numpad, [[code]], 2, 3)
    # print(codes)
    codes2 = entercode(robotpad, codes, 2, 0)
    # codes2 = entercode(robotpad, ['<A^A>^^AvvvA'], 2, 0)
    # codes3 = codes2
    codes3 = entercode(robotpad, codes2, 2, 0)
    # codes3 = entercode(robotpad, codes3)

    f = ''
    for part in codes3:
        part.sort(key=len)
        # print(part)
        f += part[0]
    # f = ''.join(codes3)
    # 179A issues
    # print(''.join(codes3))

    print(len(f), ints(code))
    print(f'{code}: {f}')
    ans += len(f) * ints(code)[0]
    # for i,code in enumerate(codes):
    #     print(code)

print(f'ans:{ans}')


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

<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
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

#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v<A<AA>^>Av<<A>A<A>^>AvA^<Av>A^AvAA^<A>Av<<A>^>AvA^Av<<A>^>AAv<A>A^AvA<A^>A<A>Av<<A>^>Av<A>A^AvA<A^>A<Av<A>^>Av<<A>^A>AvA^Av<A^>A<Av<A>^>Av<<A>^A>AAvA^Av<A<A>^>Av<<A>A^>AAA<Av>A^AvA^<A>A