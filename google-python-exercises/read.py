# author : Karambir Singh Nain

import sys

def Cat(filename):
  f = open(filename, 'rU')
  text = f.read()
  print text,
  f.close()

# define a main function here

def main ():
  Cat(sys.argv[1])

# Boilerplate syntax to call main function

if __name__ == '__main__':
  main()
