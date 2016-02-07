class Matrix():
	def __init__(self, x, y):
		self.row = x
		self.column = y
		self.matrix = []
		self.commandList = []

	def addLine(self, line):
		self.matrix.append(list(line))

	def __repr__(self):
		totalString = str(len(self.commandList)) + "\n"

		for command in self.commandList:
			totalString += command

			if command != self.commandList[-1]:
				totalString += "\n"

		return totalString

	def cell(self, x, y):
		if x < self.row and y < self.column:
			return self.matrix[x][y]
		else:
			return '-'

	def startSearching(self):
		for i in range(self.row):
			for j in range(self.column):
				if self.isCellEqualTo(i, j, '#'):
					self.iterateFromPoint(i, j)
					#sys.stdout.write i,j


	def isCellEqualTo(self, i, j, mark):
		if self.cell(i, j) == mark:
			return True
		else:
			return False

	def addSquarePaint(self, startRow, startColumn, squareRadius):
		trueRadius = (squareRadius - 1) / 2

		self.commandList.append("PAINT_SQUARE %d %d %d" % (startRow + trueRadius, startColumn + trueRadius, trueRadius))

	def addErasePaint(self, row, column):
		self.commandList.append("ERASE_CELL %d %d" % (row, column))

	def percentageOfBlackInSquare(self, startRow, startColumn, squareRadius):
		#sys.stdout.write "Starting from ", startRow, startColumn

		totalBlackCount = 0
		totalCellCount = 0
		for i in range(startRow, startRow + squareRadius):
			for j in range (startColumn, startColumn + squareRadius):
				totalCellCount += 1
				if self.isCellEqualTo(i, j, '#'):
					totalBlackCount += 1

		return float(totalBlackCount / float(totalCellCount))

	def signCellAs(self, i, j, mark):
		if self.matrix[i][j] != '#':
			self.addErasePaint(i, j)

		self.matrix[i][j] = mark

	def signSquareAsMarked(self, startRow, startColumn, squareRadius):
		for i in range(startRow, startRow + squareRadius):
			for j in range (startColumn, startColumn + squareRadius):
				self.signCellAs(i, j, '-')

	def iterateFromPoint(self, i, j):
		foundRow, foundColumn, bestFoundRadius = -1, -1, -1

		for squareRadius in range(1, min(self.row, self.column) + 1, 2):
			if i + squareRadius > self.row or j + squareRadius > self.column:
				continue

			if self.percentageOfBlackInSquare(i, j, squareRadius) > 0.7:
				if squareRadius > bestFoundRadius:
					foundRow, foundColumn, bestFoundRadius = i, j, squareRadius
			else:
				break

		if bestFoundRadius != -1:
			#sys.stdout.write "FOUND ", foundRow, foundColumn, bestFoundRadius
			self.addSquarePaint(foundRow, foundColumn, bestFoundRadius)
			self.signSquareAsMarked(foundRow, foundColumn, bestFoundRadius)
