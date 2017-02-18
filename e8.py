formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % ("A", "B", "C", "D")
print formatter % (formatter, formatter, formatter, formatter)
print formatter %(
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."



# Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. That's why the last line of output uses both single-quotes and double-quotes for indi- vidual pieces
# 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'