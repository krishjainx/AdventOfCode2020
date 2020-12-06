input = open('/Users/krishjain/Desktop/AdventOfCode/Day 6/input.txt', "r").read()
input = input.split("\n\n")

countOfAnswersPerGroup = []

for i in input:
    listOfAnswersToWhichAnsweredYes = []
    
    for j in i.replace("\n", ""):
        listOfAnswersToWhichAnsweredYes.append(j)

    unorderedListOfAnswers = list(dict.fromkeys(listOfAnswersToWhichAnsweredYes))
    orderedListOfAnswers = sorted(unorderedListOfAnswers)
    countOfAnswersPerGroup.append(len(orderedListOfAnswers))

sumOfCounts = sum(countOfAnswersPerGroup)
print("Answer is: " + str(sumOfCounts))

 