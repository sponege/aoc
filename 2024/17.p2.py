#!/bin/python3
import sys, re
from collections import deque
from util import *

p, d, test, inp, lines = getArgs()
# if test: exit()
pp = lambda *args: [print(*args) if test else 0]
if test: exit()

from z3 import *
program = ints(lines[4])

s = Optimize()
# A = [BitVec(chr(ord('a')+i), 32) for i in range(len(program))]
aa = BitVec('a', 64)
# s.add(a/(2**(4^0b111))==0)
# for i in range(len(program)):
# program=[0,0,0,0,0,2,4]
# l=2
l=len(program)
# for i in range(5,l):
# #     s.add(program[i]^1^((A[i]>>(3*i))>>(0b10^(0b111&(A[i]>>(3*i)))))==(A[i]>>(3*i))&0b111)
#     # real_A = (A/(2**(3*i)))
#     real_A = A/(8**(i))
#     # real_A = A*(2**(3*(i)))
#     # s.add(program[i]^1^(real_A>>(0b10^(real_A%8)))^(real_A%8)==0)
#     s.add(program[i]^1^(real_A>>(0b10^(real_A%8)))^(real_A%8)==0)
a = aa
for i in range(l):
    b = a  & 0b111
    b ^= 0b10
    c = a >> b
    b ^= 0b11
    b ^= c
    a = a >> 3
    s.add(b%8 == program[i])
s.minimize(aa)
print(s.check())
ans = s.model()
print(ans)
# a = ans.eval(A)
program = ints(lines[4])

# ans = 172

# a = ints(lines[0])[0]
b = ints(lines[1])[0]
c = ints(lines[2])[0]

a = 37221334433268


print(a, b, c, program)

ip=0

out=[]

# if not test: exit()

while ip < len(program):
    i=program[ip]
    cb=program[ip+1]
    lop=cb

    assert cb != 7

    if cb > 3:
        if cb == 4: cb = a
        elif cb == 5: cb = b
        elif cb == 6: cb = c

    if i == 0:
        a = a // 2**cb
    if i == 1:
        b ^= lop
    if i == 2:
        b = cb&0b111
    if i == 3:
        if a != 0: ip = lop - 2
    if i == 4:
        b ^= c
    if i == 5:
        out += [cb%8]
    if i == 6:
        b = a // 2**cb
    if i == 7:
        c = a // 2**cb
    
    ip += 2

ans = ','.join(list(map(str, out)))

print(f'ans:{ans}')
