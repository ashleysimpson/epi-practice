def divides(a,b):
	result = b
	while (result > 0):
		result = result - a

	if (result == 0):
		return 1
	else:
		return 0

def greatest_common_divisor(a,b):
	greatest_common_divisor = 1

	counter = 1
	while (counter <= a and counter <= b):
		a_divided = divides(counter,a)
		b_divided = divides(counter,b)

		if (a_divided == 1 and b_divided == 1):
			greatest_common_divisor = counter
		counter += 1

	return greatest_common_divisor

a = 163231
b = 135749

print greatest_common_divisor(a,b)