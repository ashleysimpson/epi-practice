def brute_force(s, t):
	offset_matches = []
	comparisons = 0

	i = 0
	while (i <= (len(t) - len(s))):
		match = 1

		for j in range(0, len(s)):

			comparisons += 1

			if (s[j] == t[i+j]):
				match = 1
			else:
				match = 0
				break

		if (match == 1):
			offset_matches += [i]

		i += 1

	print comparisons
	return offset_matches

def second_best_matching(s, t):
	offset_matches =[]
	comparisons = 0

	i = len(t) - len(s)
	while (i >= 0):
		match = 1
		offset_point = i

		for j in range(len(s)-1,-1,-1):

			comparisons += 1

			if (t[i+j] == s[j]):
				match = 1
			else:
				match = 0
				offset_point = i+j
				break

		if (match == 1):
			offset_matches += [i]
			i -= 1
		else:
			previous_i = i
			i = offset_point - len(s)

	print comparisons
	return offset_matches

def boyer_moore_string(s, t):
	offset_matches =[]
	comparisons = 0

	print comparisons
	return offset_matches

s = "hhhh"
t = "hhahhahha"

print brute_force(s, t)
print second_best_matching(s, t)
print boyer_moore_string(s, t)