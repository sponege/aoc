#!/bin/python3

import sys, re
from util import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
real_print = print
real_pb = print_board
if not d:
    print = lambda *args, **kwargs: None
    print_board = lambda *args, **kwargs: None

# some helpful information:
# the variable p stores what part you are currently on, it's either 1 or 2
# make your script work with both parts by using if p == 1: ... else: ...
# the variable d is a boolean; it returns if you are in debug mode or not
# the submit function works 
# the variable t is a boolean; it returns if you are in test mode or not
ans = 'No answer calculated yet'

re_mapper = lambda line: re.findall('Valve ([A-Z]+) has flow rate=([\d]+); tunnel[s]* lead[s]* to valve[s]* (([A-Z]+[, ]*)*)', line)

def mapper(line):
    m = re_mapper(line)[0]
    return {'tunnel': m[0], 'flow': int(m[1]), 'leads': m[2].split(', ')}

valvesTemplate = lm(mapper, lines)

# turn list into key-value dict
valves = {}
for v in valvesTemplate:
    valves[v['tunnel']] = v

valvesTemplate = valves
print(valvesTemplate)

paths = [
    {
        'state': valvesTemplate,
        'openedSet': set(),
        'path': ['AA'],
        'pressureReleased': 0,
        'valveTarget': None,
    }
]



## your code goes here
if p == 1:
    minutes = 30
    # ans = 1337
    pass
else: ## part 2
    minutes = 26
    # ans = 13371337
    pass

def pathfind(curValve, newValve):
    ## find next valve to go to to get to the new valve as fast as possible
    ## return the next valve to get there
    paths = [[curValve]]
    #print(f'finding path from {curValve} to {newValve}')
    while True:
        newPaths = []
        for path in paths:
            for valve in valves[path[-1]]['leads']:
                if valve == newValve:
                    path = path + [valve]
                    #print('path', path)
                    return path[1]
                if valve not in path:
                    newPaths.append(path + [valve])
        paths = newPaths

for minute in range(minutes): 
    ## traverse every single possible path
    ## use sets to make this faster
    print(f"Minute {minute+1}")
    print(f"Number of paths: {len(paths)}")
    print('----------------')
    if 0:
        for path in paths:
            print('Destination:', path['valveTarget'])
            print("Opened:", path['openedSet'])
            print("Path:", path['path'])
            print("Pressure released:", path['pressureReleased'])
            print('----------------')
    print()
    newPaths = []
    for path in paths.copy():
        np = path.copy()
        np['path'] = np['path'].copy()
        np['openedSet'] = np['openedSet'].copy()
        np['state'] = np['state'].copy()
        curValve = path['path'][-1]
        ## if all valves are open
        if len(path['openedSet']) == len([valve for valve in valves if valvesTemplate[valve]['flow']]):
            continue
        ## if we are at the target valve
        if path['valveTarget'] == curValve or path['valveTarget'] == None:
            openedValve = False
            if path['valveTarget'] == curValve: ## if we are at our destination
                ## open valve
                np['openedSet'].add(curValve)
                np['valveTarget'] = None
                np['pressureReleased'] += valves[curValve]['flow'] * (minutes - (minute+1))
                allPressureReleased = [path['pressureReleased'] for path in paths]
                maxPressureReleased = max(allPressureReleased)
                if maxPressureReleased <= np['pressureReleased']: np['path'].append(curValve)
                else: continue
                openedValve = True
            unopenedValves = set(valves.keys()) - path['openedSet'] - set(path['path'])
            newPaths.append(np)
            for newValve in unopenedValves: ## find a new valve to open and walk toward it
                if valvesTemplate[newValve]['flow'] == 0: continue
                np = path.copy()
                np['path'] = np['path'].copy()
                np['openedSet'] = np['openedSet'].copy()
                np['state'] = np['state'].copy()
                # print(np['openedSet'], "Going to open", newValve)
                np['valveTarget'] = newValve
                if not openedValve: ## if we haven't opened a valve we have some time to walk
                    np['path'].append(pathfind(curValve, newValve))
                newPaths.append(np)
        else: ## if we are not at the target valve
            ## walk toward target valve
            np['path'].append(pathfind(curValve, path['valveTarget']))
            newPaths.append(np)

    paths = newPaths

print(valvesTemplate)
allPressureReleased = [path['pressureReleased'] for path in paths]
print("Pressures released:", allPressureReleased)
ans = max(allPressureReleased)
winningPath = paths[allPressureReleased.index(ans)]
print('winning path', winningPath['path'])
if p == 2:
    print("Part 2")
    paths = [
        {
            'state': valvesTemplate,
            'openedSet': winningPath['openedSet'],
            'path': ['AA'],
            'pressureReleased': 0,
            'valveTarget': None,
        }
    ]
    for minute in range(minutes): 
        ## traverse every single possible path
        ## use sets to make this faster
        print(f"Minute {minute+1}")
        print(f"Number of paths: {len(paths)}")
        print('----------------')
        if 0:
            for path in paths:
                print('Destination:', path['valveTarget'])
                print("Opened:", path['openedSet'])
                print("Path:", path['path'])
                print("Pressure released:", path['pressureReleased'])
                print('----------------')
        print()
        newPaths = []
        for path in paths.copy():
            np = path.copy()
            np['path'] = np['path'].copy()
            np['openedSet'] = np['openedSet'].copy()
            np['state'] = np['state'].copy()
            curValve = path['path'][-1]
            ## if all valves are open
            if len(path['openedSet']) == len([valve for valve in valves if valvesTemplate[valve]['flow']]):
                continue
            ## if we are at the target valve
            if path['valveTarget'] == curValve or path['valveTarget'] == None:
                openedValve = False
                if path['valveTarget'] == curValve: ## if we are at our destination
                    ## open valve
                    np['openedSet'].add(curValve)
                    np['valveTarget'] = None
                    np['pressureReleased'] += valves[curValve]['flow'] * (minutes - (minute+1))
                    allPressureReleased = [path['pressureReleased'] for path in paths]
                    maxPressureReleased = max(allPressureReleased)
                    if maxPressureReleased <= np['pressureReleased']: np['path'].append(curValve)
                    else: continue
                    openedValve = True
                unopenedValves = set(valves.keys()) - path['openedSet'] - set(path['path'])
                newPaths.append(np)
                for newValve in unopenedValves: ## find a new valve to open and walk toward it
                    if valvesTemplate[newValve]['flow'] == 0: continue
                    np = path.copy()
                    np['path'] = np['path'].copy()
                    np['openedSet'] = np['openedSet'].copy()
                    np['state'] = np['state'].copy()
                    # print(np['openedSet'], "Going to open", newValve)
                    np['valveTarget'] = newValve
                    if not openedValve: ## if we haven't opened a valve we have some time to walk
                        np['path'].append(pathfind(curValve, newValve))
                    newPaths.append(np)
            else: ## if we are not at the target valve
                ## walk toward target valve
                np['path'].append(pathfind(curValve, path['valveTarget']))
                newPaths.append(np)

        paths = newPaths
    ans = ans + max(allPressureReleased)


## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)
## submit answer you got to the utils function
final(t, p, ans, expected_ans)
