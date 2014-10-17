#Credit to the origonal author and myself
print
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to the Mountain of Mysteriousness")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~By~J~Cornelius~Fifelolz~~~and~~~Fifey~~")
print
print

#Starting Definitions
gameOver   = 0
name       = raw_input("What, adventurer, is thy name")
attack     = 5
defense    = 5
maxHealth  = 10
health     = maxHealth

#Situation definitions TODO add improvements and more Situation types
def situation(question, yes, no):
	print (question)
	response = raw_input("Y or N: ")
	if response == ("y"):
		print (yes)
	elif response == ("n"):
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
	else:
		print ("Speak up!")
		print

#Commands
def help():
	print ("Examine")
	print ("Stats")
	print ("Quit")
	print

def stats():
	print (name)
	print ("Health : " + health + " of " + maxHealth)
	print ("Attack : " + attack)
	print ("defense: " + defense)
	print

#Core game loop
while (not gameOver):
	interpret(raw_input())
	
