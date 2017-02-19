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

