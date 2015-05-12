# input to be used for calculation
reverse_polish = raw_input("Please enter reverse polish input: ")
global stack
stack = []
splitup = reverse_polish.split(",")

def pop():
	global stack
	return_value = stack[0]
	stack = stack[1:]
	return return_value

def push(value):
	global stack
	stack = [value] + stack

for i in range(0, len(splitup)):
	
	if (splitup[i] == "+"):
		operand_1 = float(pop())
		operand_2 = float(pop())
		result = operand_1 + operand_2
		push(result)
	elif (splitup[i] == "-"):
		operand_1 = float(pop())
		operand_2 = float(pop())
		result = operand_1 - operand_2
		push(result)
	elif (splitup[i] == "*"):
		operand_1 = float(pop())
		operand_2 = float(pop())
		result = operand_1 * operand_2
		push(result)
	elif (splitup[i] == "/"):
		operand_1 = float(pop())
		operand_2 = float(pop())
		result = operand_2 / operand_1
		push(result)
	else:
		push(splitup[i])

print pop()