#!/bin/python3

import sys
inp = sys.stdin.read()
lines = inp.split('\n\n')
packetpairs = [[eval(p) for p in line.splitlines()] for line in lines]

p1 = 0

countDiff = lambda a, b: sum(1 for i in range(len(a)) if a[i] != b[i])

def convertIntsInListToLists(l):
    ## must go through every level of lists
    ## and convert ints to lists
    ## can be lists inside of lists inside of lists
    ## so we need to go through every level of lists
    ## and convert ints to lists

    ## ex: [1, 2, 3, [4, 5, 6], 7, 8, 9]
    ## ex: [1, [2, 3, [4, 5, [6], 7], 8], 9]

    newList = []
    for i in l:
        if type(i) is int:
            newList.append([i])
        else:
            newList.append(convertIntsInListToLists(i))
    return newList

def convertIntsInListToLists(l):
    ## must go through every level of lists
    ## and convert ints to lists
    ## can be lists inside of lists inside of lists
    ## so we need to go through every level of lists
    ## and convert ints to lists
    ## cannot be recursive!

    ## ex: [1, 2, 3, [4, 5, 6], 7, 8, 9]
    ## ex: [1, [2, 3, [4, 5, [6], 7], 8], 9]

    newList = []
    for i in l:
        if type(i) is int:
            newList.append([i])
        else:
            newList.append(convertIntsInListToLists(i))
    return newList

def packet_sorter(packetpair):
    things = [(packetpair, [0])]
    newpacketpairposes = []
    while len(things) > 0:
        thing, location = things.pop()
        ptr = packetpair
        if type(thing) is int:
            ## edit packetpair at location
            ## ex: packetpair[loc[0]][loc[1]] = thing
            newpacketpairposes.append((thing, location + [i]))
        else:
            for i in range(len(thing)):
                things.append((thing[i], location + [i]))
    newpacketpairposes.sort(key=lambda x: x[1]) # sort by location length
    fpp=[] ## final packet pair
    npps=[] ## new packet pairs
    oldloc = []
    for thing, location in newpacketpairposes:
        l=location[:-1]
        append = len(oldloc) > 0 and countDiff(l, oldloc) > 1
        print(l, oldloc, thing, append)
        if append:
            #if location[:-1] != oldloc:
            fpp.append(npps)
            npps = []
        npps.append(thing)
        oldloc = location[:-1]
    fpp.append(npps)
    print('fpp', fpp)

    if 0:
        l=location[1:-1]
        npp.append(thing)
        #print(npp, l[-1], thing)
        print(l)
        if countDiff(l, oldloc) > 1:
            if l[0] != oldloc[0]:
                fpp.append(npp)
                npp = []
            else:
                npp = [npp]
        else:
            npp.append(thing)
        oldloc = l

    packet1, packet2 = fpp
    print()
    print(packet1)
    print(packet2)
    return packet1 < packet2


#packetpairs.sort(key=packet_sorter)
for _ in range(len(packetpairs)):
    p1 += 1 if packet_sorter(packetpairs[_]) else 0

for packets in packetpairs:
    for packet in packets:
        print(packet)
    print()

