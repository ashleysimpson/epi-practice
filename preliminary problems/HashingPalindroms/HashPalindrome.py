def hashString(inputString):

	# create an empty hash table
	hashingTable = []
	for i in range(0, 26):
		hashingTable = hashingTable + [0]

	# go through each character
	for i in range(0, len(inputString)):
		# simple hashing function
		index = ord(inputString[i]) % 26

		hashingTable[index] += 1

	return hashingTable

# palindrome if number of odd chars is less than or equal to 1
def isPalindrome(hashTable, string):

	numberOfOddChars = 0

	# check each character
	for i in range(0, len(string)):
		if (hashTable[ord(string[i]) % 26] % 2 == 1):
			numberOfOddChars += 1

			# if odd number of chars found then make even to not count twice
			hashTable[ord(string[i]) % 26] -= 1

	if (numberOfOddChars <= 1):
		return "true"
	else:
		return "false"

inputString = raw_input("Please enter the input string (Only capital letters): ")

for i in range(0, len(inputString)):

	# check each character for proper input
	if (inputString[i] < 'A' or inputString[i] > 'Z'):
		print "Please enter proper format (capitals only)!"
		inputString = ""
		break

# if input good then call hashing
if (inputString != ""):
	hashTable = hashString(inputString)
	print isPalindrome(hashTable, inputString)
