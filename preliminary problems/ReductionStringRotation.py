def quadraticSolution(s,t):
	comparisons = 0

	if (len(s) != len(t)):
		return "false, comparisons: " + str(comparisons)

	if (len(s) == 0 or len(t) == 0):
		return "true, comparisons: " + str(comparisons)

	for i in range(0, len(t)):
		comparisons += 1
		if (s[0] == t[i]):
			match = 1
			for j in range(1, len(s)):
				comparisons += 1
				if (s[j] == t[(j + i) % len(t)] and match == 1):
					match = 1
				else:
					match = 0
					break
			if (match == 1):
				return "true, comparisons: " + str(comparisons)

	return "false, comparisons: " + str(comparisons)

def linearSolution(s,t):
	comparisons = 0

	if (len(s) != len(t)):
		return "false, comparisons: " + str(comparisons)

	if (len(s) == 0 or len(t) == 0):
		return "true, comparisons: " + str(comparisons)

	duplicate_t = t + t

	i = 0
	while(i < len(duplicate_t)):
		comparisons += 1
		j = 0
		previous_i = i
		if (s[j] == duplicate_t[i]):
			j += 1
			i += 1
			match = 1

			while (j < len(s) and match == 1 and i < len(duplicate_t)):
				comparisons += 1
				if (s[j] == duplicate_t[i]):
					match = 1
				else:
					match = 0
				j += 1
				i += 1

			if (match == 1 and j == len(s)):
				return "true, comparisons: " + str(comparisons)
		i = previous_i
		i += 1

	return "false, comparisons: " + str(comparisons)

s = "rarrrrr"
t = "arrrrrr"

print "Quadratic: " + quadraticSolution(s,t)
print "Linear: " + linearSolution(s,t)