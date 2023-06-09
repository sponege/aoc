#!/bin/python3

import sys
inp = sys.stdin.read()
lines = inp.split('\n\n')
packetpairs = [[eval(p) for p in line.splitlines()] for line in lines]

debug = 0

if not debug:
    real_print = print
    print = lambda *args, **kwargs: 0

p1 = 0

#countDiff = lambda a, b: sum(1 for i in range(len(a)) if a[i] != b[i])

#def convertIntsInListToLists(l):
#    ## must go through every level of lists
#    ## and convert ints to lists
#    ## can be lists inside of lists inside of lists
#    ## so we need to go through every level of lists
#    ## and convert ints to lists
#
#    ## ex: [1, 2, 3, [4, 5, 6], 7, 8, 9]
#    ## ex: [1, [2, 3, [4, 5, [6], 7], 8], 9]
#
#    newList = []
#    for i in l:
#        if type(i) is int:
#            newList.append([i])
#        else:
#            newList.append(convertIntsInListToLists(i))
#    return newList
#
def packet_sorter(packetpair,level=0):
    ## pprint takes multiple arguments
    def pprint(*args):
        print('\t'*level + '- ', end='')
        print(*args)
    pp = packetpair
    packet1, packet2 = pp
    pprint('Compare', packet1, 'vs', packet2)
    for i in range(max(len(packet1), len(packet2))):
        if i >= len(packet1): ## left side runs out of items
            pprint("Left side ran out of items, so inputs are in the right order")
            return True
        if i >= len(packet2): ## right side runs out of items
            pprint("Right side ran out of items, so inputs are not in the right order")
            return False
        a=packet1[i]
        b=packet2[i]
        pprint('Compare',a,'vs',b)
        numInts = int(type(a) is int) + int(type(b) is int)
        #pprint(a,b,numInts)
        if numInts == 2:
            if 0:#level == 1:
                pprint(a, b)
            if a > b:
                pprint("Right side is smaller, so inputs are not in the right order")
                return False
            elif a < b:
                pprint("Left side is smaller, so inputs are in the right order")
                return True
        else:
            if numInts == 1:
                if type(a) is int:
                    a = [a]
                if type(b) is int:
                    b = [b]
            if 0:#level == 1:
                pprint(a, b)
            response = packet_sorter([a, b],level=level+1)
            if response == 'idk keep going':
                continue
            return response
    #pprint()
    #pprint(packet1)
    #pprint(packet2)
    return 'idk keep going'


#packetpairs.sort(key=packet_sorter)
for _ in range(len(packetpairs)):
    print()
    print(f"== Pair {_+1} ==")
    correct_order = packet_sorter(packetpairs[_])
    print("Correct" if correct_order else "Wrong", "Order")
    p1 += _+1 if correct_order else 0

packets=[]
for packetpair in packetpairs:
    packet1, packet2 = packetpair
    packets.append(packet1)
    packets.append(packet2)

## distress signal
packets.append([[2]])
packets.append([[6]])

def mergesort(arr_to_sort):
    """Recursively splits and merges an unsorted list to a sorted list."""

    if len(arr_to_sort) == 1:
        return arr_to_sort

    left = mergesort(arr_to_sort[len(arr_to_sort)//2:])
    right = mergesort(arr_to_sort[:len(arr_to_sort)//2])

    merged_list = []

    while len(left) > 0 and len(right) > 0:
        if packet_sorter([left[0], right[0]]):
            merged_list.append(left[0])
            left = left[1:]
        else:
            merged_list.append(right[0])
            right = right[1:]

    left += right
    merged_list += left

    return merged_list



if 0:
    for packets in packetpairs:
        for packet in packets:
            print(packet)
        print()

print()

packets = mergesort(packets)
for packet in packets:
    print(packet)

p2 = (packets.index([[2]])+1) * (packets.index([[6]])+1)

if not debug:
    print = real_print

print("Part 1:", p1)
print("Part 2:", p2)
