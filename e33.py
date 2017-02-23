i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i +1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "
for num in numbers:
	print num


#The while statement is used for repeated execution as long as an expression is true:
#while_stmt ::=  "while" expression ":" suite
#    ["else" ":" suite]

#Q1&2_Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
#A1&A2
i = 1
numbers = []
def loop(elements):
	global i
	while i < elements:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i * 3
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

print loop(27)
print "The numbers: "
for num in numbers:
	print num

#Q3&Q4_Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8, so you can change how much it increments by. Rewrite the script again to use this function to see what effect that has.
#A3&A4
number = []
def loop(num1, num2):
	while num1 < num2:
		print "Now the first num is %d." % num1
		num1 += 1
		number.append(num1)
		print "Numbers now are:", number
		print "and num1 now is: %d." % num1

loop(5, 10)


#Q5_write it to use for-loops and range instead. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
#A5_No need. Went crazy.
number = []
def forloops():
	for num in range(0, 10):
		print "First number is %d." % num
		number.append(num)
		print number
		print "Now number is %d." % num
forloops()