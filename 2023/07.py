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

ans = 0

def compare_hands(a,b):
    for i in range(2):
        amount_a = a[0][i]
        amount_b = b[0][i]
        if amount_a < amount_b: return 1
        if amount_a > amount_b: return 0
    for i in range(5):
        value_a = a[1][i]
        value_b = b[1][i]
        if value_a < value_b: return 1
        if value_a > value_b: return 0

def mergesort(arr_to_sort):
    """Recursively splits and merges an unsorted list to a sorted list."""

    if len(arr_to_sort) == 1:
        return arr_to_sort

    left = mergesort(arr_to_sort[len(arr_to_sort)//2:])
    right = mergesort(arr_to_sort[:len(arr_to_sort)//2])

    merged_list = []

    while len(left) > 0 and len(right) > 0:
        if compare_hands(left,right):
            merged_list.append(left[0])
            left = left[1:]
        else:
            merged_list.append(right[0])
            right = right[1:]

    left += right
    merged_list += left

    return merged_list
def parseHand(hand):
    hand, bid = hand
    new_hand = [0]
    for card in set(hand):
        if p == 2 and card == 'J': continue
        new_hand.append(hand.count(card))
    new_hand.sort(reverse=True)
    print(hand, bid)
    new_hand[0] += (hand.count("J") if p == 2 else 0)
    return (new_hand[:2], [("AKQJT98765432" if p == 1 else "AKQT98765432J")[::-1].index(card) for card in hand], int(bid))

hands = [parseHand(l.split(' ')) for l in lines]
hands = mergesort(hands)
print(hands)

for i, hand in enumerate(hands):
    ans += (i+1)*hand[2]

## restore print
if not d:
    print = real_print

## place log info down here that you want shown even when running on the real large input
# print_board(board)

## submit answer you got to the utils function
final(t, p, ans, expected_ans)
