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




