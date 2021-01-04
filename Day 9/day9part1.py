from itertools import combinations
import math
import random

with open('Day 9/input.txt', 'r') as fd:
    numbers = [int(line.rstrip()) for line in fd]

HowManyNumbersToIgnore = 25        # HowManyNumbersToIgnore

def check_number(pos):
    global numbers
    startpos = pos - HowManyNumbersToIgnore
    combs = [lst for lst in combinations(numbers[startpos:pos], 2)]     
    sums = [sum(i) for i in combs]
    if numbers[pos] in sums:
        check_number(pos + 1)
    else:
        print("Part 1: " + str(numbers[pos]) + " is the first number not equal to a sum")
    return [numbers[pos], pos]


FirstInvalidLst = check_number(HowManyNumbersToIgnore)