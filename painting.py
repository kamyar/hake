import sys
from classDef import *

if len(sys.argv) < 2 or len(sys.argv) > 3:
	sys.exit('Usage: %s input-name' % sys.argv[0])

#HACKIN' IN PROGRESS

inputFile = open(sys.argv[1], "r")

[x, y] = map(int, inputFile.readline().strip("\n").split(" "))

matrix = Matrix(x, y)

while True:
	line = inputFile.readline().strip("\n")

	if not line: 
		break

	matrix.addLine(line)

#print matrix

#print matrix.cell(2, 2)

matrix.startSearching()