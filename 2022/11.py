#!/bin/python3

import sys
inp = sys.stdin.read()
lines = inp.splitlines()

def prod(list):
    p = 1
    for i in list:
        p *= i
    return p
def sumwfunc(list, func):
    val = 0
    for i in list:
        val += func(i)
    return val


# part 1
template = {}
monkeys = []
state = {
    'monkey': 0,
}

for line in lines:
    line = line.strip()
    if line.endswith(':'):
        monkey = line[:-1]
        state['monkey'] = int(monkey.split(' ')[1])
        monkeys.append({
            'items_inspected': 0,
        })
    words = line.split(' ')
    #print(words)
    if words[0] == 'Starting':
        items = [int(_) for _ in line.split(':')[1].strip().split(', ')]
        monkeys[-1]['worry_levels'] = items
    elif words[0] == 'Operation:':
        op = words[-2]
        num = int(words[-1]) if words[-1] != 'old' else 'old'
        monkeys[-1]['operation'] = {'op': op, 'num': num}
    elif words[0] == 'Test:':
        monkeys[-1]['test'] = int(words[-1])
    elif len(words) == 1:
        continue
    elif words[1] == 'true:':
        monkeys[-1]['case_true'] = int(words[-1])
    elif words[1] == 'false:':
        monkeys[-1]['case_false'] = int(words[-1])

safe_modulo = prod([m['test'] for m in monkeys])

print([m['worry_levels'] for m in monkeys])
def round():
    global monkeys
    for _ in range(len(monkeys)):
        _m = monkeys[_]
        for worry_level in monkeys[_]['worry_levels']:
            _wls = _m['worry_levels']
            monkeys[_]['items_inspected'] += len(_wls)
            while len(monkeys[_]['worry_levels']) != 0:
                _wl = monkeys[_]['worry_levels'].pop(0)
                _op = _m["operation"]["op"]
                _two = _m["operation"]["num"] if _m["operation"]["num"] != "old" else _wl
                #_wl %= _m['test']
                #_two %= _m['test']
                if _op == '+':
                    _wl += _two
                else:
                    _wl *= _two
                    pass
                #_wl //= 3
                _wl %= safe_modulo
                test = _wl % _m['test'] == 0
                if test:
                    _tm = _m['case_true']
                else:
                    _tm = _m['case_false']
                monkeys[_tm]['worry_levels'].append(_wl)




    return [m['items_inspected'] for m in monkeys]

for _ in range(10000):
    #print(_, round())
    round()

mb = [m['items_inspected'] for m in monkeys]
mb.sort()
print(mb[-1]*mb[-2])
#worry_levels = [len(monkey['inspections'])*20 for monkey in monkeys]
#print(worry_levels)
