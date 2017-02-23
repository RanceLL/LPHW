people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
#Q_What happens if multiple elif blocks are True?
#A_Python starts at the top and runs the first block that is True, so it will run only the first one.
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "fine, let's stay home then."

#Q1_Try to guess what elif and else are doing.
#A1_if_stmt ::=  "if" expression ":" suite
#             ( "elif" expression ":" suite )*
#             ["else" ":" suite]

