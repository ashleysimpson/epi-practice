def numberToLetters(num):
	if (num == 1):
		return [1]
	elif (num == 2):
		return ["A","B","C"]
	elif (num == 3):
		return ["D","E","F"]
	elif (num == 4):
		return ["G","H","I"]
	elif (num == 5):
		return ["J","K","L"]
	elif (num == 6):
		return ["M","N","O"]
	elif (num == 7):
		return ["P","Q","R","S"]
	elif (num == 8):
		return ["T","U","V"]
	elif (num == 9):
		return ["W","X","Y","Z"]
	else:
		return [0]

def numbersToLetters(num):
	if (len(num) == 0):
		return []

	i = len(num) - 1
	return_strings = numberToLetters(num[i])
	i -= 1

	while (i != -1):
		next_num = numberToLetters(num[i])

		return_strings *= len(next_num)
		tracker = len(next_num)
		length = len(return_strings)


		for j in range(0, len(return_strings)):
			return_strings[j] = next_num[j/(length/tracker)] + return_strings[j]

		i -= 1

	return return_strings

print numbersToLetters([2,2,7,6,6,9,6])