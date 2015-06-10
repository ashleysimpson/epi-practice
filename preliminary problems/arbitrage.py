import random
import time

USD = {"USD": 1, "EUR": 0.8148, "GBP": 0.6404, "JPY": 78.125, "CHF": 0.9784, "CAD": 0.9924, "AUD": 0.9465} 
EUR = {"USD": 1.2275, "EUR": 1, "GBP": 0.7860, "JPY": 96.550, "CHF": 1.2010, "CAD": 1.2182, "AUD": 1.1616}
GBP = {"USD": 1.5617, "EUR": 1.2724, "GBP": 1, "JPY": 122.83, "CHF": 1.5280, "CAD": 1.5498, "AUD": 1.4778}
JPY = {"USD": 0.0128, "EUR": 0.0104, "GBP": 0.0081, "JPY": 1, "CHF": 0.0124, "CAD": 0.0126, "AUD": 0.0120}
CHF = {"USD": 1.0219, "EUR": 0.8327, "GBP": 0.6546, "JPY": 80.39, "CHF": 1, "CAD": 1.0142, "AUD": 0.9672}
CAD = {"USD": 1.0076, "EUR": 0.8206, "GBP": 0.6453, "JPY": 79.26, "CHF": 0.9859, "CAD": 1, "AUD": 0.9535}
AUD = {"USD": 1.0567, "EUR": 0.8609, "GBP": 0.6767, "JPY": 83.12, "CHF": 1.0339, "CAD": 1.0487, "AUD": 1}

conversion = 1
country = "USD"
path = "USD"
maxConversion = 1
maxPath = "null"

money = 10000.0
counter = 0

while (1):
	money *= 1.03662426
	counter += 1
	print money
	print counter
	time.sleep(0.01)

while (1):
	if (country == "USD"):
		if (conversion > 1):
			if (conversion > maxConversion):
				maxConversion = conversion
				maxPath = path
				print path
				print conversion
				print ""

		choice = random.choice(USD.keys())
		while (choice == "USD"):
			choice = random.choice(USD.keys())

		conversion = 1 * USD[choice]
		country = choice
		path = "USD -> " + choice

	elif (country == "EUR"):

		choice = random.choice(EUR.keys())
		while (choice == "EUR"):
			choice = random.choice(EUR.keys())

		conversion *= EUR[choice]
		country = choice
		path = path + " -> " + choice

	elif (country == "GBP"):

		choice = random.choice(GBP.keys())
		while (choice == "GBP"):
			choice = random.choice(GBP.keys())

		conversion *= GBP[choice]
		country = choice
		path = path + " -> " + choice

	elif (country == "JPY"):

		choice = random.choice(JPY.keys())
		while (choice == "JPY"):
			choice = random.choice(JPY.keys())

		conversion *= JPY[choice]
		country = choice
		path = path + " -> " + choice

	elif (country == "CHF"):

		choice = random.choice(CHF.keys())
		while (choice == "CHF"):
			choice = random.choice(CHF.keys())

		conversion *= CHF[choice]
		country = choice
		path = path + " -> " + choice

	elif (country == "CAD"):

		choice = random.choice(CAD.keys())
		while (choice == "CAD"):
			choice = random.choice(CAD.keys())

		conversion *= CAD[choice]
		country = choice
		path = path + " -> " + choice

	else:

		choice = random.choice(AUD.keys())
		while (choice == "AUD"):
			choice = random.choice(AUD.keys())

		conversion *= AUD[choice]
		country = choice
		path = path + " -> " + choice
