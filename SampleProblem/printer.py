import fileinput
import sys
import sys


theMatrix = [['.' for i in range(y)] for j in range(x)]

passFirst = True



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
