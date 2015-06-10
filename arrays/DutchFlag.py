A = [1,2,3,2,1,1,2,3,2,1,2,3,2,1,2,3,3,2,1,2,3,1]

i = 0
lower = 0
upper = len(A) - 1
position = 0
value = A[position]

while (i < len(A)):
	if (i >= upper):
		if (A[i] == value):
			temp = A[i]
			A[i] = A[lower]
			A[lower] = temp
			lower += 1
		i += 1
	else:
		if (A[i] >= value):
			temp = A[i]
			A[i] = A[upper]
			A[upper] = temp
			upper -= 1
		else: 
			i += 1
			lower = i

print A