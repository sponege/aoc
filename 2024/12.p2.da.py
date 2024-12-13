#!/bin/python3

import sys, re
from util import *

p, d, test, inp, lines = getArgs()
pp = lambda *args: [print(*args) if test else 0]

ans=0

inp=inp.strip()
# print('read everything')

g = [[c for c in l] for l in lines]
if test: print(g)

h=len(g)
w=len(g[0])

d2=[[0,1],[-1,0],[0,-1],[1,0]]
seen=set()
def check(x,y):
    return x >= 0 and x < w and y >= 0 and y < h

for y in range(h):
    for x in range(w):
        if (x,y) in seen:continue
        t=g[y][x]
        ps=[(x,y)]
        c=set()
        d=set()
        xs=[]
        ys=[]
        while len(ps):
            cx,cy=ps.pop()
            
            c.add((cx,cy))
            # if (cx,cy) in seen:continue
            seen|={(cx,cy)}
            for dx,dy in d2:
                nx,ny=cx+dx,cy+dy
                if check(nx,ny) and (nx,ny) not in seen and g[ny][nx] == t:
                    ps+=[(nx,ny)]
                else:
                    # onx=nx
                    # ony=ny
                    if check(nx,ny) and g[ny][nx] == t: continue
                    cancel=(nx,ny) in c
                    nx=cx+dx
                    ny=cy+dy
                    chx,chy=d2[(d2.index([dx,dy])+1)%4]

                    while 1:
                        nx+=chx
                        ny+=chy
                        if not ((check(nx,ny) and g[ny][nx] != t) or (not check(nx,ny) and -1 <= nx < w+1 and -1 <= ny < h+1)): break

                        cnx=nx-dx
                        cny=ny-dy

                        if not ((check(cnx,cny) and g[cny][cnx] == t) or (not check(cnx,cny))): 

                            break

                    # if nx in xs:
                    # for lx, ly in d:
                    #     if lx == nx:
                    #         nx=onx
                    #         ny=ony
                    #         chy = -1 if ny > ly else 1
                    #         while ly != ny and (not check(nx,ny) or g[ny][nx] != t):
                    #             ny += chy
                    #         # if not check(nx,ny):
                    #         #     # print(cx,cy,chy,ly,cy,'asdf'); 
                    #         #     continue
                    #             # pass
                    #         if ny == ly: cancel=1;break
                    # # if ny in ys:
                    # for lx, ly in d:
                    #     if ly == ny:
                    #         nx=onx
                    #         ny=ony
                    #         chx = -1 if nx > lx else 1
                    #         while lx != nx and (not check(nx,ny) or g[ny][nx] != t): 
                    #             nx += chx
                    #         # if not check(nx,ny): continue
                    #         if nx == lx: cancel=1;break
                    
                    # cx=ocx
                    # cy=ocy
                    # print(cancel)
                    # if cancel: continue
                    d.add((nx,ny,d2.index([dx,dy])))
                    # xs+=[nx]
                    # ys+=[ny]
        # d -= set(c)
        # if test: print(c,len(d))
        if test:
            print(t, len(c), len(d), c, d)
            gg = {}
            for aax,aay in c:
                gg[(aax,aay)] = t
            # for aax,aay in d:
            #     gg[(aax,aay)] = 'a'
            # print_board(gg)
        ans += (len(c)) * len(d)


print(f'ans:{ans}')
