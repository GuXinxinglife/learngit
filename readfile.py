#!/usr/bin/python

# get file name
fname=input('Enter file name:')

# attempt to open file for reading
try:
	fobj=open(fname,'r')
except IOError as e:
	print('*** file open error',e)
else:
	# display contents to the screen
	for eachLine in fobj:
		print(eachLine)
	fobj.close()

