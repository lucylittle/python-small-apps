#!/usr/bin/python2.7.2 -tt

import sys

def Hello(name):
	if name == 'karam' or name == 'cj':
		name = 'Karambir'
		print 'Changing name'
	else:
		print 'Else'
	name = name + '!!!'
	print 'Hello', name	

def main():
	Hello(sys.argv[1])


if __name__ == "__main__":
	main()
