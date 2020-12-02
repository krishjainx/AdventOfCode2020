input = open("/Users/krishjain/Downloads/AdventOfCode/input.txt").read().splitlines()
list2 = []

for i in range(len(input)):
    t = int(input[i])
    list2.append(t)

for i in list2:
    for j in list2:
       if j == 2020 - i:
           a = j
           b = 2020 - j 
           print(a*b)
           
    i = i + 1

