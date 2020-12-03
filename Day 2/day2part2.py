import re

input = open("Day 2/input.txt").read().splitlines()

position1 = 0
position2 = 0
correctCounter = 0

for i in input:
    splitLine = re.split(' |: ', i)
    # print(splitLine)

    for j in splitLine:
        if splitLine.index(j) == 0:
            position1 = int(j.split("-")[0])
            position2 = int(j.split("-")[1])
        if splitLine.index(j) == 2 and (position1 <= len(j)) and (position2 <= len(j)):
            word_broken = list(splitLine[2])
            if (word_broken[position1 - 1] == splitLine[1]) ^ (word_broken[position2 - 1] == splitLine[1]):
                correctCounter += 1

print(correctCounter)