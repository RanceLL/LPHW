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
