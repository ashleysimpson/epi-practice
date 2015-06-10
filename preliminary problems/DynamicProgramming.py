dynamicList = [0,0,1,1,1,2,2,4]

# dynamic program example
def combinationChange(number):
	global dynamicList

	dynamicList += [dynamicList[number-7] + dynamicList[number-3] + dynamicList[number-2]]

for i in range(8, 223):
	combinationChange(i)

print dynamicList
print dynamicList[222]