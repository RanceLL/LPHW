from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input(">>>")

txt_again = open(file_again)

print txt_again.read()

#Also
#print "Type the filename :"
#txt_again = open(raw_input(">>>"))
#print txt_again.read()