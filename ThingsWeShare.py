#!/usr/bin/python

# Things We Share Application

import re

# open the file
filename = "listLinkedin.txt"
new_file = open(filename, 'rU')
# read the file
print new_file
p = re.compile('') # put any expression in to get the data in between, such as '<P><B>.+</B>'
for line in new_file:
	line = line.strip()
	print line
	m = p.match( line ) # get match object in each line
	if m is not None:
		print m.groups()[0]	# print out 1st thing that matches