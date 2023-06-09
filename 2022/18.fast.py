#!/bin/python3

import sys
from util import *
inp = sys.stdin.read()
lines = inp.splitlines()

v = 0
if len(sys.argv) > 1:
    v = 'v' in sys.argv[1]

def getCoords(line):
    return tm(int, line.split(','))

lava = lm(getCoords, lines)

gx = lambda c: c[0]
gy = lambda c: c[1]
gz = lambda c: c[2]
mx, Mx = min_max(lm(gx,lava))
my, My = min_max(lm(gy,lava))
mz, Mz = min_max(lm(gz,lava))

print(f"min x {mx} max x {Mx}")
print(f"min y {my} max y {My}")
print(f"min z {mz} max z {Mz}")

if v:
    import matplotlib
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D 
    import numpy as np

    # Create axis
    axes = [Mx, My, Mz]
    # Create Data
    data = np.zeros(axes)
    print(data)
    for c in lava:
        x,y,z=c
        #if y != 4: continue
        data[x-1][y-1][z-1]=1
    #data = np.meshgrid(lava)
    # Control Transparency
    alpha = 0.9
    # Control colour
    colors = np.empty(axes + [4], dtype=np.float32)
    colors[:] = [1, 0, 0, alpha]  # red
    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Voxels is used to customizations of the
    # sizes, positions and colors.
    ax.voxels(data, facecolors=colors)
    matplotlib.use('TkAgg')
    plt.show()
    exit()


def touching(a,b):
    dx, dy, dz = (a[0]-b[0],a[1]-b[1],a[2]-b[2])
    dx = abs(dx)
    dy = abs(dy)
    dz = abs(dz)
    c = (dx, dy, dz)
    return c.count(1) == 1 and c.count(0) == 2
#print(touching([0,0,1],[0,0,2]))

def eq(a,b):
    dx, dy, dz = (a[0]-b[0],a[1]-b[1],a[2]-b[2])
    dx = abs(dx)
    dy = abs(dy)
    dz = abs(dz)
    c = (dx, dy, dz)
    return c.count(0) == 3
    return c.count(1) == 1 and c.count(0) == 2

all_dirs = [
    (0, 1, 0),
    (0, -1, 0),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 0, 1),
    (0, 0, -1)
]
addP = lambda p1, p2: (p1[0]+p2[0],p1[1]+p2[1],p1[2]+p2[2])

p1 = (len(lava)*6)
for a in lava:
    for d in all_dirs:
        if addP(a,d) in lava: p1 -= 1


print("Part 1:",p1)
p2 = p1

stationary = [0, 0]
moving = [1, -1]

covered_lava = []
ps = set()

vps = {}

def surrounded_by_lava(_p,op):
    global covered_lava, ps
    if _p in ps:
        ps.remove(_p)
        #print(f"Deleted {_p}, full visited points: {vp}")
    if op not in vps:
        vps[op] = set()
    vps[op].add(_p)

    x,y,z=_p
    if x < mx or x > Mx or y < my or y > My or z < mz or z > Mz:
        #print("out of bounds",_p)
        covered_lava = []
        return 0
    tp = [5,2,2]
    #if _p == tp or tp in vp:
    #    print(_p, vp)
    #if len(vp) > 0 and _p in vp:
    #    pass
        #print(vp)
    if _p in lava:
        return 1
    surrounded = not _p in lava
    for d in all_dirs:
        p = (x+d[0],y+d[1],z+d[2])
        if p in lava:
            covered_lava.append(p)
        elif p not in vps[op]:
            surrounded = surrounded_by_lava(p,op)
            if not surrounded: return 0
    return surrounded 

"""
for x in range(mx, Mx):
    for y in range(my, My):
        for z in range(mz, Mz):
            p=(x,y,z)
            
            ps.add(p)
"""


for p in lava:
    for d in all_dirs:
        ps.add(addP(p,d))

while len(ps) > 0:
    covered_lava = []
    p = ps.pop()
    air = p not in lava
    if air:
        air = surrounded_by_lava(p,p)

    #air = 1
    #for p in lrl(lava):
    #    if not eq([x,y,z],lava[p]):
    #        air = 0
    #    if not air: break
    if air:
        p2 -= len(covered_lava)
        #print("Surface area of inside crater:", len(covered_lava))
    else:
        pass
        #print("not doing anything because out of bounds")

print("Part 2:", p2)
submit(2, p2)
