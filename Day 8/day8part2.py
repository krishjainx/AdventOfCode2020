with open('Day 8/input.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]


def get_endoffile(data):
    acc = 0
    arrayOfInstructionsDone = []
    instructionNumber = 0

    while (instructionNumber) < (len(data) - 1):
        if instructionNumber in arrayOfInstructionsDone:
            return acc, False  # infinite loop

        arrayOfInstructionsDone.append(instructionNumber)
        opcode = data[instructionNumber].split()[0]
        operand = data[instructionNumber].split()[1]

        if opcode == "nop":
            instructionNumber = instructionNumber + 1
            continue

        if opcode == "acc":
            subtractOrPlus = operand[:1]
            numberValue = int(operand[1:])

            if subtractOrPlus == "+":
                acc = acc + numberValue

            if subtractOrPlus == "-":
                acc = acc - numberValue

        if opcode == "jmp":
            subtractOrPlus = operand[:1]
            numberValue = int(operand[1:])

            if subtractOrPlus == "+":
                instructionNumber = instructionNumber + numberValue

            if subtractOrPlus == "-":
                instructionNumber = instructionNumber - numberValue

        if opcode != "jmp":
            instructionNumber = instructionNumber + 1
    return acc, True  # it finished without getting into an infinite loop

# acc, trueFalse = get_endoffile(data)


for i in range(len(data)):

    if "jmp" in data[i]:
        data[i] = data[i].replace("jmp", "nop")
        acc, found = get_endoffile(data)

        if found:
            print(acc)
            break
        else:
            data[i] = data[i].replace("nop", "jmp")