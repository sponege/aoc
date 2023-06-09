#!/bin/python3

import sys
from util import *
inp = sys.stdin.read()
coords = [l[10:].split(': closest beacon is at ') for l in inp.splitlines()]
coords = [[tuple([int(xy[2:]) for xy in point.split(', ')]) for point in coord] for coord in coords]
sensors = [coord[0] for coord in coords]
beacons = [coord[1] for coord in coords]

board = {}
for sensor, beacon in zip(sensors, beacons):
    board[sensor] = 'S'
    board[beacon] = 'B'

manhattan = lambda a, b: abs(a[0]-b[0])+abs(a[1]-b[1])

ranges_of_beaconless = []
_=0
for sensor in sensors:
    print('done', _)
    _+=1
    closestBeaconToSensor = min(beacons, key=lambda beacon: manhattan(sensor, beacon))
    distanceToClosestBeacon = manhattan(sensor, closestBeaconToSensor)

    for dy in range(-distanceToClosestBeacon, distanceToClosestBeacon+1):
        x=sensor[0]
        ranges_of_beaconless.append(([x-distanceToClosestBeacon+abs(dy),x+distanceToClosestBeacon-abs(dy)], sensor[1]+dy))
        #for dx in range(-distanceToClosestBeacon+abs(dy), distanceToClosestBeacon+1-abs(dy)):
        #    x=sensor[0]+dx
        #    y=sensor[1]+dy
        #    coord = (x,y)
        #    if not coord in board:
        #        board[coord] = '#'

# smallest x in range
minx = min([range[0] for range,_ in ranges_of_beaconless])
print('min x', minx)
maxx = max([range[1] for range,_ in ranges_of_beaconless])
print('max x', maxx)

y=miny = min([y for _,y in ranges_of_beaconless])
maxy = max([y for _,y in ranges_of_beaconless])
print('min y', miny)
print('max y', maxy)
print('num ranges', len(ranges_of_beaconless))
#while 1:

def addpos(list):
    nl = []
    _=0
    for i in list:
        nl.append([i[0],i[1],_])
        _+=1
    return nl

getranges = lambda y: [r for r,_y in ranges_of_beaconless if y == _y]

for y in range(miny, maxy+1):
    ranges = getranges(y)
    ranges = addpos(ranges)

    print("{}% done".format((y-miny)/(maxy-miny)*100))

    #values = [board[coord] for coord in row]
    #if y == 11: 
    #    print('omgomgomg', y,ranges)
    count = 0#values.count('#')
    if len(ranges) < 2:
        continue
    for _s, sx, y1 in ranges:
        for bx, _b, y2 in ranges:
            #print('sx', sx, 'bx', bx, 'y1', y1, 'y2', y2)
            if y1 != y2 and sx == bx - 2:
                #print('possible', (sx + 1, y), [_s, sx], [bx, _b])
                #print(ranges)
                x = sx + 1
                fr = 1
                #mx = min([x for x,_,_ in ranges])
                #Mx = max([x for x,_,_ in ranges])
                #print('min max of ranges', [mx, Mx])
                fail = 0
                for r in ranges:
                    if x in range(r[0], r[1]) or (x,y) in board:
                        fail = 1
                        continue
                if fail:
                    continue
                for _y in [y-1, y+1]:
                    curfail = 1
                    rr = getranges(_y)
                    #print(f'testing {_y} with x = {x} with ranges {rr}')
                    for r in rr:
                        #print(r)
                        if x in range(r[0], r[1]):
                            #print("NOT FAIL")
                            curfail = 0
                            break
                    if curfail:
                        fail = 1
                        break
                if fail:
                    #print('fail')
                    continue
                print('found', (x,y))
                print('part 2', x*4000000+y)
                exit()
    y+=1


#for y in range(15):
#    print(beaconless(y))
    #print(f"funny {y} thing", beaconless(y))

