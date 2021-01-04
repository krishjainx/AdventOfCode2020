import day9part1

print("Part 2")
contiguous_set = day9part1.getValidContinuousSet(day9part1.numbers, day9part1.invalid_total)
print(min(contiguous_set) + max(contiguous_set))