#!/usr/bin/python

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


#print "Horizontal Search"
matrix.startSearchingHorizontal()
#print "\n"

#print "Vertical Search"
matrix.startSearchingVertical()
#print "\n"

which = -1

if len(matrix.VerticalLines) >= len(matrix.HorizontalLines): 
	#print "Vertical Lines"
	#print matrix.VerticalLines
	which = 0
else:
	#print "Horizontal Lines"
	#print matrix.HorizontalLines
	which = 1

if which == 1:
	for i in range(len(matrix.VerticalLines)):
		print "PAINT_LINE " + str(matrix.VerticalLines[i][0]) + " " + str(matrix.VerticalLines[i][1]) + " " + str(matrix.VerticalLines[i][0]) + " " + str(matrix.VerticalLines[i][2])

elif which == 0:
	for i in range(len(matrix.HorizontalLines)):
		print "PAINT_LINE " + str(matrix.HorizontalLines[i][0]) + " " + str(matrix.HorizontalLines[i][1]) + " " + str(matrix.HorizontalLines[i][0]) + " " + str(matrix.HorizontalLines[i][2])

			
