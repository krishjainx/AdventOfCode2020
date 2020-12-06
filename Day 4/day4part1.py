input = open('Day 4/input.txt', "r").read()
input = input.split("\n\n")

validCounter = 0

for i in input:

    splitBySpaces = i.split()

    detailsNeeded = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]

    arrayOfTheItems = []

    for j in splitBySpaces:
        arrayOfTheItems.append(j.split(':')[0])

        doesHaveAllDetails = all(item in arrayOfTheItems for item in
                                 detailsNeeded)

    if doesHaveAllDetails:
        validCounter = validCounter + 1

print("These are the number of valid ones: " + str(validCounter))
