def reverseWords(s):
	i = len(s) - 1
	return_string = ""
	last_space = len(s)

	while(1):
		j = i + 1

		if (i == 0):
			while (i < last_space):
				return_string = return_string + s[i]
				i += 1
			return return_string

		if (s[i] == " "):
			while (j < last_space):
				return_string = return_string + s[j]
				j += 1
			return_string += " "
			last_space = i

		i -= 1

print reverseWords("Bob likes Alice")