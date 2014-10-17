#Credit to the origonal author and myself
print
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to the Mountain of Mysteriousness")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~By~J~Cornelius~Fifelolz~~~and~~~Fifey~~")
print
print

#Starting Definitions
gameOver   = false
name       = raw_input("What, adventurer, is thy name")
attack     = 5
defense    = 5
maxHealth  = 10
health     = maxHealth

#Situation definitions TODO add improvements
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

#Core game loop
while (!gameOver)
	
