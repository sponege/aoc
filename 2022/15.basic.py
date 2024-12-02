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

for sensor in sensors:
    closestBeaconToSensor = min(beacons, key=lambda beacon: manhattan(sensor, beacon))
    distanceToClosestBeacon = manhattan(sensor, closestBeaconToSensor)

    for dy in range(-distanceToClosestBeacon, distanceToClosestBeacon+1):
        ranges_of_beaconless.append(([-distanceToClosestBeacon+abs(dy),distanceToClosestBeacon+1-abs(dy)], sensor[1]+dy))
        #for dx in range(-distanceToClosestBeacon+abs(dy), distanceToClosestBeacon+1-abs(dy)):
        #    x=sensor[0]+dx
        #    y=sensor[1]+dy
        #    coord = (x,y)
        #    if not coord in board:
        #        board[coord] = '#'

maxx = max([max([x for x, y in coord]) for coord in coords])

def beaconless(y):
    ranges = [(r,_y) for r,_y in ranges_of_beaconless if y == _y]

    #values = [board[coord] for coord in row]
    print(ranges)
    count = 0#values.count('#')
    return count

print_board(board)
print("Part 1:", beaconless(2000000))
