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
xposition  = 0
yposition  = 0

#Raw command interpreter
def interpret(command):
	if   (command == "help"):
		help()
	elif (command == "go"):
		go()
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
	print ("Go")
	print ("Stats")
	print ("Help")
	print ("Quit")

def examine():
	object = raw_input("Examine what? ")
        global xposition
        global yposition
	if object == "area":
		print (map[xposition][yposition].description)
	elif object == "enemy":
		print ("Something about the object. yeah.")

def go():
	direction = raw_input("Go where?")
	if (direction == "up"):
		global yposition
		yposition += 1
	elif (direction == "down"):
		global yposition
		yposition -= 1
	elif (direction == "left"):
		global xposition
		xposition -= 1
	elif (direction == "right"):
		global xposition
		xposition += 1
	else:
		print ("That's not a direction")

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

#MapSquare Class
class MapSquare:
	def __init__(self, intro, description, walkable):
		self.intro       = intro
		self.description = description
		self.walkable    = walkable

#Map Definition 
map = [[MapSquare for x in xrange(5)] for x in xrange(5)]

forest = MapSquare("You look around to see lush green forests. Definitely not the way to go, but still very beautiful.", "You are in a forest", 0)



map[0][0] = forest
map[0][1] = forest
map[0][2] = forest
map[0][3] = forest
map[0][4] = forest

map[1][0] = forest
map[1][1] = forest
map[1][2] = forest
map[1][3] = forest
map[1][4] = forest

map[2][0] = forest
map[2][1] = forest
map[2][2] = forest
map[2][3] = forest
map[2][4] = forest

map[3][0] = forest
map[3][1] = forest
map[3][2] = forest
map[3][3] = forest
map[3][4] = forest

map[4][0] = forest
map[4][1] = forest
map[4][2] = forest
map[4][3] = forest
map[4][4] = forest

#Pregame setup
print ("Start your adventure by typing help")

#Core game loop
while (gameOver == 0):
	print
	interpret(raw_input())

#Closing statements
tmp = sp.call('clear',shell=True)
