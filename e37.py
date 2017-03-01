Del, 
del_stmt ::=  "del" target_list

As, 
used as an assignment operator for various builtin types.
#Using
1. Context managers:
	with ContextManager as instance:
2. Import statements:
	import foo as bar
3. Exceptions:
	catch Exception as exc:
	e.g.,
	instead of 
		f = open(file)
		f.read()
		f.close 
	you can write
		with open(file) as f:	#by using with statement, u have no need to "f.close()"
		    f.read()

	instead of
		import SomeBigModuleName
		SomeBigModuleName.method()
	you can write 
		import SomeBigModuleName  as sbmn
		sbmn.method()


Global, global_stmt ::=  "global" identifier ("," identifier)*
#The global statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without global, although free variables may refer to globals without being declared global.
#Names listed in a global statement must not be used in the same code block textually preceding that global statement.
#Names listed in a global statement must not be defined as formal parameters or in a for loop control target, class definition, function definition, or import statement.
#The global statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals.

With, 
with_stmt ::=  "with" with_item ("," with_item)* ":" suite
with_item ::=  expression ["as" target]
#In python the with keyword is used when working with unmanaged resources (like file streams). It is similar to the USING statement in VB.NET and C"#". It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown. It provides 'syntactic sugar' for "try/finally" blocks.
#A context manager is an object that defines the runtime context to be established when executing a with statement. The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code. Context managers are normally invoked using the with statement, but can also be used by directly invoking their methods.
#Typical uses of context managers include saving and restoring various kinds of global state, locking and unlocking resources, closing opened files, etc.
#object.__enter__(self)	Enter the runtime context related to this object. The with statement will bind this method’s return value to the target(s) specified in the as clause of the statement, if any.
#object.__exit__(self, exc_type, exc_value, traceback)	Exit the runtime context related to this object. The parameters describe the exception that caused the context to be exited. If the context was exited without an exception, all three arguments will be None.

Assert, 
can better be described as being equivalent to
	if __debug__:
		if not expression: raise AssertionError 
	OR
	if not condition:
		raise AssertionError()

Iteration, 
Reading items of a list one by one is called iteration
Iterators, 
1. An object can be iterated over with "for" if it implements
   __iter__() or __getitem__().

2. An object can function as an iterator if it implements next().

Generators,
Generators are iterators, but you can only iterate over them once. It's because they do not store all the values in memory, they generate the values on the fly.

Yield, 
is a keyword that is used like return, except the function will return a generator, which will only be read once.
★ when you call the function, the code you have written in the function body does not run. The function only returns the generator object, then, your code will be run each time the for uses the generator. 

Try, Except and Finally
	try_stmt  ::=  try1_stmt | try2_stmt
	try1_stmt ::=  "try" ":" suite
	               ("except" [expression [("as" | ",") identifier]] ":" suite)+
	               ["else" ":" suite]
	               ["finally" ":" suite]
	try2_stmt ::=  "try" ":" suite
	               "finally" ":" suite
If an error is encountered, a try block code execution is stopped and transferred
down to the except block. 
In addition to using an except block after the try block, you can also use the
finally block. 
The code in the finally block will be executed regardless of whether an exception
occurs. (finally is for defining "clean up actions". The finally clause is executed in any event before leaving the try statement, whether an exception (even if you do not handle it) has occurred or not.)
e.g., 
	try:
	    print "Hello World"
	except IOError:
	    print('An error occured trying to read the file.')
You can use finally to make sure files or resources are closed or released regardless of whether an exception occurs, even if you don't catch the exception. (Or if you don't catch that specific exception.)
eg. 
	try:
	    run_code1()
	except TypeError:
	    run_code2()
	    return None   # The finally block is run before the method returns
	finally:
	    other_code()
	Compare to this:
	try:
	    run_code1()
	except TypeError:
	    run_code2()
	    return None   
	other_code()  # This doesn't get run if there's an exception.

Exec, 
exec_stmt ::=  "exec" or_expr ["in" expression ["," expression]]
This statement supports dynamic execution of Python code. The first expression should evaluate to either 
	*a Unicode string, 
	*a Latin-1 encoded string, 
	*an open file object, 
	*a code object, 
	*a tuple. 
If it is a string, the string is parsed as a suite of Python statements which is then executed (unless a syntax error occurs). 
If it is an open file, the file is parsed until EOF and executed. 
If it is a code object, it is simply executed. 
In all cases, the code that’s executed is expected to be valid as file input. Be aware that the return and yield statements may not be used outside of function definitions even within the context of code passed to the exec statement.

Raise
raise_stmt ::=  "raise" [expression ["," expression ["," expression]]]
If no expressions are present, raise re-raises the last exception that was active in the current scope. If no exception is active in the current scope, a TypeError exception is raised indicating that this is an error (if running under IDLE, a Queue.Empty exception is raised instead).
Otherwise, raise evaluates the expressions to get three objects, using None as the value of omitted expressions. The first two objects are used to determine the type and value of the exception.

Continue
continue_stmt ::=  "continue"
continue may only occur syntactically nested in a for or while loop, but not nested in a function or class definition or finally clause within that loop. It continues with the next cycle of the nearest enclosing loop.
When continue passes control out of a try statement with a finally clause, that finally clause is executed before really starting the next loop cycle.
e.g., 
	for x in range(5):
	    if x == 3:
	        continue
	    print(x)
	#result.
	0
	1
	2
	4

