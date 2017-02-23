def break_words(stuff):
	words = stuff.split(' ')
	return words
#str.split([sep[, maxsplit]])
#'1<>2<>3'.split('<>') returns ['1', '2', '3']
def sort_words(words):
	return sorted(words)
#sorted(iterable[, cmp[, key[, reverse]]])
#Return a new sorted list from the items in iterable.

def print_first_word(words):
	word = words.pop(0)
	print word
#pop(key[, default])
#If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.

def print_last_word(words):
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


#1_Also works.  ---->
#Create a file named test.py with codes below and run it like "python text.py"
import e25
sentence = "All good things come to those who wait."
words = e25.break_words(sentence)
print words
#unlike modules we imported, we can't directly use "break_words(sentence)"
#remember "from sys import argv"? As far as I guess, "e25" = "sys" here which contains bundles of methods such as "break_words" or "argv".------------Maybe I'm WRONG : \
##According to SD3, it's right!


#2_As I guess, we can't call functions ending with "return" directly without "e25." been typed at first. But it's OKAY to call those functions ending with "print". e.g. 
#sort_words(aaa)  ------>  WRONG
#print_last_word(aaa)  ------>   RIGHT
#Maybe the reasong: functions ending with "print" are global names, unlike those ending with "return" which are local names.------------Maybe I'm WRONG : \

##YEP, it works! Print command lines in python mode and we could find:
##"help(Global_Funtions_Ending_With_Print"  -------->    OK
##"help(Local_Functions_Ending_With_Return"  -------->    ERROR    #Must "help(e25.Local_Functions_Ending_With_Return"

#2.1_GOT A QUESTION
#help(print_first_and_last)  -------->    It works but seems like this function with "break_words()", which is a local name, inside.


#3_Difference between PRINT and RETURN?
#Return gives something back or replies to the caller of the function, while print produces text only.
#Think of that PRINT makes your function write some text out to the user but it causes a side-effect which is it can't be used by another function. While RETURN could.

##The Point. 
###Return is not a function. It is a control flow construct (like if else constructs). It is what lets you "take data with you between function calls".
##Break Down.
###print: gives the value to the user as an output string. print(3) would give a string '3' to the screen for the user to view. The program would lose the value.
###return: gives the value to the program. Callers of the function then have the actual data and data type (bool, int, etc...) return 3 would have the value 3 put in place of where the function was called.
##Example
def ret(n):
    return n
def pri(n):
    print(n)
4 + ret(3) # ret(3) is replaced with the number 3 when the function ret returns
>>> 7
4 + pri(3) # pri(3) prints 3 and implicitly returns None which can't be added
>>> 3
>>> TypeError cannot add int and NoneType