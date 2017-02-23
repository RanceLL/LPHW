people = 20 
cats = 30
dogs = 20   

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs"

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."


#Q1_What do you think the if does to the code under it?
#A1_The if statement is used for conditional execution:
#if_stmt ::=  "if" expression ":" suite
#             ( "elif" expression ":" suite )*
#             ["else" ":" suite]
#It selects exactly one of the suites by evaluating the expressions one by one until one is found to be true (see section Boolean operations for the definition of true and false); then that suite is executed (and no other part of the if statement is executed or evaluated). If all expressions are false, the suite of the else clause, if present, is executed.
#An if-statement creates what is called a “branch” in the code. The if-statement tells your script, “If this boolean expression is True, then run the code under it, otherwise skip it.

#Q2_Why does the code under the if need to be indented four spaces?
#A2_It's a part of conditional execution. A colon at the end of a line is how you tell Python you are going to create a new “block” of code, and then indenting four spaces tells Python what lines of code are in that block. This is exactly the same thing you did when you made functions in the first half of the book.

#Q3_What happens if it isn’t indented?
#A4_If it isn’t indented, you will most likely create a Python error. Python expects you to indent something after you end a line with a : (colon).

#Q4_Can you put other boolean expressions from Exercise 27 in the if-statement?
#A4_Yes.

#Q5_What happens if you change the initial values for people, cats, and dogs?
#A5_Because you are comparing numbers, if you change the numbers, different if-statements will evaluate to True, and the blocks of code under them will run.