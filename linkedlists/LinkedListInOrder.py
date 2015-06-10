def sort_two_lists(l1, l2):
	
	next_node_l1 = l1
	next_node_l2 = l2

	if (next_node_l1.getData() <= next_node_l2.getData()):
		return_head = next_node_l1
	else:
		return_head = next_node_l2

	while (1):
		if (next_node_l1.getData() <= next_node_l2.getData()):
			previous_node_l1 = next_node_l1
			next_node_l1 = next_node_l1.getChild()

			if (next_node_l1 == None):
				previous_node_l1.setChild(next_node_l2)
				break

			while(next_node_l1.getData() <= next_node_l2.getData()):
				previous_node_l1 = next_node_l1
				next_node_l1 = next_node_l1.getChild()

				if (next_node_l1 == None):
					break

			if (next_node_l1 == None):
				previous_node_l1.setChild(next_node_l2)
				break
			else:
				previous_node_l1.setChild(next_node_l2)
		else:
			previous_node_l2 = next_node_l2
			next_node_l2 = next_node_l2.getChild()

			if (next_node_l2 == None):
				previous_node_l2.setChild(next_node_l1)
				break

			while(next_node_l1.getData() > next_node_l2.getData()):
				previous_node_l2 = next_node_l2
				next_node_l2 = next_node_l2.getChild()

				if (next_node_l2 == None):
					break

			if (next_node_l2 == None):
				previous_node_l2.setChild(next_node_l1)
				break
			else:
				previous_node_l2.setChild(next_node_l1)

	return return_head


class LinkedListNode:

	def __init__(self, data):
		self.child = None
		self.data = data

	def getData(self):
		return self.data

	def getChild(self):
		return self.child

	def setData(self, data):
		self.data = data

	def setChild(self, node):
		self.child = node

head_node_l1 = LinkedListNode(1)
head_node_l2 = LinkedListNode(2)

next_node = head_node_l1
for i in range(1,30):
	data = i*3+1
	new_node = LinkedListNode(data)

	next_node.setChild(new_node)
	next_node = new_node

next_node = head_node_l2
for i in range(2,30):
	data = i*2
	new_node = LinkedListNode(data)

	next_node.setChild(new_node)
	next_node = new_node

next_node = head_node_l1
print ""
print "List 1:"
print next_node.getData()
while(next_node.getChild() != None):	
	next_node = next_node.getChild()
	print next_node.getData()
	if (next_node.getChild() == None):
		break

next_node = head_node_l2
print ""
print "List 2:"
print next_node.getData()
while(next_node.getChild() != None):
	next_node = next_node.getChild()
	print next_node.getData()
	if (next_node.getChild() == None):
		break

sorted_list_head = sort_two_lists(head_node_l1, head_node_l2)

next_node = sorted_list_head
print ""
print "List 3:"
print next_node.getData()
while(next_node.getChild() != None):
	next_node = next_node.getChild()
	print next_node.getData()
	if (next_node.getChild() == None):
		break