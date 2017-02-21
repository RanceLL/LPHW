from sys import argv

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
