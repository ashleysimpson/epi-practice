import math

def tostring(value):
	if (value <= 9):
		return str(value)
	elif (value == 10):
		return "A"
	elif (value == 11):
		return "B"
	elif (value == 12):
		return "C"
	elif (value == 13):
		return "D"
	elif (value == 14):
		return "E"
	else:
		return "F"

def convert_base(b1, s, b2):
	
	in_base_10 = 0
	power_tracker = len(s) - 1
	
	for i in range(0, len(s)):
		in_base_10 += int(s[i]) * math.pow(b1, power_tracker)
		power_tracker -= 1

	print in_base_10

	converted_int = ""

	while (in_base_10 != 0):
		divided = in_base_10 / b2
		remainder = divided - int(divided)
		value = remainder * b2
		str_value = tostring(int(str(value).split('.')[0]))
		converted_int = str_value + converted_int
		in_base_10 = math.floor(divided)

	return converted_int

print convert_base(6, "12345", 12)

