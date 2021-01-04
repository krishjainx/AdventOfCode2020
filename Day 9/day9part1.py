def getValidContinuousSet(numbers, total):
	for length in range(2, len(numbers)+1):
		for offset in range(len(numbers)-length+1):
			contiguous_set = numbers[offset:offset+length]
			if sum(contiguous_set) == total:
				return contiguous_set

with open("Day 9/input.txt", "r") as file:
	numbers = list(map(int, file.read().split()))

lengthOfPreamble = 25
for i in range(len(numbers) - lengthOfPreamble):
	previous_numbers = numbers[i:i+lengthOfPreamble]
	total = numbers[i+lengthOfPreamble]
	total_valid = False
	for num1 in previous_numbers:
		for num2 in previous_numbers:
			if num1 + num2 == total:
				total_valid = True
	if not total_valid:
		invalid_total = total




print("Part 1")
print(invalid_total)

