#iterater over sequence of 10 numbers, 0-9
for x in range(10):
	print(x)

print("")

#iterate over sequence of 10 numbers, -0-9
for x in range(0, 10):
	print(x)

print("")

#iterate over sequence of 6 numbers, 1-6
for x in range(1, 7):
	print(x)

print("")

#iternate over sequence of 5 numbers, 0-28, skipping every 6 numbers
#range first digit is "start point", second digit is "maximum digit of range but not included", thrid digit is "steps"
#range can only accept "int" and never a "float"  
for x in range(0, 30, 7):
	print(x)

print("")

#iterate over sequence of 6 numbers, counting backwards from 5 - 0
for x in range(5, -1, -1):
	print(x)

print("")

#Find the numbers between 1 and 1000 that are odd
odd_numbers = []
for number in range(1, 1201):
	#if oddm append to odd numbers list
	if (number % 2 != 0):
		odd_numbers.append(number)

print(odd_numbers)