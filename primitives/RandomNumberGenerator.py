import random
import math
import time

def randomZeroOne():
	randomNumber = random.random()
	if (randomNumber < 0.5):
		return 0
	else:
		return 1

def randomInRange(a, b):
	
	total = 0

	while (a > total or total > b):
		total = 0
		bit_tracker = 0

		while (bit_tracker < b):
			total += math.pow(2,bit_tracker)*randomZeroOne()
			
			if (bit_tracker == 0):
				bit_tracker = 1
			else:
				bit_tracker = bit_tracker << 1

	return int(total)

a = -1
while (a < 0):
	try:
		a = int(raw_input("Please enter lower range: "))
		if (a < 0):
			print "Enter a positive int!"
	except ValueError:
		print "Enter an int!"

print a

b = -1
while (b < a):
	try:
		b = int(raw_input("Please enter upper range: "))
		if (b < a):
			print "Please enter a number not smaller than a!"
	except ValueError:
		print "Enter an int!"


counter = 0
tracked_list = []

while (counter < int(b)):
	tracked_list += [0]
	counter += 1

counter = 0

while (counter < 100000):	
	tracked_list[randomInRange(a,b)-1] += 1
	counter += 1

print tracked_list