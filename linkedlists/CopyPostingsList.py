def copyPostingsList(list_head):
	
	# check empty node
	if (list_head == None):
		return None

	# first pass
	next_node = list_head
	copy_list_head = LinkedListNode(next_node.getData())
	copy_next_node = copy_list_head
	while(1):
		next_node_actual = next_node.getNext()
		next_node.setNext(copy_next_node)
		copy_next_node.setNext(next_node_actual)

		if (next_node_actual == None):
			break

		next_node = next_node_actual
		copy_next_node = LinkedListNode(next_node.getData())

	# second pass
	next_node = list_head
	copy_next_node = copy_list_head
	while(1):
		next_jump = next_node.getJump()
		copy_next_jump = next_jump.getNext()
		copy_next_node.setJump(copy_next_jump)

		if (copy_next_node.getNext() == None):
			break

		next_node = copy_next_node.getNext()
		copy_next_node = next_node.getNext()

	# third pass
	next_node = list_head
	copy_next_node = copy_list_head
	while(1):
		next_actual = copy_next_node.getNext()
		next_node.setNext(next_actual)

		if (next_actual == None):
			copy_next_node.setNext(None)
			break

		copy_next_node.setNext(next_actual.getNext())
		next_node = next_actual
		copy_next_node = next_actual.getNext()

	return copy_list_head

class LinkedListNode:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.jump = None

	def getData(self):
		return self.data
	def getNext(self):
		return self.next
	def getJump(self):
		return self.jump

	def setNext(self, node):
		self.next = node
	def setData(self, data):
		self.data = data
	def setJump(self, node):
		self.jump = node

head_node = LinkedListNode(1)
next_node = head_node

for i in range(2,10):
	new_node = LinkedListNode(i)
	next_node.setNext(new_node)
	new_node.setJump(next_node)
	next_node = new_node

head_node.setJump(next_node)

print "List:"
next_node = head_node
while(1):
	if (next_node == None):
		break
	print next_node.getData()
	next_node = next_node.getNext()

print "Jumps:"
next_node = head_node
while(1):
	if (next_node == None):
		break
	print next_node.getJump().getData()
	next_node = next_node.getNext()

copy_head_node = copyPostingsList(head_node)

print ""
print "Copy List:"
next_node = copy_head_node
while(1):
	if (next_node == None):
		break
	print next_node.getData()
	next_node = next_node.getNext()

print "Copy Jumps:"
next_node = copy_head_node
while(1):
	if (next_node == None):
		break
	print next_node.getJump().getData()
	next_node = next_node.getNext()