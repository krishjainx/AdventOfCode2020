from day5part1 import arrayOfSeatID
from day5part1 import allValues

allValues = list(range(min(arrayOfSeatID), max(arrayOfSeatID)))
print(set(allValues).difference(set(arrayOfSeatID)))
