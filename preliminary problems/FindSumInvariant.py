def bruteForceSum(sumTotal, array):

	numberIterations = 0

	for i in range(0, len(array)):
		for j in range(0, len(array)):
			numberIterations += 1
			if (array[i] + array[j] == sumTotal):
				return [array[i], array[j], numberIterations]

	return [0,0,0]

def hashSum(sumTotal, array):

	hashArray = [0]*10
	numberIterations = 0

	for i in range(0, len(array)):
		value = array[i]
		hashArray[value % 10] = value

	for i in range(0, len(array)):
		numberIterations += 1

		value = sumTotal - array[i]
		if (value == hashArray[value % 10]):
			return [array[i], hashArray[value % 10], numberIterations]

	return [0,0,0]

def invariantSum(sumTotal, array):

	numberIterations = 0
	i = 0
	j = len(array) - 1

	while (i <= j):
		numberIterations += 1

		if (array[i] + array[j] == sumTotal):
			return [array[i], array[j], numberIterations]
		elif (array[i] + array[j] < sumTotal):
			i += 1
		else:
			j += 1

	return [0,0,0]

array = [1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,21,22,22,25]
sumTotal = 27

# brute force approach
bruteResult = bruteForceSum(sumTotal, array)
print "\nBrute force iterations and results: iterations = " + str(bruteResult[2]) + " i = " + str(bruteResult[0]) + " j = " + str(bruteResult[1])

hashResult = hashSum(sumTotal, array)
print "\nHash iterations and results: iterations = " + str(hashResult[2]) + " i = " + str(hashResult[0]) + " j = " + str(hashResult[1])

invariantResult = invariantSum(sumTotal, array)
print "\nInvariant iterations and results: iterations = " + str(invariantResult[2]) + " i = " + str(invariantResult[0]) + " j = " + str(invariantResult[1])
print ""