Break, 
break_stmt ::=  "break"
break may only occur syntactically nested in a for or while loop, but not nested in a function or class definition within that loop.
It terminates the nearest enclosing loop, skipping the optional else clause if the loop has one
e.g., 
	for x in range(5):
	    if x == 3:
	        break
	    print(x)
	#result.
	0
	1
	2

Is, 
"==" is for value equality. Use it when you would like to know if two objects have the same value.
"is" is for reference equality. Use it when you would like to know if two references refer to the same object.
The "is" operator test, just tests if two variables POINT the same object, not if two variables have the same value.

Lambda
Small anonymous functions can be created with the lambda keyword. This function returns the sum of its two arguments: 
	lambda a, b: a+b. 
	lambda is just a fancy way of saying function.
	Lambda functions can be used wherever function objects are required. Lambda functions can reference variables from the containing scope:
	>>> def make_incrementor(n):
	...     return lambda x: x + n
	...
	>>> f = make_incrementor(42)
	>>> f(0)
	42
	>>> f(1)
	43
The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:
	>>>
	>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
	>>> pairs.sort(key=lambda pair: pair[1])
	>>> pairs
	[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

"""\\	Backslash (\)	 
\'	Single quote (')	 
\"	Double quote (")	 
\a	ASCII Bell (BEL)	 
\b	ASCII Backspace (BS)	 
\f	ASCII Formfeed (FF)	 
\n	ASCII Linefeed (LF)	 
\r	ASCII Carriage Return (CR)	 
\t	ASCII Horizontal Tab (TAB)	 
\uxxxx	Character with 16-bit hex value xxxx (Unicode only)	(1)
\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)	(2)
\v	ASCII Vertical Tab (VT)	 
\ooo	Character with octal value ooo	(3,5)
\xhh	Character with hex value hh
"""

%s	String format. This is the default type for strings and may be omitted.
%None	The same as 's'.
%b	Binary format. Outputs the number in base 2.
%c	Character. Converts the integer to the corresponding unicode character before printing.
%d	Decimal Integer. Outputs the number in base 10.
%i	Integer. 100% Same as %d.
%o	Octal format. Outputs the number in base 8.
%x	Hex format. Outputs the number in base 16, using lower- case letters for the digits above 9.
%X	Hex format. Outputs the number in base 16, using upper- case letters for the digits above 9.
%n	Number. This is the same as 'd', except that it uses the current locale setting to insert the appropriate number separator characters.
%e	Exponent notation. Prints the number in scientific notation using the letter ‘e’ to indicate the exponent. The default precision is 6.
%E	Exponent notation. Same as 'e' except it uses an upper case ‘E’ as the separator character.
%f	Fixed point. Displays the number as a fixed-point number. The default precision is 6.
%F	Fixed point. Same as 'f'.
%g	General format. For a given precision p >= 1, this rounds the number to p significant digits and then formats the result in either fixed-point format or in scientific notation, depending on its magnitude.
	A precision of 0 is treated as equivalent to a precision of 1. The default precision is 6.
%G	General format. Same as 'g' except switches to 'E' if the number gets too large. The representations of infinity and NaN are uppercased, too.
%n	Number. This is the same as 'g', except that it uses the current locale setting to insert the appropriate number separator characters.
%%	Percentage. Multiplies the number by 100 and displays in fixed ('f') format, followed by a percent sign.

%u 	Unsigned integer



a + b		Addition		add(a, b)
seq1 + seq2	Concatenation		concat(seq1, seq2)
obj in seq	Containment Test	contains(seq, obj)
a / b		Division		div(a, b) (without __future__.division)
a / b		Division		truediv(a, b) (with __future__.division)
a // b		Division		floordiv(a, b)
a & b		Bitwise And		and_(a, b)
a ^ b		Bitwise Exclusive Or	xor(a, b)
~ a		Bitwise Inversion	invert(a)
a | b		Bitwise Or		or_(a, b)
a ** b		Exponentiation		pow(a, b)
a is b		Identity			is_(a, b)
a is not b	Identity			is_not(a, b)
obj[k] = v	Indexed Assignment	setitem(obj, k, v)
del obj[k]	Indexed Deletion	delitem(obj, k)
obj[k]		Indexing		getitem(obj, k)
a << b		Left Shift		lshift(a, b)
a % b		Modulo			mod(a, b)
a * b		Multiplication		mul(a, b)
- a		Negation (Arithmetic)	neg(a)
not a		Negation (Logical)	not_(a)
+ a		Positive		pos(a)
a >> b		Right Shift		rshift(a, b)
seq * i		Sequence Repetition	repeat(seq, i)
seq[i:j] = values	Slice Assignment	setitem(seq, slice(i, j), values)
del seq[i:j]		Slice Deletion		delitem(seq, slice(i, j))
seq[i:j]		Slicing			getitem(seq, slice(i, j))
s % obj		String Formatting	mod(s, obj)
a - b		Subtraction		sub(a, b)
obj		Truth Test		truth(obj)
a < b		Ordering		lt(a, b)
a <= b		Ordering		le(a, b)
a == b		Equality		eq(a, b)
a != b		Difference		ne(a, b)
a >= b		Ordering		ge(a, b)
a > b		Ordering		gt(a, b)