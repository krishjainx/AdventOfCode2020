input = open("/Day 1/input.txt").read().splitlines()
list2 = []

for i in range(len(input)):
    t = int(input[i])
    list2.append(t)

for i in list2:
    for j in list2:
    #    if j == 2020 - i:
    #        a = j
    #        b = 2020 - j 
    #        print(a*b)
        for k in list2:
            if i + j + k == 2020:
                    # print(i)
                    # print(j)
                    # print(k)
                    print(i*j*k)
           
i = i + 1

