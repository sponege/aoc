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

def beaconless(y):
    ranges = [(r,_y) for r,_y in ranges_of_beaconless if y == _y]

    #values = [board[coord] for coord in row]
    print(ranges)
    count = 0#values.count('#')
    for x in range(minx,maxx+1):
        ## check if x is in range in a fast way
        for r in ranges:
            if x in range(r[0][0],r[0][1]):
                count += 1
                break

    return count

#for y in range(15):
#    print(beaconless(y))
    #print(f"funny {y} thing", beaconless(y))

print("Part 1 for test:", beaconless(10))
print("Part 1 for input:", beaconless(2000000))
