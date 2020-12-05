input = open('Day 4/input.txt', "r").read()
input = input.split("\n\n")

validCounter = 0

insideCounter = 0

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

        
        
        jsecond = j.split(':')[1]
        jfirst = j.split(':')[0]
        if (jfirst == "byr") and (len(jsecond) == 4) and (int(jsecond) >= 1920) and (int(jsecond) <= 2002):
            insideCounter = insideCounter + 1
        
        if (jfirst == "iyr") and (len(jsecond) == 4) and (int(jsecond) <= 2020) and (int(jsecond) >= 2010):
            insideCounter = insideCounter + 1
        
        if (jfirst == "eyr") and (len(jsecond) == 4) and (int(jsecond) >= 2020) and (int(jsecond) <= 2030):
             insideCounter = insideCounter + 1

        hclAllowedCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        if (jfirst == "hcl") and (jsecond[0] == "#") and (len(jsecond) == 7) and (jsecond[1] in hclAllowedCharacters) and (jsecond[2] in hclAllowedCharacters) and (jsecond[3] in hclAllowedCharacters) and (jsecond[4] in hclAllowedCharacters) and (jsecond[4] in hclAllowedCharacters) and (jsecond[5] in hclAllowedCharacters) and (jsecond[6] in hclAllowedCharacters):
            insideCounter = insideCounter + 1

        ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
        if (jfirst == "ecl") and (any(item in jsecond for item in ecl)):
            insideCounter = insideCounter + 1
        

        if (jfirst == "pid") and (len(jsecond) == 9) and (jsecond.isnumeric()):
             insideCounter = insideCounter + 1

        heightUnit = [jsecond[-2:]]
        if (jfirst == "hgt") and (jsecond[-2:] == "cm") and (jsecond[:-2].isnumeric()) and (int(jsecond[:-2]) <= 193) and (int(jsecond[:-2]) >= 150):
             insideCounter = insideCounter + 1
        elif (jfirst == "hgt") and (jsecond[-2:] == "in") and (jsecond[:-2].isnumeric()) and (int(jsecond[:-2]) <= 76) and (int(jsecond[:-2]) >= 59):
          insideCounter = insideCounter + 1
        
        
        doesHaveAllDetails = all(item in arrayOfTheItems for item in detailsNeeded)

        print(insideCounter)
    
    if doesHaveAllDetails and (insideCounter == 7):
         validCounter = validCounter + 1
  
    insideCounter = 0

print ("These are the number of valid ones: " + str(validCounter))