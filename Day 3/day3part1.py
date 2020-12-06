input = open("Day 3/input.txt").read().splitlines()

xPosition = 0
encounteredTrees = 0

for i in input:
    if xPosition >= len(i):
        xPosition = xPosition - len(i)

    if i[xPosition] == "#":
        encounteredTrees += 1

    xPosition += 3


print(encounteredTrees)
