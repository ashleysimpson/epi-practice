def naive_approach(array_of_64s):
	return_parity = []
	for i in range(0, len(array_of_64s)):
		checker = long(1)
		number_of_bits = 0
		for j in range(0, 64):
			if (checker & array_of_64s[i] == checker):
				number_of_bits += 1
			checker = checker << 1
		if (number_of_bits % 2 == 1):
			return_parity += [1]
		else :
			return_parity += [0]
	return return_parity

long_1 = long(1)
long_2 = long(2)
long_3 = long(4)
long_4 = long(96)
long_5 = long(224)
array = [long_1,long_2,long_3,long_4,long_5]

print naive_approach(array)