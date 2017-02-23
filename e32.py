the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

for i in change:
	print "I got %r" % i

elements = []
#build an empty list.

for i in range(0, 6):
#The range() function only does numbers from the first to the last, NOT INCLUDING THE LAST.
	print "Adding %d to the list." % i
	elements.append(i)

for i in elements:
	print "Element was: %d" % i


#Q1_Look up the range function to understand it.
#A1_
#range(stop)
#range(start, stop[, step])
#This is a versatile function to create lists containing arithmetic progressions.
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(0, 30, 5)
[0, 5, 10, 15, 20, 25]
>>> range(0)
[]
>>> range(1, 0)
[]
#If there're only two number in in range(), they could only be range(start, stop). impossible to be like range(stop, step)

#Q2_Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6)directly to elements?
#A2_It's OK.
#counts = range (0, 10)
#print counts

#Q3_Find the Python documentation on lists and read about them. What other operations can you do to lists besides append?
#A3_
##class list([iterable])
##Return a list whose items are the same and in the same order as iterable‘s items. iterable may be either a sequence, a container that supports iteration, or an iterator object. If iterable is already a list, a copy is made and returned, similar to iterable[:]. For instance, list('abc') returns ['a', 'b', 'c'] and list( (1, 2, 3) ) returns [1, 2, 3]. If no argument is given, returns a new empty list, [].
##list is a mutable sequence type, as documented in Sequence Types —
##In Python, arrays and lists are referred to as lists. Just call these lists for now.

#Q4_What does elements.append() do? Any time you run into things like this, always try to play with them interactively in the Python shell.
#A4_
list_a = []
for i in range(66, 666, 6):
	list_a.append(i)
print list_a