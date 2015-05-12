import os

x = ["1"]

iterations = int(raw_input("Please enter number of iterations: "))

for i in range(0, iterations):
	check_string = x[len(x)-1]
	counter = 1
	check_char = ""
	new_string = ""
	for j in range(0, len(check_string)):
		if (check_char == check_string[j] and j > 0):
			counter = counter + 1
		elif (j > 0):
			new_string = new_string + str(counter) + check_char
			counter = 1
			check_char = check_string[j]
		else:
			check_char = check_string[j]
	new_string = new_string + str(counter) + check_char
	x = x + [new_string]
		
print x