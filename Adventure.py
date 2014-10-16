print
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("Welcome to the Mountain of Mysteriousness")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~By~J~Cornelius~Fifelolz~~~~~~~~~~~~~~~")
print
print

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

situation("You are finished preparing for your journey! Do you leave home in search of adventure?" , "Cool!" , "Too Bad!")
situation("You are hungry. Do you eat?" , "Cool!" , "That's gonna suck in like an hour or so...")
print ("Game Over!")
