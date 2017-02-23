True and True #True
False and True #False
1 == 1 and 2 ==1 #False
"test" == "test" #True
1 == 1 or 2 != 1 #True
True and 1 == 1 #True
False and 0 != 0 #False
True or 1 ==1 #True
"test" == "testing" #False
1 != 0 and 2 == 1 #False
"test" != "testing" #True
"test" == 1 #False
not (True and False) #True
not (1 == 1 and 0 != 1) #False
not (10 == 1 or 1000 == 1000) #False
not (1 !=10 or 3 ==4) #False
not ("testing" == "testing" and "Zed" == "Cool Guy") #True
1 == 1 and not ("testing" == 1 or 1 == 0) #True
"chunky" == "bacon" and not (3 == 4 or 3 == 3) #False
3 == 3 and not ("testing" == "testing" or "Python" == "Fun") #False

#Warning: 
##NOT has first precedence, then AND, then OR

#Q1_There are a lot of operators in Python similar to != and ==. Try to find out as many “equality operators” as you can. They should be like < or <=.
#Q2_Write out the names of each of these equality operators. For example, I call != “not equal.”
#A1 & A2
##or = if there is a T, then T
##and = if there is a F, then F
##!or = if there is a T, then F
##!and = if there is a F, then T
##Assume variable a holds 10 and variable b holds 20, then −
## ==   Equal. If the values of two operands are equal, then the condition becomes true.    Example (a == b) is not true.
## !=	Not equal. Same as "<>". If values of two operands are not equal, then condition becomes true.    Example (a != b) is true.
## >	Strictly greater than. If the value of left operand is greater than the value of right operand, then condition becomes true.    Example (a > b) is not true.
## <	Strictly less than. If the value of left operand is less than the value of right operand, then condition becomes true.    Example (a < b) is true.
## >=	Greater than or equal. If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.    Example (a >= b) is not true.
## <=	Less than or equal. If the value of left operand is less than or equal to the value of right operand, then condition becomes true.    Example (a <= b) is true.

#Q3_Play with the Python by typing out new boolean operators, and before you hit Enter, try to shout out what it is. Do not think about it—just name the first thing that comes to mind. Write it down, then hit Enter, and keep track of how many you get right and wrong.
#A3_Just visit this site for testing.    http://www.mypythonquiz.com/question.php?qid=180