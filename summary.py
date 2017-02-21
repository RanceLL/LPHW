print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
#print 'I "said" do not touch this.'

print "I could have code like this."
print "This will run."



# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.
print "I could have code like this." # and the comment after is ignored 5
# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."
print "This will run."print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2

print "What is 5 - 7", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5>= -2
print "Is it less or equal?", 5 <= -2

#How does % work?
#Another way to say it is “X divided by Y with J remaining.” For example, “100 divided by 16 with 4 remaining.” The result of % is the J part, or the remaining part.
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool tody"
print "We need to put about", average_passengers_per_car, "in each car."

i = 5+3/2.0
print i




AAAA = 'Rang. Luo'
BBB =  24
CCC = 185  / 2.5 # inches
DDD = 71 # kgs
EEE = 'Black'
GGG = 'White'
FFF = 'Black'

print "Let's talk about %s."  %AAAA
print "He's %d inches tall." % CCC
print "He's %s kgs heavy." % DDD
print "Actually that's not too heavy yah."
print "He's got %r eyes and %s hair." % (EEE, FFF)
print "His teeth are usually %s depending on the tea." % GGG

print "If I add %s, %s and %s, then I could get %s." %(BBB, CCC, DDD, BBB + CCC + DDD)
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" % hilarious

print joke_evaluation

w = "This is the left side of..."
e = "a string with a right side."

print w + e

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % ("A", "B", "C", "D")
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."



# Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. That's why the last line of output uses both single-quotes and double-quotes for indi- vidual pieces
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4lines if we want, or 5, or 6.
"""
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat fod
\t* Fishies
\t* Catnip\n\t%s.* Grass
""" % 'asaaaa'



print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?"
weight = raw_input('Please type your data here ---->  ')

print "So, you're %r old, %s tall and %r heavy." % (age, height, weight)



age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)
from sys import argv

Alice= raw_input("What do you want to call your first variable? "),
Black = raw_input("What do you want to call your 2nd variable? "),
Carl = raw_input("What do you want to call your 3rd variable? "),

script, Alice, Black, Carl = argv

print "The script is called:", script
print "Your first variable is:", Alice
print "Your second variable is:", Black
print "Then, your third variable is:", Carl

test1 = raw_input('Alice')
print test1
print Alice
from sys import argv

script, user_name, title = argv
prompt = 'Please input your data, thank you!  >'

