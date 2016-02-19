# A Python Book: Beginning Python, Advanced Python, and Python Exercises
# Dave Kuhlman
# 1/11/2016

# ****************************************
# 
# Working with lists
# Page 1 - 23
#
# - len
# - in, not in, is, is not, and, or
# - append
# - insert
# - extend
# - pop
# - remove
# - delete
# ****************************************
import string
import types
import re

print "\n \n \n LISTS \n \n \n"

data = [1, 11, 111, 1111, 11111]

# provides the length of the list
print len(data)
# provides if the value is in the data set
print 12 in data
# provides the data list after the cut.
# The list will start at the beginning value and end at the second value.
print data[2:4]
# adding to the end of a list
data.append(111111)
print data
# what if we want to insert at the beginning of a list? We need to use insert.
# This actually lets us insert at any point of the list
val = 0
data.insert(0, val)
print data
# adding a list to the existing list
extra = [1111111, 11111111, 111111111]
data.extend(extra)
print data
# removing a value from the end of a list 
data.pop()
# remove item from a list. Its important to check if the item exists in the list using "in" first before
# performing this action
data.remove(11111111)
print data
# What if we want to remove a data point at a specific index? We use delete
del data[0]
print data

x = 0

if not(x):
	print "True"

# ****************************************
#
# Working with Strings
# pages 24 - 29
#
#
# String formatting
# unicode formatting
# string.format
#
# ****************************************

print "\n \n \n STRINGS \n \n \n"

name = 'dave'
size = 25
factor = 3.45

# rather than putting the name of the object or the variables you place it outside the string

print 'Name: %s Size: %d Factor %3.4f' % (name, size, factor,)

print 'Name: %s Size: %d Factor %12.6f' % (name, size, factor,)

values = {'fruit': 'banana', 'vegetable':'potato'}

print 'I love %(fruit)s and I also love %(vegetable)s' % values

# when wanting to create a separated array based on a value
content = []
content.append('finch')
content.append('sparrow')
content.append('thrush')
content.append('jay')
contentstr = ':'.join(content)
contentcommastr = ", ".join(content)

print contentstr
print contentcommastr

# when you know the length of the array

first = "Dave"
last = "Kuhlman"
other_first = "Johnathon"
other_last = "Druery"
full = '%s, %s, %s, %s, ' % (last, first, other_last, other_first, )

print full 

# using make trans we can replace specified characters from a string if it exists

def test():
	a = 'axbycz'
	t = string.maketrans('iii', '123')
	print a
	print a.translate(t)

test()

# the new way to format strings
# this is important and cleaner. It'll make it easier rather than splitting the string and adding in variables

print 'n1: {num1} and n2: {num2}'.format(num1 = 5, num2 = 10)

# also for dictionaries as well it'll work

values = {'first': 5, 'second': 10}
print 'this string will show {first} and {second}'.format(**values)

# understanding unicode.

# an international encoding standard for use with different languages and scripts, by which each letter, digit, 
# or symbol is assigned a unique numeric value that applies across different platforms and programs.
# when generating a file make sure to have it with a specific ending for the encoding you want like 'utf-8'

a = u'abcd'
b = unicode('efgh')
print a, b

a.decode('utf-8')
print a

c = u'abcd'
c = c.decode('utf-8')
print type(c) is types.UnicodeType

# ****************************************
#
# Dictionaries
# pages 29 - 32
#
# keys()							gives you the keys for the dictionary
# values()							gives you the values for the keys that exist in the dict
# items()							gives you an array of tuples for the values that exist. You can dive into these, its essentially an array in an array.
# has_key(key_your_looking_for)		this lets you know if the key exists
# get(key_your_looking_for, -1)		the proper way of using has_key is really to use a get
# setdefault 						allows you to check if a value exists, if it doesnt then we can set the value with whatever we want
#
# ****************************************


print "\n \n \n DICTIONARIES \n \n \n"

d = {'aa' : 11, 'bb': 22}

print d.keys()

print d.values()

print d.items()

print d.items()[0][0]

print d.get('aa', -1)

if d.get('cc') is None:
	print 'missing'

if 'aa' in d:
	print 'aa is there'

testing_dict = {}
testing_dict['a'] = 1
print testing_dict

testing_dict.setdefault('c',"test")
print testing_dict

# ****************************************
#
# Files
# pages 32 - 35
#
# open								when using this and writing it'll create the file in the current directory where the python file is
# append 							you can append as well
# read 								read a file
# readlines()						this is a method for reading all of the lines in a file using "r" (line 255)
#
# the cool thing to note here is that you can do combinations to read and write to a new file which is probably a better practice than
# overwriting what exists in a file
#
# ****************************************

print "\n \n \n FILES \n \n \n"

def replace(line):
	replaced_line = re.sub(r"m", "poop", line)
	return replaced_line

write_log = open('mylog.txt', 'w')
write_log.write('message #1 \n')
write_log.close()

read_log = file('mylog.txt', 'r')
for line in read_log:
	print re.sub(r"\s", 'p', line)
	print line
read_log.close()

with file("mylog.txt", "a") as myfile:
	myfile.write("appended text")

with file('mylog.txt', 'r') as readfile:
	with file('mylog2.txt', 'w') as writefile:
		replaced_val = ""
		for line in readfile:
			print line
			replaced_val += replace(line)
		writefile.write(replaced_val)

with file('mylog2.txt', 'r') as finalread:
	lines = finalread.readlines()
	print lines


# ****************************************
#
# Other built-in types
# pages 35 - 
#
# None								This is a built in type for null
# Sets								Sets are great for seeing the intersection or difference between 2 data sets
# 	add()							add another value to the set
# 	union()							creates a unique set between two sets
# 	intersection()					
#
# ****************************************

print "\n \n \n OTHER BUILT-IN TYPES \n \n \n"

flag = None

if flag is None:
	print 'nothing'

a = set()
a.add('aa')
a.add('bb')
b = set([11, 22])
print a, b
c = set([22, 33])
union = b.union(c)
intersection = b.intersection(c) 
print union, intersection

