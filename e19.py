def cheese_and_crackers(cheese_count, boxes_of_crackers):
#those variables are separate and live outside the function. 
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!\nGet a blanker.\n"
	return
#Not pretty know but, think better add a RETURN here.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#If you can use = to name something, you can usually pass it to a function as an argument.
##Find some connection between two or more argument and translate it into code, then pass it to a function.

#Q3. Write at least one more function of your own design, and run it 10 different ways.
##A3.
def AAA(m, cm):
	print "Here u are %sm tall.\n OR in %scms." % (m, cm)
	return
AAA(1.85, 185)		#1

m = raw_input("So how tall are your brother?>>>")
cm = float(m) * 100
AAA(m, cm)			#2

AAA(1 + 1, 100 + 100)		#3

a = 1
b = 100
AAA(float(m) + a, cm + b)	#4

AAA(float(m) + 0.1, cm + 10)	#5

def passValue():         		#6
  x1 = 100 
  x2 = 200
  displaySum(x1,x2)

for i in range(10):
  AAA(i, int(i) * 100)		#7~16