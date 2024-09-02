# Main file for DNDice

import random
from time import sleep

output = []
rolls = []
userValues = []

def helpMenu():
	print('''Controls:
e[X]it
[C]lear
[R]oll

Usage:
Use the format D# where # is the number of possible outcomes, e.g. D6 would be a 6 sided dice.
A preceding number can be used to roll multiple of the same dice, e.g. 3D6 would roll 3 6 sided die.''')

def startPrompt():
	print('''Enter values to roll:
Use ? for help, e[X]it, [C]lear, [R]oll

*Notice* Full words are not accepted as commands, e.g. exit is not accepted but x is.''')

def roll():
	for index in rolls:
		output.append("[" + str(index) + "]")
	print("Results: " + ' '.join(output))
	print("Total: " + str(sum(rolls)))

def Main():
	userinput = (input("> ").replace(" ", "")).lower()

	if userinput == "?": helpMenu(), Main()
	elif userinput == "x": print("Exiting..."), sleep(0.35), quit()
	elif userinput == "c": userValues = [], Main()
	elif userinput == "r": roll(), Main()

	userValues = userinput.split("d")
	if userValues[0] == "": userValues[0] = "1"

	try:
		userValues = list(map(int, userValues))
	except:
		print("Input error")
		Main()

	print(str(userValues[0]) + "D" + str(userValues[1]) + " dice was added.")


	for n in range(userValues[0]):
		rolls.append(random.randint(1,userValues[1]))

	Main()


startPrompt()
Main()
