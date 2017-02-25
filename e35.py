from sys import exit
def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("---> ")

	if "0" in next or "1" in next: 
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
#	next = int(raw_input("---> "))
#	how_much = int(next)
#	if how_much < 50:		
		print "Nice, you're not greedy, you win!"
		exit(0)

	else:
		dead("You greedy bastard!")

def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

	while True:    #"While True:" would make an INFINITE loop
		next = raw_input("---> ")

		if next == "take honey":
			dead("The bear looks at you then slaps your face off.")
		
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
			#First time taunting. Python would stop running blocks here since Python starts at the top and runs the first block that is True
		
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews you leg off.")
			#Second time tauning. Since "bear_moved = True" now, Python would skip the block  above(which is the first "taunt bear" block.) So users can taunt bear for only ONE time.
		
		elif next == "open door" and bear_moved:
			gold_room()
		
		else:
			print "I got no idea what that means."

def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee for your life or eat your head?"

	next = raw_input("---> ")

	if "flee" in next:
		start()
	
	elif "head" in next:
		dead("Well that was tasty!")
	
	else:
		cthulhu_room()

def dead(why):
	print why, "Good job!"
	exit(0)    #a program can abort with exit(0), and the number passed in will indicate an error or not. If you do exit(1), then it will be an error, but exit(0) will be a good exit.

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

	next = raw_input("---> ")

	if next == "left":
		bear_room()
	
	elif next == "right":
		cthulhu_room()
	
	else:
		dead("You stumble around the room until you starve.")

start()

#Q1_Draw a map of the game and how you flow through it.
#A1_See e35_map.png

#TIPS
#1. Every if-statement must have an else.
#2. Never nest if-statements more than two deep and always try to do them one deep.
#3. Treat if-statements like paragraphs, where each if, elif, else grouping is like a set of sentences. Put blank lines before and after.
#4. Boolean tests should be simple.
