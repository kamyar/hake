import fileinput
import sys

#HACKIN' IN PROGRESS

# inputFile = open(sys.argv[1], "r")

# [x, y] = map(int, inputFile.readline().strip("\n").split(" "))

x,y = 14,80 
theMatrix = [['.' for i in range(y)] for j in range(x)]

passFirst = True

def eraseCell(i, j):
	theMatrix[i][j] = '.'

def paintSquare(i, j, radius):
	startRow = i - radius
	startColumn = j - radius
	endRow = i + radius
	endColumn = j + radius

	for x in range(startRow, endRow + 1):
		for y in range(startColumn, endColumn + 1):
			theMatrix[x][y] = '#'

def paintLine(startRow, startColumn, endRow, endColumn):
	for x in range(startRow, endRow + 1):
		for y in range(startColumn, endColumn + 1):
			theMatrix[x][y] = '#'

for line in fileinput.input():
	if passFirst == True:
		passFirst = False
		continue

	commandLine = line.strip("\n").split(" ")

	if commandLine[0] == 'ERASE_CELL':
		print commandLine
		eraseCell(int(commandLine[1]), int(commandLine[2]))
	elif commandLine[0] == 'PAINT_SQUARE':
		paintSquare(int(commandLine[1]), int(commandLine[2]), int(commandLine[3]))
	elif commandLine[0] == 'PAINT_LINE':
		paintLine(int(commandLine[1]), int(commandLine[2]), int(commandLine[3]), int(commandLine[4]))

outputFile = open("produced.in", "w")
outputFile.write("%s %s\n" %(x, y))

for line in theMatrix:
	outputFile.write(''.join(line))
	outputFile.write("\n")

outputFile.close()