print "Hi %s the %s, I'm the %s script." % (user_name, title, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s with the title of %s?" % (user_name, title)
likes = raw_input(prompt)

print "Where do you live, %s?" % user_name
location = raw_input(prompt)

print "What kind of computer do you have, %s?" % user_name
pc = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Great.
""" % (likes, location, pc)
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">>>")

txt_again = open(file_again)

print txt_again.read()

#Other approaches:
##print "Type the filename :"
##txt= open(raw_input(">>>"))
##print txt.read()
#Or
##print "Type the filename :"
##print open(raw_input(">>>")).read()

#Q. Start python again and use open from the prompt. Notice how you can open files and run read on them right there?
##print open("e17.py").read()
#OR
##$ python 
##>>> xyz = open ("ex16.py")
##>>> print xyz.read()
##>>> xyz.close()


from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL+C (^C) or CMD+C (%s C)." % u'\u2318'
#I exchanged the Ctrl and Command key of MacOS, so that for me, I need to print sigh of the "Command key" when I'm using MacOS. 
#That's a trick, well... I just want to know how to print Cmd sigh... It's okay for you to delete "or CMD+C (%s C)" of course.

print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
 
print "I'm going to write these to the file."
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it."
target.close()


#I exchanged the Ctrl and Command key of MacOS, so that for me, I need to print sigh of the "Command key" when I'm using MacOS.
##print "If you don't want that, hit CTRL+C (^C) or CMD+C (%s C)." % u'\u2318'
#make sure you just put a 'blank' between "%s" and "C". This is so that characters don't overlap each other.

#Q2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
##from sys import argv
##script, A1 = argv
##print open(A1).read()

#Q3. There’s too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
##target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#Q4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly say you want to write a file.
## 'w' for writing (truncating the file if it already exists)

#Q5. If you open the file with 'w' mode, then do you really need the target.truncate()? Go read the docs for Python’s open function and see if that’s true.
#That's TRUE.
#We could also
##raw_input("?")
##print """Opening the file...
##.............
##.............
##.............
##"""
##target = open(filename, 'w')
##print "Truncating the file. Goodbye!"


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? \n...\nOkay, that's %s" % exists(to_file)

print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input(">>>")

open(to_file, 'w').write(indata)

print "Alright, all done."


#Q2. This script is really annoying. There’s no need to ask you before doing the copy, and it prints too much out to the screen. Try to make it more friendly to use by removing features.
##Let's make this script EVEN MORE ANNOYING!!!!!!!!!

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Now, we are going to test if the files really exist. Hit RETURN to continue\n..."
raw_input(">>>")

print "Okay, that's %s" % str(exists(to_file)).upper()

#Create a file to test the "exists" function.
##from os.path import exists
##a = exists("e19.py")
##print a
#"True" or "False" is not enough at all, what we need is TRUE or FALSE to get the attention of users.

print "Ready to copy? \nHit RETURN to continue, CTRL-C to abort."
raw_input(">>>")

open(to_file, 'w').write(indata)
print "Alright, all done."

#Anwser for Q2
from sys import argv; from os.path import exists; script, from_file, to_file = argv; open(to_file, 'w').write(open(from_file).read())

#Q6. Find out why you had to do output.close() in the code.
##1. if your program does something else for a while, or repeats this sequence of steps dozens of times, you could run out of resources, or overwrite something.
##2. Second, some operating system platforms won't let the same file be simultaneously open for readonly and for write.  So if the two filenames happened to be the same file (through symlink or other mechanism, or even using two different ways to describe the same file), you might get an error trying to write without having closed the input file.

def print_two(*args):
#The sigh of * means there are tons of args here need to be unpacked later
     arg1, arg2 = args
#Unpacking args.
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

#Try to build a function!
A = raw_input("Let's input some numbers >>> ")

def C_I2C(A):
	C = int(A) * 2.5
	print "So,%s inches equal %s cms" % (A, C)
print C_I2C(A)

#It will be also OK.
def C_I2C(A):
	C = int(A) * 2.5
	return "So,%s inches equal %s cms" % (A, C)
    ##To avoid getting 'None' in the output, use Return in stead of print here.
A = raw_input("Let's input some numbers >>> ")
    ##In stead of place this sentence in in the head of script.
print C_I2C(A)




def cheese_and_crackers(cheese_count, boxes_of_crackers):
#those variables are separate and live outside the function. 
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!\nGet a blanker.\n"
	return
#Not pretty know but, think better add a RETURN here.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#If you can use = to name something, you can usually pass it to a function as an argument.
##Find some connection between two or more argument and translate it into code, then pass it to a function.

#Q3. Write at least one more function of your own design, and run it 10 different ways.
##A3.
def AAA(m, cm):
	print "Here u are %sm tall.\n OR in %scms." % (m, cm)
	return
AAA(1.85, 185)		#1

m = raw_input("So how tall are your brother?>>>")
cm = float(m) * 100
AAA(m, cm)			#2

AAA(1 + 1, 100 + 100)		#3

a = 1
b = 100
AAA(float(m) + a, cm + b)	#4

AAA(float(m) + 0.1, cm + 10)	#5

def passValue():         		#6
  x1 = 100 
  x2 = 200
  displaySum(x1,x2)

for i in range(10):
  AAA(i, int(i) * 100)		#7~16from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)
#moving to the start of the file.

def print_a_line(line_count, f):
	print line_count, f.readline(),
#The readline() function returns the \n that’s in the file at the end of that line. To change this behavior simply add a , (comma) at the end of print so that it doesn’t print its own \n.

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#Q4. Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there.
#A4. 
##fileObject.seek(offset[, whence])
##fileObject is the file pointer you're working with;  ###not quite sure what's this sentence mean.
##offset means how many positions you will move
##whence -- This is optional and defaults to 
###0 which means absolute file positioning,
###1 which means seek relative to the current position,
###2 means seek relative to the file's end.

#When you open a file, the system points to the beginning of the file. Any read or write you do will happen from the beginning. A seek() operation moves that pointer to some other part of the file so you can read or write at that place.
##So, if you want to read the whole file but skip the first 20 bytes, open the file, seek(20) to move to where you want to start reading, then continue with reading the file.
##Or say you want to read every 10th byte, you could write a loop that does seek(9, 1) (moves 9 bytes forward relative to the current positions), reads one byte, repeat.


#Q5. Research the shorthand notation += and rewrite the script to use that.
#A5. 
##print "Let's print three lines:"
##current_line = 1
##print_a_line(current_line, current_file)
##current_line += 1
##print_a_line(current_line, current_file)
##current_line += 1
##print_a_line(current_line, current_file)
#a = a + b is the same as a += b
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
#Why "return"?
##1. Our function is called with two arguments: a and b.
##2. We print out what our function is doing, in this case ADDING.
##3. Then we tell Python to do something kind of backward: we return the addition of a + b. You might say this as, "I add a and b, then return them."
##4. Python adds the two numbers. Then when the function ends, any line that runs it will be able to assign this a + b result to a variable.

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(43, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#Q4. Finally, do the inverse. Write out a simple formula and use the functions in the same way to calculate it.
#A4. a1 = divide(iq, 2)
#b1 = multiply(weight, a1)
#c1 = subtract(height, b1)
#print d1