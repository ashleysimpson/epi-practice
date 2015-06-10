import random

def sort5(array5):
	for i in range(0,4):
		maxValue = 0
		minPosition = 6
		for j in range(i,5):
			if (maxValue < array5[j]):
				maxValue = array5[j]
				minPosition = j
		temp = array5[i]
		array5[i] = array5[minPosition]
		array5[minPosition] = temp

	return array5

array = [100,25,23,99,21,1,97,4,24,7,3,2,18,99,16,22,8,9,10,2,5,3,14,13,4]

random.shuffle(array)

unsortedArrays = [sort5(array[0:5])] + [sort5(array[5:10])] + [sort5(array[10:15])] + [sort5(array[15:20])] + [sort5(array[20:25])]

print unsortedArrays

sortedArrays = sort5(unsortedArrays)

print sortedArrays

finalSorted = []

# check the one position for order to have 5 numbers for sort5() method
if (sortedArrays[0][2] < sortedArrays[1][1]):
	finalSorted = sort5([sortedArrays[0][0],sortedArrays[0][1],sortedArrays[1][1],sortedArrays[1][0],sortedArrays[2][0]])
else:
	finalSorted = sort5([sortedArrays[0][0],sortedArrays[0][1],sortedArrays[0][2],sortedArrays[1][0],sortedArrays[2][0]])

print finalSorted

print "First: " + str(finalSorted[0]) + ", Second: " + str(finalSorted[1]) + ", Third: " + str(finalSorted[2])