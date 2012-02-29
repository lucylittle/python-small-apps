#!/usr/bin/python2.7.2 -tt

import sys

def Hello(name):
  if name == 'karam' or name == 'cj':
    name = 'Karambir'
    print 'Changing name'
  else:
    print 'Didn\'t expect that name :)'
  name = name + '!!!'
  print 'Hello', name	

def main():
  arguement = sys.argv[1] 
#  if arguement == false:
#    print 'give some value'
#  else:
  print arguement, '???'
  Hello(arguement)


if __name__ == "__main__":
  main()
