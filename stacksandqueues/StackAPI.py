
class Stack:
	def __init__(self):
		self.stack = []
	def push(self,value):
		if (len(self.stack) == 0):
			self.stack = self.stack + [[value, value]]
		else:
			if (value >= self.stack[len(self.stack) - 1][1]):
				self.stack = self.stack + [[value, value]]
			else:
				self.stack = self.stack + [[value, self.stack[len(self.stack) - 1][1]]]
	def pop(self):
		popped_value = self.stack[len(self.stack)-1][0]
		self.stack = self.stack[:-1]
		return popped_value
	def max(self):
		return self.stack[len(self.stack)-1][1]
	def length(self):
		return len(self.stack)

stack = Stack()

while(1):
	user_input = raw_input("Please enter the stack command push, pop, or max: ")

	if (user_input == "push"):
		push_input = raw_input("Please enter an int to push: ")

		try:
			int_value = int(push_input)
			stack.push(int_value)
			print push_input + " has been pushed!"
		except ValueError:
			print "Please enter an integer value!"

	elif (user_input == "pop"):

		if (stack.length() == 0):
			print "Nothing in the stack to pop!"
		else:
			popped_value = stack.pop()
			print str(popped_value) + " has been popped!"
	elif (user_input == "max"):

		if (stack.length() == 0):
			print "Nothing in the stack!"
		else:
			max_value = stack.max()
			print str(max_value) + " is the max in the stack!"
	else:
		"Please enter a correct command!"