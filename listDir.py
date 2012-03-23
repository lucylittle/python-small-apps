#Listing Directory files

import sys
import os
import commands

def list(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    path = os.path.join(dir, filename)
    print path
    print os.path.abspath(path)

def listcommand(dir):
  cmd = 'ls -l ' + dir
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    print sys.stderr.write('there was an error: ' + output)
    sys.exit(1)  
  print output


def main():
  py, option, direc = sys.argv
#  direc = sys.argv[2]
  if option == 1:
    list(direc)
  elif option == 2:
    listcommand(direc)
  else:#if direc == None:
    print 'ERROR: Use 1 for simple Listing and 2 for Advance Listing'
    sys.exit(1)

if __name__ == "__main__":
  main()
