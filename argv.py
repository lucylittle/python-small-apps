from sys import argv


def main():
  script, first, second, third = argv
  print "The script is called:", script
  print "Your first variable is:", first
  print "Your second variable is:", second
  print "Your third variable is:", third

if __name__ == "__main__":
  main()
