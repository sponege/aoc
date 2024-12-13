#!pypy3

##             ##
#  OUT OF DATE  #
#  Please use   #
#    aoc.js!    #
##             ##

import json, datetime, os

print('Out of date, please use aoc.js instead')
exit()

## read session data
session = open('state/session').readline().strip()

today = datetime.date.today()
state = json.loads(open('state/state.json').read())

if (today.month == 11 and today.day == 30) or (today.month == 12 and today.day < 25):# and state.get('day') != today.day:
    upcoming = input("Are you playing the upcoming challenge? (anykey/n) ") != 'n'
else:
    upcoming = False

def getNum(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except:
            print("Please enter a number")
    return num


if upcoming:
    state = {
        'year': today.year,
        'day': (today.day + 1) % 30,
        'part': 1,
    }
else:
    newday = input("Are you starting a new day? (y/anykey) ") == 'y'
    if newday:
        year = getNum("What year? ")
        day = getNum("What day? ")
        part = 1
        state = {
            'year': year,
            'day': day,
            'part': part,
        }

# the day needs to be length 2! (e.g. 01, 02, 03, etc)
state['day'] = str(state['day']).zfill(2)

open('state/state.json', 'w').write(json.dumps(state))

## make a new year directory if needed
if not os.path.exists(str(state['year'])):
    os.mkdir(str(state['year']))

## update utils
open(f'{state["year"]}/util.py', 'w').write(open('util.py').read())

## make a new day.test and day.py for the day
if not os.path.isfile(f'{state["year"]}/{state["day"]}.t'):
    open(f'{state["year"]}/{state["day"]}.t', 'w').write('')
if not os.path.isfile(f'{state["year"]}/{state["day"]}.py'):
    open(f'{state["year"]}/{state["day"]}.py', 'w').write(open('template.py').read())

    ## make script executable
    os.system(f'chmod +x {state["year"]}/{state["day"]}.py')

if upcoming:
    ## do a fancy countdown to 12 am EST
    import time
    import datetime
    import pytz
    import sys

    tz = pytz.timezone('US/Eastern')
    now = datetime.datetime.now(tz)
    midnight = tz.localize(datetime.datetime(now.year, now.month, now.day, 0, 0, 0))
    midnight += datetime.timedelta(days=1)
    midnight += datetime.timedelta(seconds=1) ## server time is one second behind
    print("Countdown to midnight EST")
    while now < midnight:
        ## Format: hh:mm:ss
        t = str(midnight - now).split('.')[0].split(':')
        for i in range(len(t)):
            part = t[i]
            if len(part) == 1:
                t[i] = '0' + part
        t = ':'.join(t)
        sys.stdout.write("\r" + t)
        sys.stdout.flush()
        time.sleep(1)
        now = datetime.datetime.now(tz)
    print() ## newline

## download input if we dont have one yet
if not os.path.isfile(f'{state["year"]}/{state["day"]}.i'):
    ## download input
    import requests
    url = f'https://adventofcode.com/{state["year"]}/day/{int(state["day"])}/input'
    cookies = {'session': session}
    headers = {'User-Agent': 'github.com/sponege/aoc by apples@jappl.es'}
    r = requests.get(url, cookies=cookies, headers=headers)
    open(f'{state["year"]}/{state["day"]}.i', 'w').write(r.text)
    print(r.text) ## print input



## run the code
#import subprocess
#subprocess.run(['python3', f'{state["year"]}/{state["day"]}.py'])
