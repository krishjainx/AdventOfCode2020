input = open("/Users/krishjain/Desktop/AdventOfCode/Day 3/input.txt").read().splitlines()

def day3part2(theInput):
    def path(xMovement, yMovement):    
        x = 0
        total = 0
        for i in range(len(theInput)):
            if i % yMovement != 0:         
                continue
            if theInput[i][x] == '#':
                total += 1
            x = (x + xMovement) % len(theInput[i]) #OR 
            # x += xMovement
            # if x >= len(theInput[i]):
            #     x = x - len(theInput[i])
                
        return total     
    return path(1,1) * path(3,1) * path(5,1) * path(7,1) * path(1,2)

print(day3part2(input))


 
        