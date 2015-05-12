import os
import math

path = "/Users/as_763/desktop/practice/trades/"

# heap class, used to 
class Heap:
	def __init__(self):
		self.heap = []

	def getParent(self,element):
		return int((math.ceil(float(element)/float(2)) - 1))

	def getLeftChild(self,element):
		return (element * 2) + 1

	def getRightChild(self, element):
		return (element * 2) + 2

	def reorderMinHeapInsertion(self):
		endElement = len(self.heap) - 1
		if (endElement == 0):
			return
		parentElement = self.getParent(endElement)

		# check each parent for min heap property
		while(self.heap[parentElement][0] > self.heap[endElement][0]):
			temp = self.heap[parentElement]
			self.heap[parentElement] = self.heap[endElement]
			self.heap[endElement]= temp

			endElement = parentElement

			# at the root node, just break here, ordering complete
			if (parentElement == 0):
				break

			parentElement = self.getParent(endElement)
		return

	def reorderMinHeapReturnMin(self):
		maxLength = len(self.heap)
		parentElement = 0;
		leftChildElement = self.getLeftChild(parentElement)
		rightChildElement = self.getRightChild(parentElement)

		while (1):
			if (rightChildElement >= maxLength):
				if  (leftChildElement >= maxLength):
					return
				if (self.heap[leftChildElement] < self.heap[parentElement]):
					temp = self.heap[leftChildElement]
					self.heap[leftChildElement] = self.heap[parentElement]
					self.heap[parentElement] = temp
					return
				return
			else:
				if (self.heap[rightChildElement] <= self.heap[leftChildElement]):
					temp = self.heap[rightChildElement]
					self.heap[rightChildElement] = self.heap[parentElement]
					self.heap[parentElement] = temp
					parentElement = rightChildElement
				else:
					temp = self.heap[leftChildElement]
					self.heap[leftChildElement] = self.heap[parentElement]
					self.heap[parentElement] = temp
					parentElement = leftChildElement
			leftChildElement = self.getLeftChild(parentElement)
			rightChildElement = self.getRightChild(parentElement)

		# add the functionality here to reorder from root
		return

	def addNewTradeToHeap(self, pathToFile, timestamp):
		
		openFile = open(pathToFile, 'r')
		nextTrade = openFile.readline().strip('\n')
		
		while (nextTrade != timestamp):
			nextTrade = openFile.readline()

		nextTrade = openFile.readline()

		if (nextTrade == ""):
			openFile.close()
			return

		print nextTrade

		self.addElement([nextTrade,pathToFile])

		openFile.close()

		return

	def addElement(self, element):
		self.heap = self.heap + [element]
		self.reorderMinHeapInsertion()
		return

	def getMinElement(self):
		# base cases
		if (len(self.heap) == 0):
			return ""
		if (len(self.heap) == 1):
			returnElement = self.heap.pop()
			self.addNewTradeToHeap(returnElement[1], returnElement[0])
			return returnElement[0]

		# deal with returning the min and reordering
		returnElement = self.heap[0]
		self.heap[0] = self.heap.pop()
		self.reorderMinHeapReturnMin()

		# call a function to add the next timestamp from the file
		self.addNewTradeToHeap(returnElement[1], returnElement[0])

		return returnElement[0]


def setupHeap(tradesFileLocation):
	heap = Heap()

	for i in range(0,len(tradesFileLocation)):
		heapElement = []
		tradeFile = open(tradesFileLocation[i],'r')

		heapElement = [tradeFile.readline().strip('\n'),tradesFileLocation[i]]

		heap.addElement(heapElement)

		tradeFile.close()

	return heap

priorityQueue = []

tradesFileLocation = os.listdir(path)

# setup the correct file names for easier manipulation
for i in range(0,len(tradesFileLocation)):
	tradesFileLocation[i] = path + tradesFileLocation[i]

# create the heap
fileHeap = setupHeap(tradesFileLocation)

nextElementToQueue = "initialization"

# continue adding to priority queue until no more to add
while (nextElementToQueue != ""):
	nextElementToQueue = fileHeap.getMinElement()
	if (nextElementToQueue != ""):
		priorityQueue = priorityQueue + [nextElementToQueue.strip('\n')]

print priorityQueue