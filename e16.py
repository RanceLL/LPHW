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


