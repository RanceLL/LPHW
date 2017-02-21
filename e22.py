Q1:Go back through every exercise you have done so far and write down every word and symbol (another name for “character”) that you have used. Make sure your list of symbols is complete.
A1.
First, go merge your files from ex1 to ex21.

filenames = ['e1.py', 'e2.py','e3.py','e4.py','e5.py','e6.py','e7.py','e8.py','e9.py','e10.py','e11.py','e12.py','e13.py','e14.py','e15.py','e16.py','e17.py','e18.py','e19.py','e20.py','e21.py']
with open('summary.py', 'w') as outfile:
	for fname in filenames:
		with open(fname) as infile:
			outfile.write(infile.read())

Second, read "summary.py" and try to create a list / table.

#HERE is the table.

#Approaches To Solve Errors
pydoc = Check documentation from python modules.
Google
	stack overflow
	quora
Dash

#General
Variable = Temporarily stores data and given a name.
Functions = Packages of scripts created by yourself.
	#e.g. def AAA(a,b,c):
Modules = Packages of scipts created by others.
	#from XXX import YYY
Methods = Functions belong to a class. (SPECIALIZED functions).
	#Difference between M & F:
	#Methods are functions that belong to a class, functions can be on any other scope of the code so you could state that all methods are functions, but not all functions are methods.
Arguments = variable values provided by users.
Return = Value that a function call evaluates to.
Parameter = A variable that an argument is stored in when a function is called.
prompt = a character or string that the user can specify to ask for info from the user

#Functions and Methods
int() = Convert data into whole numbers.
float() = Convert data into decimals.
str() = Convert data into text.
len() = Count the length of a string.
raw_input() = Get user input.
print = Output result of expression.
open() = Open an external file. 
	r = Default mode. Open with Reading only mode. Position of stream : BIGINNING.
	r+ = Open with reading and writing mode. Position of stream : BIGINNING.
	w = Truncate or create files for writing. Position of stream : BIGINNING.
	w+ = Create a new file and open it with reading and writing mode. Position of stream : BIGINNING.
	a = Open(or create, if not exists) with writing mode. Position of stream : Ending.
	a+ = Open(or create, if not exists) with reading and writing mode. Position of stream : Ending.
	#e.g. open(filename, 'a+')
.read() = Read the contents of the file.		fileObject.read()
	#e.g. open(filename).read()
.readline() = Read one line of the file.		fileObject.readline()
	#e.g. open(filename).readline()
.write() = Write a string to the file.		fileObject.write()
	#e.g. open(filename).write('BLANK')
.truncate() = delete contents of a file.		fileObject.truncate()
	#e.g. open(filename).truncate()
.seek() = Set the current position in the file.	fileObject.seek(offset[, whence])
	#e.g. open(filename).seek(offset[, whence])
	#seek(0) = absolute file positioning, beginning of the file ; seek(1) = seek relative to the current position; seek(2) = seek relative to the file's end.
.close() = Close the file.
	#Why u should close the file.
	#1. if your program does something else for a while, or repeats this sequence of steps dozens of times, you could run out of resources, or overwrite something. 2. Second, some operating system platforms won't let the same file be simultaneously open for readonly and for write.  So if the two filenames happened to be the same file (through symlink or other mechanism, or even using two different ways to describe the same file), you might get an error trying to write without having closed the input file.
exist = Checks if a file exists. Returns True or False.
argv = Module that enables scripts to accept command line arguments.
	#to get info before running scripts. BTW, raw_input() enables scripts to get info during scripts' running.
	packing/unpacking values = to get info out of a argv
	*args = refers to a list of arguments in a function (better to just list the arguments next to the function name).

#Math Operators And Symbols
triple quotes '''	= Span the string across multiple lines
# = A hash sign (#/ octothrope) that is not inside a string literal begins a comment. All characters after the # and up to the physical line end are part of the comment, and the Python interpreter ignores them. Could be on the same line after a statement or expression
"+" & "-" & "*" & "/" & "<=>="   #ellipsis
"%" = Caculate remainder after division.
"+=" = Shortcut for "plus itself". Also "-=", "*=", etc. #e.g. x = x + y    OR    x+=y
"==" = Equal
"=" = ASSIGN value on the right to variable on the left.
True & False = Boolean test for truth values.

#Format and Escape Characters
%d =  A placeholder for a number
%s = A placeholder for a string
%r = A  placeholder for a raw data
\n = New line
\t = Tab
\\ = Escapes a backslash


