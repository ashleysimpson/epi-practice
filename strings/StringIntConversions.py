def intDecimalsToStringDecimals(decimal):
	if (decimal == 0):
		return "0"
	elif (decimal == 1):
		return "1"
	elif (decimal == 2):
		return "2"
	elif (decimal == 3):
		return "3"
	elif (decimal == 4):
		return "4"
	elif (decimal == 5):
		return "5"
	elif (decimal == 6):
		return "6"
	elif (decimal == 7):
		return "7"
	elif (decimal == 8):
		return "8"
	else:
		return "9"

def stringDecimalsToIntDecimals(decimal):
	if (decimal == "0"):
		return 0
	elif (decimal == "1"):
		return 1
	elif (decimal == "2"):
		return 2
	elif (decimal == "3"):
		return 3
	elif (decimal == "4"):
		return 4
	elif (decimal == "5"):
		return 5
	elif (decimal == "6"):
		return 6
	elif (decimal == "7"):
		return 7
	elif (decimal == "8"):
		return 8
	elif (decimal == "9"):
		return 9
	else:
		return -1

def intToString(s):
	try:
		check = s / 10
	except TypeError:
		return "Error, please supply an int!"

	return_string = ""

	neg = 0
	if (s < 0):
		s = s * -1
		neg = 1

	while (s != 0):
		check = intDecimalsToStringDecimals(s%10)
		return_string = check + return_string
		s = s - (s%10)
		s = s / 10

	if (neg == 1):
		return_string = "-" + return_string

	return return_string

def stringToInt(s):

	return_int = 0
	
	neg = 0
	if (s[0] == "-"):
		neg = 1

	end = -1
	if (neg == 1):
		end = 0

	i = len(s) - 1
	current_multiple_of_ten = 1
	while (i != end):
		value = stringDecimalsToIntDecimals(s[i])

		if (value == -1):
			return "Error, please supply a correct string!"

		return_int += value*current_multiple_of_ten

		current_multiple_of_ten *= 10
		i -= 1

	if (neg == 1):
		return_int *= -1

	return return_int

input_string = "12345"
input_int = 21312
bad_input = "2w1edwedwef"
input_neg_string = "-124"
input_neg_int = -13412

print intToString(input_int)
print intToString(input_neg_int)
print stringToInt(input_string)
print stringToInt(input_neg_string)
print intToString(bad_input)
print stringToInt(bad_input)