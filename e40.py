# -*- coding: utf-8 -*-

'''
The statement “object-oriented programming language” means there’s a construct in Python called a class that lets you structure your software in a particular way. Using classes, you can add consistency to your programs so that they can be used in a cleaner way

Modules ≒ dict(dictionaries)
	Regard MODULE as a bigger dict. (almost the same thing.)    #a specialized dictionary that can store Python code so you can get to it with the '.' operator
	The common pattern between dict and module.
		1. Take a key = value style container
		2. Get something out of it by the key's name.
	In the case of the dict, 
		key == a string
		syntax == [key]
	In the case of the module,
		key == identifier
		syntax == .key0-】

Classes ≒ Modules
	class == a way to take a grouping of ①functions and ②data and place them inside a container so you can access them with the '.' (dot) operator.
	Advantages of classes == we could take them and use it to craft many of them and they won't interfere with each other. #while with modules, once we import them, generally there would be only one for the entire program.

Objects == Mini-Imports
	Once we instantiate(≒ create) a class, what we get is called an OBJECT.
		e.g., 
		thing = MyStuff()    #the instantiate operation. Looks like calling a function huh.
		thing.apple()
	when we call a class like a function, this is not giving us the class, but instead it is using the class as a blueprint for how to build a copy of that type of thing.
	Difference Between Classes And Objects:
		• Classes are like blueprints or definitions for creating new mini-modules.
		• Instantiation is how you make one of these mini-modules and import it at the same time.
		• The resulting created mini-module is called an object and you then assign it to a vari- able to work with it.
'''

class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
happy_bday = Song(["Happy birthday to you",
			"13324234",
			"12843994"])

bulls_on_parade = Song(["TTTTTTTTTT",
			"WWWWWWWW"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
