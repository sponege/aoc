#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None


# my terrible solution that probably doesn't work on real input ;-;
# BFS doesn't work this day :(
ans = 0
g = [list(l) for l in lines]
# print(g)
ps=[[0,0,3,'>',0],[0,0,3,'v',0]]
f=[]

visited={}

while len(ps)>0:
    nps=[]
    print(len(ps))
    for x,y,sl,dir,s in ps: # steps left, score
        dx,dy=[[0,-1],[0,1],[1,0],[-1,0]]["^v><".index(dir)]
        x+=dx
        y+=dy
        if not (x<0 or x>len(g[0])-1 or y<0 or y>len(g)-1):
            sl-=1
            if sl:
                nps.append((x,y,sl,dir,s+int(g[y][x])))
        x-=dx
        y-=dy
        dir = '<>^v'["^v><".index(dir)]
        dx,dy=[[0,-1],[0,1],[1,0],[-1,0]]["^v><".index(dir)]

        x+=dx
        y+=dy
        if not (x<0 or x>len(g[0])-1 or y<0 or y>len(g)-1):
            nps.append((x,y,3,dir,s+int(g[y][x])))
        x-=dx
        y-=dy
        dir = 'v^<>'["^v><".index(dir)]
        dx,dy=[[0,-1],[0,1],[1,0],[-1,0]]["^v><".index(dir)]
        x+=dx
        y+=dy
        if not (x<0 or x>len(g[0])-1 or y<0 or y>len(g)-1):
            nps.append((x,y,3,dir,s+int(g[y][x])))
    nnps=[]
    for x,y,sl,dir,s in nps:
        if x == len(g[0])-1 and y == len(g)-1: f.append(s)
        if (x,y) in visited and visited[(x,y)]<s: continue
        visited[(x,y)]=s
        nnps.append((x,y,sl,dir,s))
    ps=nnps
# print(visited)
ans = min(f)
# print(ans, f)
# print(visited[(5,1,'>')])
## submit answer you got to the utils function
final(t, p, ans, expected_ans)