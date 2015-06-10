def reverse_linked_list(original_list):

	previous_node = original_list
	next_node = previous_node.get_child()
	original_list.set_child(None)
	while(1):
		if (next_node == None):
			break
		save_node = next_node.get_child()
		next_node.set_child(previous_node)
		previous_node = next_node
		next_node = save_node

	return previous_node

class LinkedListNode:
	def __init__(self, data):
		self.child = None
		self.data = data

	def get_child(self):
		return self.child

	def get_data(self):
		return self.data

	def set_child(self, node):
		self.child = node

	def set_data(self, data):
		self.data = data

head_node = LinkedListNode(2)

previous_node = head_node
for i in range(2,50):
	data = i*2
	next_node = LinkedListNode(data)
	previous_node.set_child(next_node)
	previous_node = next_node

print "List 1:"
print head_node.get_data()
next_node = head_node.get_child()
while (1):
	if (next_node == None):
		break
	print next_node.get_data()
	next_node = next_node.get_child()

reversed_head = reverse_linked_list(head_node)

print "List 2:"
print reversed_head.get_data()
next_node = reversed_head.get_child()
while (1):
	if (next_node == None):
		break
	print next_node.get_data()
	next_node = next_node.get_child()