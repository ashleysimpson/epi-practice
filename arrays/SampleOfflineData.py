import random

def k_subsets(array, k):

	subsets = []

	for i in range(0,k):
		subsets += [[]]

	i = 0
	while(len(array) != 0):
		index = random.randint(0,len(array)-1)

		temp = array[index]
		array[index] = array[len(array)-1]
		array[len(array)-1] = temp

		subsets[i%k] += [array.pop()]
		i += 1

	return subsets

array = [1,2,3,4,5,6,7,8,9]
k = 3

print k_subsets(array, k)