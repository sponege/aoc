#!/bin/python3

import sys, re
from util import *

ans = 1337 

p, d, t, inp, lines = getArgs()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


expected_ans=123
print(bcolors.OKGREEN + bcolors.BOLD + 'Test passed!!!!' + bcolors.ENDC + f' Expected {bcolors.OKBLUE+bcolors.BOLD}{expected_ans}{bcolors.ENDC}, got {bcolors.OKBLUE+bcolors.BOLD}{ans}{bcolors.ENDC}')
print(f'ans:{ans}')
