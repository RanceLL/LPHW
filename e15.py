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


