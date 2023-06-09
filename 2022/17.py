#!/bin/python3

import sys
from util import *
inp = sys.stdin.read()
lines = inp.splitlines()

split = lambda s: s.split('\n')


print(sys.argv)
debug = 'd' in sys.argv[1] if len(sys.argv) > 1 else 0

if not debug:
    real_print = print
    print = lambda *args, **kwargs: 0
    rpb = print_board
    print_board = lambda *args, **kwargs: 0

rocks = lm(split,"""####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split('\n\n'))


cl = 7

print(rocks)

chamber = {}
chamber[(-1,0)]='|'
chamber[(-1,1)]='+'
chamber[(-2,2)]='+'
chamber[(cl,0)]='|'
chamber[(cl,1)]='+'

for x in range(cl):
    chamber[(x,1)]='-'

def draw(t, s=True):
    rn,x,y=t
    global chamber
    nc=chamber.copy()
    for dy, l in enumerate(rocks[rn]):
        cy=dy-y
        nc[(-1,cy)]='|'
        nc[(cl,cy)]='|'
        for dx in range(len(l)):
            cx=dx+x
            if cx < 0 or cx > cl or cy > 0:
                raise Exception(f"Wrong coord ({cx}, {-cy})")
            if l[dx] == '#': nc[(cx,cy)]=chr(ord('1')+rn)
    if s:
        chamber=nc
    return nc

getpx = lambda x,y: chamber[(x,-y)] if (x,-y) in chamber else '.'

#draw((1,0,2))
#print_board(draw((2,3,5),s=0))
# 1,000,000,000,000

print(getpx(4,10))

if debug:
    rounds = 10
else:rounds=4603
p1t = 2022
p1a='no answer found'
#rounds=len(inp)*3
if not debug:print=real_print
print(f"Performing {rounds} rounds")
if not debug:print=lambda *args, **kwargs: 0
#else:rounds=2022
_=1
rn=0
xa=2
ya=3
j=0

def collision(nr):
    c=0
    for dx in range(rw):
        for dy in range(rh):
            print(dx, dy,rocks[nr[0]], rocks[nr[0]][dy][dx],getpx(nr[1]+dx,nr[2]-dy))
            if getpx(nr[1]+dx,nr[2]-dy) != '.' and rocks[nr[0]][dy][dx] != '.':
                print('collision detected')
                print(nr)
                c=1
                break
        if c:
            break
    return c

d=0
mys=[]
while 1:
    rc=[coord[1] for coord, cell in chamber.items() if cell != '|' and cell != '+' and cell != '-'] ## real chamber
    print('chamber', rc)
    miny, maxy = min_max(rc) if len(rc) > 1 else (1, 1)
    miny, maxy = (-maxy, -miny)
    if _-1 == p1t: p1a = maxy+1
    mys.append((maxy-mys[-1][1], maxy) if len(mys) > 0 else (maxy, maxy))
    nr=[rn,xa,ya+maxy+len(rocks[rn])]
    rw=len(rocks[rn][0])
    rh=len(rocks[rn])

    print("New rock!")
    print(rw,rh)
    print('max y', maxy, 'min y', miny)
    print(f"{_-1} rocks have fallen")
    print_board(draw(nr,s=0))
    
    while 1: # rock moving
        # jet push
        c=1
        dx=1 if inp[j]=='>' else -1
        if nr[1]+dx+rw<=cl and nr[1]+dx>=0:
            c=0
            nr[1]+=dx
            if collision(nr):
                c=1
                nr[1]-=dx
            else:
                print("Jet of gas pushes rock", 'right' if dx == 1 else 'left')
        
        if c:

            print("Jet of gas pushes rock", ('right' if dx == 1 else 'left') + ", but nothing happened")
        print_board(draw(nr,s=0))


        # next jet stream
        j+=1
        j%=len(inp)-1

        # gravity:
        # check for collision
        print("Rock falls 1 unit")
        nr[2]-=1
        c=collision(nr)
        nr[2]+=1

        if c:
            break
        else:
            nr[2]-=1
        
        print_board(draw(nr,s=0))

    draw(nr)
    print()
    if _>=rounds:
        break
    _+=1
    rn+=1
    rn%=len(rocks)

    print("Deleting shit")
    # remove items from chamber that are 50 below the highest rock
    for coord, cell in chamber.copy().items():
        if -coord[1] < maxy-50:
            d+=1
            del chamber[coord]


    if not debug:
        # go to beginning of line
        real_print(chr(27) + "[1A", end='')
        # delete line
        real_print(chr(27) + "[2K", end='')
        # go to beginning of line
        real_print(chr(27) + "[1A", end='')
        real_print(f"Performing {rounds} rounds, {_} rocks have fallen, {d} items have been deleted")
        sys.stdout.flush()

#11:36:49

if not debug:
    print = real_print
    print_board = rpb

#print_board(chamber)

print("Part 1:",p1a)
print(_)
i_one = lambda x: x[0]
i_two = lambda x: x[1]
mysh=lm(i_two,mys)[1:]
mys=lm(i_one,mys)[1:]
print(mys[663:2363]==mys[2363:(663+1700*2)])
print(mys[657:657+1700]==mys[657+1700:(657+1700*2)])
psqs=[]
def find_seq_len(seq):
    for _ in range(1,len(seq)):
        #if _ < 10: print(seq[0:_],seq[_:2*_])
        if seq[0:_]==seq[_:2*_]:
            return _
    return 0
for start_seq in range(1,len(mys),len(rocks)):
    seq_len=find_seq_len(mys[start_seq:])
    if seq_len != 0:
        psqs.append((seq_len,start_seq))
psqs.sort(key=i_one,reverse=1)
lsq=psqs[0]#largest sequence
trillion=2022
trillion=1000000000000
seq_len,start_seq=lsq
start_range_height = mysh[start_seq]
repeat_height = mysh[start_seq+seq_len]-mysh[start_seq]
end_seq_len=(trillion-start_seq)%seq_len
end_seq=trillion-end_seq_len
end_seq_height=mysh[start_seq+end_seq_len]
n_sequences=(end_seq-start_seq)/seq_len

print("Number of rocks placed:", trillion)
print("Sequence length:", seq_len)
print("Starting sequence position:", start_seq)
print("Height before first sequence starts:",start_range_height)
print("Height of each repeating sequence:", repeat_height)
print("Length of cut off ending sequence:", end_seq_len)
print("End sequence position:", end_seq)
print("End sequence height:", end_seq_height)
print("Number of sequences:", n_sequences)
n_sequences = int(n_sequences)
height_all_seqs=(repeat_height*n_sequences)
print("Height of all sequences:", height_all_seqs)

total_height = end_seq_height + height_all_seqs
print("Total height:", total_height)
