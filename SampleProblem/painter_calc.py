import sys
from classDef import *

# Check inpu file
if len(sys.argv) < 2 or len(sys.argv) > 3:
  sys.exit('Usage: %s input-name' % sys.argv[0])

with open(sys.argv[1], "r") as inputFile:
  x, y = map(int, inputFile.readline().strip("\n").split(" "))

  matrix = Matrix(x, y)

  for line in inputFile:
    line.strip("\n")
    matrix.addLine(line)

matrix.startSearching()

# print matrix


result = [['.' for i in range(y)] for j in range(x)] 



def eraseCell(i, j):
  result[i][j] = '.'

def paintSquare(i, j, radius):
  startRow = i - radius
  startColumn = j - radius
  endRow = i + radius
  endColumn = j + radius

  for x in range(startRow, endRow + 1):
    for y in range(startColumn, endColumn + 1):
      result[x][y] = '#'

def paintLine(startRow, startColumn, endRow, endColumn):
  for x in range(startRow, endRow + 1):
    for y in range(startColumn, endColumn + 1):
      result[x][y] = '#'




for cmd in matrix.commandList:
  cmd = cmd.split(" ")
  if cmd[0] == 'ERASE_CELL':
    eraseCell(int(cmd[1]), int(cmd[2]))
  elif cmd[0] == 'PAINT_SQUARE':
    paintSquare(int(cmd[1]), int(cmd[2]), int(cmd[3]))
  elif cmd[0] == 'PAINT_LINE':
    paintLine(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))

outputFile = open("produced.in", "w")
outputFile.write("%s %s\n" %(x, y))

for line in result:
  outputFile.write(''.join(line))
  outputFile.write("\n")

outputFile.close()


