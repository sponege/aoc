#!/bin/python3

import sys, re
from util import *
from z3 import *

p, d, t, year, day, inp, lines, expected_ans = getArgs()

## you don't want to print a lot of debug info if you aren't in debug mode!
if not d:
    real_print = print
    print = lambda *args, **kwargs: None

# some helpful information:
# the variable p stores what part you are currently on, it's either 1 or 2
# make your script work with both parts by using if p == 1: ... else: ...
# the variable d is a boolean; it returns if you are in debug mode or not
# the submit function works 
# the variable t is a boolean; it returns if you are in test mode or not
ans = 'No answer calculated yet'

def parseEq(line):
    try:
        name, num = re.findall(r'([a-z]*): (\d*)', line)[0]
        return {'type': 'num', 'name': name, 'num': int(num)}
    except:
        name, op1, symbol, op2 = re.findall(r'([a-z]*): ([a-z]*) ([\+\*\-\/]) ([a-z]*)', line)[0]
        return {'type': 'op', 'name': name, 'op1': op1, 'op2': op2, 'symbol': symbol}

eqs = lm(parseEq, lines)
nums = filter(lambda x: x['type'] == 'num', eqs)
nums = lm(lambda num: {num['name']: num['num']}, nums)
# convert to dict
nums = {k: v for d in nums for k, v in d.items()}
eqs = list(filter(lambda x: x['type'] == 'op', eqs))

## your code goes here
if p == 1:
    print(nums)
    print(eqs)
    # ans = 1337
    while 'root' not in nums:
        for eq in eqs:
            if eq['op1'] in nums and eq['op2'] in nums:
                op1= nums[eq['op1']]
                op2 = nums[eq['op2']]
                if eq['symbol'] == '+':
                    nums[eq['name']] = op1 + op2
                elif eq['symbol'] == '*':
                    nums[eq['name']] = op1 * op2
                elif eq['symbol'] == '-':
                    nums[eq['name']] = op1 - op2
                elif eq['symbol'] == '/':
                    nums[eq['name']] = op1 / op2
                eqs.remove(eq)
                print(nums)
            else:
                pass
                #print('not ready', eq)
                #print("Missing one of", eq['op1'], eq['op2'])
    ans = int(nums['root'])
    
    pass
else: ## part 2
    # ans = 13371337
    # delete humn from nums
    del nums['humn']
    # change equation for root to sign =
    for eq in eqs:
        if eq['name'] == 'root':
            eq['symbol'] = '='
    print(nums)
    print(eqs)
    
    vars = {}
    # create variables
    for eq in eqs:
        for var in [eq['op1'], eq['op2']]:
            if var not in vars:
                vars[var] = Int(var)
    print(vars)


    s = Solver()
    for d in nums:
        name, num = d, nums[d]
        num = int(num)
        s.add(vars[name] == num)
    for eq in eqs:
        op1 = vars[eq['op1']]
        op2 = vars[eq['op2']]
        if eq['symbol'] == '+':
            s.add(op1 + op2 == vars[eq['name']])
        elif eq['symbol'] == '*':
            s.add(op1 * op2 == vars[eq['name']])
        elif eq['symbol'] == '-':
            s.add(op1 - op2 == vars[eq['name']])
        elif eq['symbol'] == '/':
            s.add(op1 / op2 == vars[eq['name']])
        elif eq['symbol'] == '=':
            s.add(op1 == op2)
    s.check()
    ans = s.model()[vars['humn']]



    
    """
    nums = oldnums
    for eq in eqs:
        if eq['name'] == 'root':
            eq['symbol'] = '='
    print(nums)
    print(eqs)
    for a in range(1,99999999):
        del nums
        nums = oldnums.copy()
        eqs = oldeqs.copy()
        nums['humn'] = a
        print(a)
        try:
            while 'root' not in nums:
                for eq in eqs:
                    if eq['op1'] in nums and eq['op2'] in nums:
                        op1= nums[eq['op1']]
                        op2 = nums[eq['op2']]
                        if eq['symbol'] == '+':
                            nums[eq['name']] = op1 + op2
                        elif eq['symbol'] == '*':
                            nums[eq['name']] = op1 * op2
                        elif eq['symbol'] == '-':
                            nums[eq['name']] = op1 - op2
                        elif eq['symbol'] == '/':
                            nums[eq['name']] = op1 // op2
                        elif eq['symbol'] == '=':
                            print(nums)
                            print(op1, '==', op2, '?')
                            assert op1 == op2
                            ans = a
                            final(t, p, ans, expected_ans)
                            exit(0)
                            
                        eqs.remove(eq)
                        print(nums)
                    else:
                        pass
                        #print('not ready', eq)
                        #print("Missing one of", eq['op1'], eq['op2'])
            print("WHAT THE FUCK")
        except Exception as e:
            pass
    """

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
