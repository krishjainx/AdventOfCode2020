input = open("Day 5/input.txt").read().splitlines()
# Part 1

arrayOfSeatID = []
last_amount_moved = 128

for boardingPass in input:
    rowPosition = boardingPass[0:7]
    columnPosition = boardingPass[-3:]
    row = 0
    last_amount_moved = 128
    for character in rowPosition:
        if character == "B":
            row += (last_amount_moved/2)
        last_amount_moved = last_amount_moved/2

    column = 0
    last_amount_moved_column = 8
    
    for character in columnPosition:
        if character == "R":
            column += (last_amount_moved_column/2)
        last_amount_moved_column = last_amount_moved_column/2

    arrayOfSeatID.append(int(column+row*8))

solution = max(arrayOfSeatID)
print(solution)

# Part 2 variable to pass to part2 file

allValues = list(range(min(arrayOfSeatID), max(arrayOfSeatID)))
