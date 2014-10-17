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
xposition  = 2
yposition  = 2

#Raw command interpreter
def interpret(command):
	if   (command == "help"):
		help()
	elif (command == "stats"):
		stats()
	elif (command == "examine"):
		examine()
	elif (command == "hack"):
		hackGame()
	elif (command == "quit"):
		quit()
	else:
		print ("Speak up!")

#User Commands
def help():
	print ("~~~~")
	print ("Examine")
	print ("Stats")
	print ("Help")
	print ("Quit")

def examine():
	global xposition
	global yposition
	print (map[xposition][yposition])

def stats():
	print ("~~~~~")
	print (name)
	print ("Health : " + str(health) + " of " + str(maxHealth))
	print ("Attack : " + str(attack))
	print ("Defense: " + str(defense))

def hackGame():
	increase = int(raw_input("How much you wanna hack? "))
	modifyStats(increase, increase, increase, increase)

def quit():
	global gameOver
	gameOver =1

#System Commands
def modifyStats(hp, mh, ak, df):
	global health
	global maxHealth
	global attack
	global defense
        health    = (health    + hp)
	maxHealth = (maxHealth + mh)
	attack    = (attack    + ak)
	defense   = (defense   + df)

#Map Definition 
map = [["" for x in xrange(5)] for x in xrange(5)]
map[0][0] = "You are in a forest"
map[0][1] = "You are in a forest"
map[0][2] = "You are in a forest"
map[0][3] = "You are in a forest"
map[0][4] = "You are in a forest"

#Pregame setup
print ("Start your adventure by typing help")

#Core game loop
while (gameOver == 0):
	print
	interpret(raw_input())

#Closing statements
tmp = sp.call('clear',shell=True)
