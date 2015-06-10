def mergesort(mergeList):

	if (len(mergeList) <= 1):
		return mergeList

	mid = len(mergeList) / 2

	return merge(mergesort(mergeList[:mid]),mergesort(mergeList[mid:]))


def merge(mergeList1, mergeList2):

	returnList = []

	i = 0
	j = 0
	while (i < len(mergeList1) and j < len(mergeList2)):
		if (mergeList1[i][1] < mergeList2[j][1]):
			returnList += [mergeList1[i]]
			i += 1
		else :
			returnList += [mergeList2[j]]
			j += 1

	if (i == len(mergeList1)):
		while (j < len(mergeList2)):
			returnList += [mergeList2[j]]
			j += 1

	if (j == len(mergeList2)):
		while (i < len(mergeList1)):
			returnList += [mergeList1[i]]
			i += 1

	return returnList

def reorderLineSegments(lineList):

	for i in range(0, len(lineList)):
		if (lineList[i][0] > lineList[i][1]):
			temp = lineList[i][0]
			lineList[i][0] = lineList[i][1]
			lineList[i][1] = temp

	return lineList
 
def getMaximumNumberIntersects(sortedList):

	maximumIntersects = 0
	i = 0

	while (i < len(sortedList)):
		localMax = 0
		j = i + 1
		while (j < len(sortedList)):
			if (sortedList[j][0] <= sortedList[i][1]):
				localMax += 1
			j += 1
		if (localMax > maximumIntersects):
			maximumIntersects = localMax
		i += 1

	return maximumIntersects

unsortedList = [[1,9],[2,8],[3,7],[4,6],[5,6],[6,7],[7,7],[8,8],[9,0]]
unsortedList = reorderLineSegments(unsortedList)

print unsortedList

sortedList = mergesort(unsortedList)

maximumIntersects = getMaximumNumberIntersects(sortedList)

print sortedList
print maximumIntersects