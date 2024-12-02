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
getranges = lambda y: [r for r,_y in ranges_of_beaconless if y == _y]
__=0
for sensor in sensors:
    closestBeaconToSensor = min(beacons, key=lambda beacon: manhattan(sensor, beacon))
    distanceToClosestBeacon = manhattan(sensor, closestBeaconToSensor)

    print(f"Sensor: {sensor}\nClosest beacon: {closestBeaconToSensor}\nDistance to closest beacon: {distanceToClosestBeacon}")

    nomore = 4000000
    y=sensor[1]
    my=max(-distanceToClosestBeacon,-nomore)
    My=min(distanceToClosestBeacon+1,nomore)
    dist=abs(my)+abs(My)-1

    print(f"Expected amount of ranges to add: {dist}")

    for dy in range(my,My):
        percentage=(dy-my)/(dist)*100
        #sys.stdout.write('\r' + "{}% done, length of ranges is {}".format(round(percentage,2),len(ranges_of_beaconless)))
        #sys.stdout.flush()
        x=sensor[0]
        sx=x-distanceToClosestBeacon+abs(dy)
        bx=x+distanceToClosestBeacon-abs(dy)
        y=sensor[1]
        y+=dy
        nr=[[sx,bx],y]
        if y < 0 or y > nomore or sx < 0 or bx > nomore:
            continue
        #print('nr',nr)
        #print('managable length?',len(ranges_of_beaconless))
        #print(ranges_of_beaconless)

        # contains
        c=lambda r: contains((r,nr[0]),oneway=1)
        # not contains
        nc=lambda r: not c(r)

        rs=getranges(y)

        overlappings = lm(c,rs)
        overlappings_count = sum(overlappings)
        #print(overlappings,overlappings_count)
        if overlappings_count: 
            rs.sort(key=nc)
            print(f"Replacing {overlappings_count} ranges")

        for r in rs[:overlappings_count]:
            #print('r',r)
            #print('testing',nr[0],r)
            #if contains((nr[0],r),oneway=True):
            #print(nr[0], 'contains', r)
            nr[0][0]=min(sx,r[0])
            nr[0][1]=max(bx,r[1])
            #_=0
            ranges_of_beaconless.pop(ranges_of_beaconless.index([r,y]))
            #while _ < len(ranges_of_beaconless):
            #    if ranges_of_beaconless[_]==[r,y]:
            #        #print('popping', ranges_of_beaconless[_], _)
            #        ranges_of_beaconless.pop(_)
            #        break
            #        _-=1
            #    _+=1
        #print('adding',nr)
        ranges_of_beaconless.append(nr)
        #for dx in range(-distanceToClosestBeacon+abs(dy), distanceToClosestBeacon+1-abs(dy)):
        #    x=sensor[0]+dx
        #    y=sensor[1]+dy
        #    coord = (x,y)
        #    if not coord in board:
        #        board[coord] = '#'
    print('\nCompleted', __+1, 'sensor' + ('s' if __>0 else ''))
    __+=1

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


for y in range(miny, maxy+1):
    ranges = getranges(y)
    ranges = addpos(ranges)

    percentage=(y-miny)/(maxy-miny)*100
    sys.stdout.write('\r' + "{}% done, length of ranges is {}".format(round(percentage,2),len(ranges_of_beaconless)))
    sys.stdout.flush()

    #values = [board[coord] for coord in row]
    #if y == 11: 
    #    print('omgomgomg', y,ranges)
    count = 0#values.count('#')
    if len(ranges) < 2:
        continue
    for _s, sx, y1 in ranges:
        for bx, _b, y2 in ranges[y1:]:
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
                print('\nfound', (x,y))
                print('part 2', x*4000000+y)
                exit()
    y+=1


#for y in range(15):
#    print(beaconless(y))
    #print(f"funny {y} thing", beaconless(y))

