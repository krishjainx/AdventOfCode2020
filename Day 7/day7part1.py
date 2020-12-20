with open('Day 7/input.txt') as file:
    data = file.readlines()
    data = [line.strip() for line in data]


def get_num_bags(colour):

    lines = [line for line in data if colour in line and line.index(colour) != 0] #Lines that have shiny gold directly 
    # The abpve checks does line for line in data if the colour is present on line and line.index(colour) isn't 0
    allcolours = []  # keep track of colours already checked

    if len(lines) == 0:
        return []
    else:
        colours = [line[:line.index(" bags")] for line in lines]
        colours = [colour for colour in colours if colour not in allcolours]

        for colour in colours:
            allcolours.append(colour)
            bags = get_num_bags(colour)

            allcolours = allcolours + bags

        uniquecolours = []
        for colour in allcolours:
            if colour not in uniquecolours:
                uniquecolours.append(colour)
        return uniquecolours


colours = get_num_bags('shiny gold')

print(len(colours))

