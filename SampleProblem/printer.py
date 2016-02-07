import fileinput
import sys

if len(sys.argv) < 2 or len(sys.argv) > 3:
	sys.exit('Usage: %s input-name' % sys.argv[0])

#HACKIN' IN PROGRESS

inputFile = open(sys.argv[1], "r")

[x, y] = map(int, inputFile.readline().strip("\n").split(" "))

passFirst = True

for line in fileinput.input():
	if passFirst == True:
		passFirst = False
		continue

	print line.strip("\n")


