ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')	#Q1_What Python does ---> str.split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)	#Q1_What Python does ---> since type object 'str' has no attribute 'append', we couldn't use like "str.append(stuff, next_one)"
	print "So there's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do something with sutff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)	#Q1_What Python does ---> str.join(' ', stuff)
print '#'.join(stuff[3:5])	#Q1_What Python does ---> str.join('#', stuff[3:5])


-------------------
#Q&A below:

Q1_Take each function that is called, and go through the steps outlined above to translate them to what Python does. For example, ' '.join(things) is join(' ', things).
A1_To be precise, ''.join(things) and join('',things) are not necessarily the same. However, ''.join(things) and str.join('',things) are the same. 
''.join(things) is syntactic sugar for str.join('', things)
''.join(things) is not the only way to call this function. You can also call it using str.join('', things) because it's a method of the class str. As before, self will be '' and iterable will be things.

Q2_Translate these two ways to view the function calls. 
A2_
ten_things.split(' ') == Split ten_things with ' ' between them.
str.split('ten_things, " "') == Call split with 'ten_things' and ' '.
' '.join(stuff) == Join stuff with ' ' between them.
str.join(' ', stuff) == Call str.join with ' ' and stuff.
'#'.join(stuff[3:5]) == Join stuff with ' ' between them.
str.join('#', stuff[3:5]) == Call str.join with ' ' and stuff.

Q3_Go read about ¡°object-oriented programming¡± online.
A3_Totally confused.............

Q4_Read up on what a ¡°class¡± is in Python.
A4_A class definition is an executable statement. It first evaluates the inheritance list, if present. Each item in the inheritance list should evaluate to a class object or class type which allows subclassing. The class¡¯s suite is then executed in a new execution frame, using a newly created local namespace and the original global namespace. (Usually, the suite contains only function definitions.) When the class¡¯s suite finishes execution, its execution frame is discarded but its local namespace is saved. A class object is then created using the inheritance list for the base classes and the saved local namespace for the attribute dictionary. The class name is bound to this class object in the original local namespace.
	Programmer¡¯s note: Variables defined in the class definition are class variables; they are shared by all instances. To create instance variables, they can be set in a method with self.name = value. Both class and instance variables are accessible through the notation ¡°self.name¡±, and an instance variable hides a class variable with the same name when accessed in this way. Class variables can be used as defaults for instance variables, but using mutable values there can lead to unexpected results. For new-style classes, descriptors can be used to create instance variables with different implementation details.

Q5_What¡¯s the relationship between dir(something) and the ¡°class¡± of something?
A5_
dir([object])
	Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.
	If the object has a method named __dir__(), this method will be called and must return the list of attributes.
	The default dir() mechanism behaves differently with different types of objects, as it attempts to produce the most relevant, rather than complete, information:

	If the object is a module object, the list contains the names of the module¡¯s attributes.
	If the object is a type or class object, the list contains the names of its attributes, and recursively of the attributes of its bases.    #maybe this is the anwser?
	Otherwise, the list contains the object¡¯s attributes¡¯ names, the names of its class¡¯s attributes, and recursively of the attributes of its class¡¯s base classes.
	The resulting list is sorted alphabetically. For example:
e.g., 
	>>> import struct
	>>> dir()   # show the names in the module namespace
	['__builtins__', '__doc__', '__name__', 'struct']
	>>> dir(struct)   # show the names in the struct module
	['Struct', '__builtins__', '__doc__', '__file__', '__name__',
	 '__package__', '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
	 'unpack', 'unpack_from']
	>>> class Shape(object):
	        def __dir__(self):
	            return ['area', 'perimeter', 'location']
	>>> s = Shape()
	>>> dir(s)
	['area', 'perimeter', 'location']
