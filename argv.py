from sys import argv


def aksh():
	script, first, second, third = argv
	print "The script is called:", script
	print "Your first variable is:", first
	print "Your second variable is:", second
	print "Your third variable is:", third
	
#def main():
#	print 'Error in program'

#def aksh():

if __name__ == "__main__":
    main()
else:
    aksh()  
