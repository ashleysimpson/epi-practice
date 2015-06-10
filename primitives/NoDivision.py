def divideWithNoDivisionNaive(x, y):
	if (x < y):
		return 0
	else:
		return 1 + divideWithNoDivisionNaive(x-y,y)

# fix this
def divideWithNoDivision(x, y):
	value = 0

	return value

print divideWithNoDivisionNaive(18,6)
print divideWithNoDivision(18,6)
print 18/6