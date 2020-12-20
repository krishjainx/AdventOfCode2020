with open('Day 7/input.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]


def get_bag_count(colour):
    rule = ''
    for line in data:
        if line[:line.index(" bags")] == colour:
            rule = line

    if "no" in rule:
        return 1

    rule = rule[rule.index("contain ")+8:].split()

    total = 0
    i = 0
    while i < len(rule):
        count = int(rule[i])
        colour = rule[i+1] + " " + rule[i+2]

        total += count * get_bag_count(colour)
        i = i + 4

    return total + 1


count = get_bag_count('shiny gold')
print(count - 1)
