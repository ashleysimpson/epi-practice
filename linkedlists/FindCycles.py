def findCycles(list_head):
	double_speed_pointer = list_head
	single_speed_pointer = list_head

	# find the start of the cycle
	while (1):
		double_speed_pointer = double_speed_pointer.getChild()

		if (double_speed_pointer == None):
			return None

		double_speed_pointer = double_speed_pointer.getChild()

		if (double_speed_pointer == None):
			return None

		single_speed_pointer = single_speed_pointer.getChild()

		if (double_speed_pointer == single_speed_pointer):
			break

	# find the cycle length
	cycle_length = 0
	while(1):
		double_speed_pointer = double_speed_pointer.getChild()
		double_speed_pointer = double_speed_pointer.getChild()
		single_speed_pointer = single_speed_pointer.getChild()
		
		cycle_length += 1
	
		if (double_speed_pointer == single_speed_pointer):
			break

	cycle_start = 1
	single_speed_pointer = list_head
	double_speed_pointer = list_head
	for i in range(0,cycle_length):
		double_speed_pointer = double_speed_pointer.getChild()
	while(1):
		double_speed_pointer = double_speed_pointer.getChild()
		single_speed_pointer = single_speed_pointer.getChild()

		cycle_start += 1

		if (double_speed_pointer == single_speed_pointer):
			break

	return cycle_start

class LinkedListNode:
	def __init__(self,data):
		self.data = data
		self.child = None
	def getData(self):
		return self.data
	def getChild(self):
		return self.child
	def setData(self,data):
		self.data = data
	def setChild(self,node):
		self.child = node

no_cycle_head = LinkedListNode(1)
cycle_head = LinkedListNode(1)
previous_node_l1 = no_cycle_head
previous_node_l2 = cycle_head

for i in range(2,11):
	next_node_l1 = LinkedListNode(i)
	next_node_l2 = LinkedListNode(i)

	if (i == 2):
		cycle_node = next_node_l2

	previous_node_l1.setChild(next_node_l1)
	previous_node_l2.setChild(next_node_l2)
	previous_node_l1 = next_node_l1
	previous_node_l2 = next_node_l2

previous_node_l2.setChild(cycle_node)

print "No Cycle List:"
previous_node = no_cycle_head
print previous_node.getData()
while(1):
	next_node = previous_node.getChild()
	if (next_node == None):
		break
	print next_node.getData()
	previous_node = next_node

# print "Cycle List:"
# previous_node = cycle_head
# print previous_node.getData()
# while(1):
# 	next_node = previous_node.getChild()
# 	if (next_node == None):
# 		break
# 	print next_node.getData()
# 	previous_node = next_node

print findCycles(no_cycle_head)
print findCycles(cycle_head)