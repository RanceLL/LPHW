#Differences between list and dict:
#1) We can only use numbers to get items out of a list, while when it comes to DICT, we could use anything, not just numbers, to get items out of a list.
#2) A list is for an ordered list of items. A dictionary (or dict) is for matching some items (called “keys”) to other items (called “values”).

#stuff = {'name': 'rang', 2: 25, 'height': 185}
#print stuff
#print stuff[2]    #Notice that 2 here means the 'name', not the number of the object in DICT. As dicts don't have order, we can not look them up by a numeric index.


###WARNING
#Correction: in P133, the [ ] after the the "state =" in line 2 of the codes should be {}, so does the "cities = { }" 

states = {
	'Oregon': 'OR', 
	'Florida': 'FL', 
	'California': 'CA', 
	'New York': 'NY', 
	'Michigan': 'MI'
}


cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'Ney York'
cities['OR'] = 'Portland'	

print '*' * 10
print "NY state has %s" % cities['NY']
print "OR state has %s" % cities['OR']

print '*' * 10
print "Michigan's abbreviation is : ", states['Michigan']
print "Florida's abbreviation is : ", states['Florida']

print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-' * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s." % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s." % (abbrev, city)

print '_' * 10
for state, abbrev in states.items():    #state, abbrev doesn't mean anything, just a varible like i.
	print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '_' * 10
state = states.get('Texas', None)    #Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.

if not state:
	print "Sorry, no Texas."

city = cities.get('TX', 'Does not Exits')
print "The city for the state 'TX' is: %s" % city


--------------------------------------

Q3_Find out what you can’t do with dictionaries. A big limitation is that they do not have order, so try playing with that.
A3_class collections.OrderedDict([items])
Ordered dictionaries are just like regular dictionaries but they remember the order that items were inserted. When iterating over an ordered dictionary, the items are returned in the order their keys were first added.
Return an instance of a dict subclass, supporting the usual dict methods. An OrderedDict is a dict that remembers the order that keys were first inserted. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.

Q1_Do this same kind of mapping with cities and states/regions in your country or in some other country.
A1_
states = {
    'Hunan': 'HN',
    'Fujian': 'FJ',
    'Jiangsu': 'JS',
    'Heilongjiang': 'HLJ'
}

cities = {
    'HN': 'Changsha',
    'FJ': 'Fuzhou'
}

cities['HLJ'] = 'Harbing'
cities['JS'] = 'Nanjing'

print '-' * 10
print "HN province has %s." % cities['HN']
print "HLJ province has %s." % cities['HLJ']

print '-' * 10
print "Jiangsu's abbr is %s." % states['Jiangsu']
print "Fujian's abbr is %s." % states['Fujian']

print '-' * 10
print "Hunan has %s." % cities[states['Hunan']]
print "Fujian has %s." % cities[states['Fujian']]

print '-' * 10
for state, abbrev in states.items():
    print "%s's abbr is %s." % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s." % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Hebei', 'HB')

if not state:
    print "Sorry, there is no Hebei."
else:
    print state

city = cities.get('HB', 'Shijiazhuang')
print "HB province has %s." % city


