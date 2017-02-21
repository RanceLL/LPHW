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