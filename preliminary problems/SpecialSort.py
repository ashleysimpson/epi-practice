import math

def quicksort(array):
	wall = 0
	pivot = len(array)-1

	if (pivot <= 0):
		return array

	while (wall < pivot):
		if (array[wall] > array[pivot]):
			temp = array[wall]
			array[wall] = array[pivot]
			array[pivot] = temp
			wall += 1
		else:
			pivot -= 1

	temp = array[wall]
	array[wall] = array[pivot]
	array[pivot] = temp

	return quicksort(array[0:wall]) + [array[wall]] + quicksort(array[wall+1:])

def bruteForce(array1, array2):

	return_list = []

	i = 0
	while (i < len(array2) and i < len(array1)):
		return_list += [array1[i],array2[i]]
		i += 1

	if (i < len(array1)):
		return_list += [array1[i]]

	if (i < len(array2)):
		return_list += [array2[i]]

	return return_list

def upperLowerAroundMedian(array):
	total = 0.0

	for i in range(0, len(array)):
		total += array[i]

	median = total / len(array)

	lowerArray = []
	upperArray = []

	for i in range(0, len(array)):
		if (array[i] <= median):
			lowerArray = [array[i]] + lowerArray
		else:
			upperArray = [array[i]] + upperArray

	return (lowerArray, upperArray)

def positionChecking(array):
	i = 0

	while ((i + 1) < len(array)):
		if ((((i % 2) == 0) and array[i] > array[i+1]) or (((i % 2) == 1) and array[i] < array[i+1])):
			temp = array[i]
			array[i] = array[i+1]
			array[i+1] = temp
		i += 1

	return array

unfixedList = [10,9,8,7,6,5,4,3,2]

sortedList = quicksort(unfixedList)
halfLength = int(math.ceil(len(sortedList) / 2.0))
bruteSpecialSort = bruteForce(sortedList[0:halfLength],sortedList[halfLength:])

print bruteSpecialSort

lowerUpperMedian = upperLowerAroundMedian(unfixedList)
betterSpecialSort = bruteForce(lowerUpperMedian[0], lowerUpperMedian[1])

print betterSpecialSort

unfixedList = [10,9,8,7,6,5,4,3,2]
bestSpecialSort = positionChecking(unfixedList)

print bestSpecialSort