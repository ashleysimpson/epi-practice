import math

line1 = [[0.0,0.5],10.0,"red"]
line2 = [[0.5,1.0],11.0,"green"]
line3 = [[1.0,1.5],12.0,"blue"]
line4 = [[1.5,2.0],13.0,"yellow"]
line5 = [[0.4,0.6],9.0,"orange"]
line6 = [[0.9,1.1],14.0,"black"]
line7 = [[1.4,1.6],17.0,"white"]

listOfLines = [line1] + [line2] + [line3] + [line4] + [line5] + [line6] + [line7] 

class BST:
	BSTList = []

	def addNode(self, element):
		if (len(self.BSTList) == 0):
			self.BSTList += [element]
			return

		index = 0

		# find the place for the element
		while (index < len(self.BSTList)):
			if (self.BSTList[index] == -1):
				break
			# if point is the same
			if (self.BSTList[index][0] == element[0]):
				# if element bigger must update
				if (self.BSTList[index][1] < element[1]):
					self.BSTList[index] = element
				return
			# if the point is smaller
			elif (self.BSTList[index][0] > element[0]):
				index = self.getLeftChild(index)
			# or if the point is bigger
			else:
				index = self.getRightChild(index)

		if (index >= len(self.BSTList)):
			pointer = len(self.BSTList)

		# initialize nodes that haven't been initialized
			for i in range(pointer, index+1):
				self.BSTList += [-1]

		self.BSTList[index] = element
		
	def getLeftChild(self, index):
		return (2*index + 1)

	def getRightChild(self, index):
		return (2*index + 2)

	def getParent(self, index):
		return int(math.ceil(float(index)/2.0) - 1.0)

	def getPositionColour(self, position):

		index = 0

		while (index < len(self.BSTList)):
			if (self.BSTList[index] == -1):
				break
			if (self.BSTList[index][0] == position):
				return self.BSTList[index][2]
			elif (self.BSTList[index][0] > position):
				index = self.getLeftChild(index)
			else: 
				index = self.getRightChild(index)

		previousIndex = self.getParent(index)
		index = self.getParent(previousIndex)

		while (index >= 0):

			if ((self.BSTList[previousIndex][0] < position and self.BSTList[index][0] > position)):
				if (self.BSTList[previousIndex][0] < self.BSTList[index][0]):
					return self.BSTList[previousIndex][2]
				else:
					return self.BSTList[index][2]

			if ((self.BSTList[previousIndex][0] > position and self.BSTList[index][0] < position)):
				if (self.BSTList[previousIndex][0] < self.BSTList[index][0]):
					return self.BSTList[previousIndex][2]
				else:
					return self.BSTList[index][2]

			if (index == 0):
				index = -1

			previousIndex = index
			index = self.getParent(index)

		return "out of range"

# create a BST
bst = BST()

maxPosition = -10000
maxInfo = []
minPosition = 10000
minInfo = []

# go through the lists of sets and 
for i in range(0,len(listOfLines)):
	start = listOfLines[i][0][0]
	finish = listOfLines[i][0][1]
	height = listOfLines[i][1]
	colour = listOfLines[i][2]

	# compare against all other sets, remove duplicates
	for j in range(0,len(listOfLines)):
		if (i == j):
			continue

		# intersection at finish
		if (finish > maxPosition):
			maxPosition = finish
			maxInfo = listOfLines[i] 

		# intersection at start
		if (start < minPosition):
			minPosition = start
			minInfo = listOfLines[i]

		if (listOfLines[j][0][0] <= finish and listOfLines[j][0][0] >= start):
			# check height difference
			if (listOfLines[j][1] < height):
				intersectPoint = listOfLines[j][0][0]
				biggestHeight = height
				shownColour = colour

				bst.addNode([intersectPoint,biggestHeight,shownColour])

				# check if a move is required
				if (listOfLines[j][0][1] > finish):
					bst.addNode([finish+0.0001,listOfLines[j][1],listOfLines[j][2]])
					listOfLines += [[[finish+0.0001,finish+0.0001],listOfLines[j][1],listOfLines[j][2]]]
			else:
				intersectPoint = listOfLines[j][0][0]
				biggestHeight = listOfLines[j][1]
				shownColour = listOfLines[j][2]

				bst.addNode([intersectPoint,biggestHeight,shownColour])
		# intersection at end
		if (listOfLines[j][0][1] <= finish and listOfLines[j][0][1] >= start):
			# check height difference
			if (listOfLines[j][1] < height):
				intersectPoint = listOfLines[j][0][1]
				biggestHeight = height
				shownColour = colour

				bst.addNode([intersectPoint,biggestHeight,shownColour])

				# check if a move is required
				if (listOfLines[j][0][0] < start):
					bst.addNode([start-0.0001,listOfLines[j][1],listOfLines[j][2]])
					listOfLines += [[[start-0.0001,start-0.0001],listOfLines[j][1],listOfLines[j][2]]]
			else:
				intersectPoint = listOfLines[j][0][1]
				biggestHeight = listOfLines[j][1]
				shownColour = listOfLines[j][2]

				bst.addNode([intersectPoint,biggestHeight,shownColour])

bst.addNode([maxPosition,maxInfo[1],maxInfo[2]])
bst.addNode([minPosition,minInfo[1],minInfo[2]])

print bst.BSTList

while (1):
	inputPosition = float(raw_input("Please enter position: "))

	print bst.getPositionColour(inputPosition)