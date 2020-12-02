import re

input = open("/Users/krishjain/Downloads/AdventOfCode/Day 2/input.txt").read().splitlines()
lower_bound = 0
higher_bound = 0
counter2 = 0


for i in input:
	splitLine = re.split(' |: ', i)
	
	for j in splitLine:
		if splitLine.index(j) == 0:
			lower_bound = int(j.split("-")[0])
			higher_bound = int(j.split("-")[1])
		if splitLine.index(j) == 2:
			numberoftimes = splitLine[2].count(splitLine[1])
			if (numberoftimes <= higher_bound) and (numberoftimes >= lower_bound):
				counter2 += 1

print(counter2)
	
