print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("---> ")

if door == "1":
	print "There are two boxes here. What do you do?"
	print "1. Take the red one."
	print "2. Take the blue one."

	box = raw_input("---> ")

	if box == "1":
		print "Here you get a weapon and a map. Touch spots in the map to go to another world. What do you do?"
		print "1. Touch the left one."
		print "2. Touch the right one."

		map_touch = raw_input("---> ")

		if map_touch == "1":
			print "Yep, Welcome to paradise."
		elif map_touch == "2":
			print "Yep, Welcome to NewYork."
		else:
			print "You touched the wrong place!"
	elif box == "2":
		print "There're two capsules here. You have to choose one of them otherwise you will die for disease. What do you do?"
		print "1. Take the bigger one."
		print "2. Take the smaller one."

		capsule = raw_input("---> ")

		if capsule == "1":
			print "Congratulations! You become to SUPERMAN now!"
		elif capsule == "2":
			print "Congratulations! You are Batman now!"
		else:
			print "Game Over."

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("--->")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"

