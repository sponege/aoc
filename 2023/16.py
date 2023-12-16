#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

ans = 0

g = [list(l) for l in lines]

beams=[[0,0,'>']]
def run():
    global beams
    x,y,dir=beams[0]
    nbs=[]
    c=g[y][x]
    dx,dy=[[0,-1],[0,1],[1,0],[-1,0]]["^v><".index(dir)]
    if c =='.':
        nbs.append([x,y,dir])
    elif c == '/':
        nbs.append([x,y,"^v<>"["><v^".index(dir)]])
    elif c == '\\':
        nbs.append([x,y,"^v<>"["<>^v".index(dir)]])
    elif c == '|' and dx!=0:
        nbs.append([x,y,"^"])
        nbs.append([x,y,"v"])
    elif c == '-' and dy!=0:
        nbs.append([x,y,'<'])
        nbs.append([x,y,'>'])
    else:
        nbs.append([x,y,dir])
    beams=nbs
    e=set()
    d=set()
    while len(beams)>0:
        nbs=[]

        for x,y,dir in beams:
            e.add((x,y))
            dx,dy=[[0,-1],[0,1],[1,0],[-1,0]]["^v><".index(dir)]
            x+=dx
            y+=dy
            if x<0 or x>len(g[0])-1 or y<0 or y>len(g)-1: continue
            e.add((x,y))
            if (x,y,dir) in d: continue
            d.add((x,y,dir))
            c=g[y][x]
            if c =='.':
                nbs.append([x,y,dir])
            elif c == '/':
                nbs.append([x,y,"^v<>"["><v^".index(dir)]])
            elif c == '\\':
                nbs.append([x,y,"^v<>"["<>^v".index(dir)]])
            elif c == '|' and dx!=0:
                nbs.append([x,y,"^"])
                nbs.append([x,y,"v"])
            elif c == '-' and dy!=0:
                nbs.append([x,y,'<'])
                nbs.append([x,y,'>'])
            else:
                nbs.append([x,y,dir])


        beams=nbs
        # print(beams)
    return e
if p == 1:
    e=run()
    ans=len(e)
if p == 2:
    for b in [[x,0,'v'] for x in range(len(g[0]))]:
        beams = [b]
        e=run()
        ans=max(ans,len(e))
    for b in [[x,len(g)-1,'^'] for x in range(len(g[0]))]:
        beams = [b]
        e=run()
        ans=max(ans,len(e))
    for b in [[0,y,'>'] for y in range(len(g))]:
        beams = [b]
        e=run()
        ans=max(ans,len(e))
    for b in [[len(g[0])-1,y,'<'] for y in range(len(g))]:
        beams = [b]
        e=run()
        ans=max(ans,len(e))
    pass
## submit answer you got to the utils function
final(t, p, ans, expected_ans)