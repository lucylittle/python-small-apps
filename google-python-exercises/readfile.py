#!/usr/bin/python2.7.2 -tt

import sys

def Cat(filename):
  f = open(filename, 'rU')
  lines = f.readlines()
  print lines
  f.close()

# Define a main () function that prints ..
def main ():
  Cat(sys.argv[1])


# This is the standard boilerplate that calls the main function
if __name__ == '__main__':
  main()
