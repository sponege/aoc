#!/bin/python3

# i hate this code
# i was trying to go really fast, so i wrote terrible indexes that you can hardly even remember
# i am smarter now so I'm going to redo this day

import sys
from util import *
inp = sys.stdin.read()
lines = inp.splitlines()

def parse_input(line):
    words = line.split()
    if len(line) == 0: return
    v=line.split('valves ')
    if len(v) == 1:
        v=line.split('valve ')
    return [words[1], int(words[4][:-1].split('=')[1]), v[1].split(', ')]

parse_valves = lambda s: s.split(', ')
flow_rate = lambda t: -t[1]
tns = lm(parse_input, lines)
tns.sort(key=flow_rate)
gtn = lambda t: t[0]
gt = lambda tn: lm(gtn, tns).index(tn)

gtr = lambda t: t[1]
gtbr = lambda tn: lm(gtr, tns).index(tn)

gtps = lambda t:t[2]


print(lm(flow_rate,tns))

ct = 'AA'
_ct = set(lm(gtn,tns))
ot = set()
print(_ct)

print(gt('BB'))
print(lm(lambda t:t[0],tns))
print(tns)

def pf(tna,tnd):
    # tunnel name at, tunnel name destination
    ct=tna
    i=gt(ct)
    lsfy=lambda a: lm(lambda d:[d],a)
    paths=[[ct]]
    while True:
        nps=[]
        for _ in range(len(paths)):
            ps=gtps(tns[lm(gtn, tns).index(paths[_][-1])])
            #print(paths[_][-1],ps)
            for p in ps:
                np = paths[_] + [p]
                if p == tnd:
                    return np
                nps.append(np)
        paths=nps


print(pf('AA','EE'))

prs = 0

sgn = lambda n: 1 if n > 0 else (-1 if n < 0 else 0)

for minute in range(30):
    for t in ot:
        _=gt(t)
        prs += gtr(tns[_])
    print(f'== Minute {minute+1} ==')
    i=gt(ct)
    t_flow=lm(lambda t: (tns[gt(t)][1], t), _ct)
    print(lm(lambda v:v[1],t_flow))
    d=lambda s:len(pf(ct,s[1]))
    gr=lambda s:tns[gt(s[1])][1]
    t_flow.sort(key=gr,reverse=1)
    print('before', t_flow)
    flowfind=lambda n: t_flow[lm(lambda v:v[1]==n,t_flow).index(1)]
    sr=lambda s,m: gr(s)*(m-minute-d(s))
    best=lambda s: max([[sr(s,m)-sr(flowfind(s[1]),m-(d(s)-d(flowfind(s[1]))))]+[d(s),gr(s),s,m] for m in range(30)])
    neg=lambda n:-best(n)[0]
    print(flowfind('II'))
    ntf=t_flow.copy()
    ntf.sort(key=neg)
    t_flow=ntf
    print(t_flow)
    print(lm(best,t_flow))
    print(t_flow[0][1])
    nt=t_flow[0][1]
    if ct in _ct and ct == nt:
        ot.add(ct)
        _ct.remove(ct)
        print(f"You open valve {ct}.")
        print(ot)
    else:
        # find new tunnel
        ct=pf(ct,nt)[1]
        print(f"You move to valve {ct}.")

print(ot,prs)
