def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

start_point = 10000
aaa, bbb, ccc = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (aaa, bbb, ccc)
