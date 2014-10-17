#Clear Screen
import subprocess as sp
tmp = sp.call('clear',shell=True)

#Credit to authors
print
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to the Mountain of Mysteriousness")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~By~J~Cornelius~Fifelolz~~~and~~~Fifey~~")
print
print

#Starting Definitions
gameOver   = 0
name       = raw_input("What, adventurer, is thy name? ")
attack     = 5
defense    = 5
maxHealth  = 10
health     = maxHealth

#Situation definitions TODO add improvements and more Situation types
def situation(question, yes, no):
	print (question)
	response = raw_input("Y or N: ")
	if   (response == ("y")):
		print (yes)
	elif (response == ("n")):
		print (no)
	else:
		print ("Dolt...")
	print

#Raw command interpreter
def interpret(command):
	if   (command == "help"):
		help()
	elif (command == "stats"):
		stats()
	elif (command == "quit"):
		quit()
	else:
		print ("Speak up!")

#Commands
def help():
	print ("~~~~")
	print ("Examine")
	print ("Stats")
	print ("Help")
	print ("Quit")

def stats():
	print ("~~~~~")
	print (name)
	print ("Health : " + str(health) + " of " + str(maxHealth))
	print ("Attack : " + str(attack))
	print ("defense: " + str(defense))

def quit():
	global gameOver
	gameOver =1

#Pregame setup
print ("Start your adventure by typing help")

#Core game loop
while (gameOver == 0):
	print
	interpret(raw_input())

#Closing statements
tmp = sp.call('clear',shell=True)

