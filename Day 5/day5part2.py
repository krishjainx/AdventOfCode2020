import day5part1

day5part1.allValues = list(range(min(day5part1.arrayOfSeatID), max(day5part1.arrayOfSeatID)))

print(set(day5part1.allValues).difference(set(day5part1.arrayOfSeatID)))