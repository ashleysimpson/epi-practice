stack = []

def push(element):
	global stack

	# if empty add the appropriate condition
	if (len(stack) == 0):
		stack += [[element, element]]
	# else add the max association after a comparison
	else:
		end = len(stack) - 1

		if (stack[end][1] > element):
			stack += [[element, stack[end][1]]]
		else:
			stack += [[element, element]]

def pop():
	global stack 

	lastElement = stack.pop()

	return lastElement[0]

def maxInStack():
	global stack

	end = len(stack) - 1

	return stack[end][1]

while (1):
	commandInput = raw_input("Enter push, pop or max: ")

	if (commandInput == "push"):
		value = raw_input("Enter value to push: ")

		push(int(value))

		print "Value pushed!"
		print stack

	elif (commandInput == "pop"):
		if (len(stack) == 0):
			print "No elements in the stack..."
			continue

		else:
			print "This is the popped value: " + str(pop())
			print stack

	elif (commandInput == "max"):
		if (len(stack) == 0):
			print "No elements in the stack..."
			continue

		else :
			print "This is the max: " + str(maxInStack())
			print stack

	else:
		print "Command not recognised"
		continue