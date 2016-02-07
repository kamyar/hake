class Matrix():
	def __init__(self, x, y):
		self.row = x
		self.column = y
		self.matrix = []
		self.firstPointer = -1
		self.secondPointer = -1
		self.lines = []

	def addLine(self, line):
		self.matrix.append(list(line))

	def __repr__(self):
		return str(self.matrix)

	def cell(self, x, y):
		if x < self.row and y < self.column:
			return self.matrix[x][y]
		else:
			return '-'

	def startSearching(self):
		push = False
		for i in range(self.row):
			for j in range(self.column):
				if self.isCellBlack(i, j):
					self.marking(i, j)
				if self.isCellBlack(i, j) == False:
					push = True
				if j == self.column - 1 or push == True:
					t = (i, self.firstPointer, self.secondPointer)
					if self.firstPointer != -1 and self.secondPointer != -1:
						self.lines.append(t)
					self.firstPointer = -1
					self.secondPointer = -1
					push = False
		print self.lines

	
	def marking(self, i, j):
		if self.firstPointer == -1:
				self.firstPointer = j
		else:
				self.secondPointer = j



	def isCellBlack(self, i, j):
		if self.cell(i, j) == '#':
			return True
		else:
			return False

	def percentageOfBlackInSquare(self, startRow, startColumn, squareRadius):
		#print "Starting from ", startRow, startColumn

		totalBlackCount = 0
		totalCellCount = 0
		for i in range(startRow, startRow + squareRadius):
			for j in range (startColumn, startColumn + squareRadius):
				totalCellCount += 1
				if self.isCellBlack(i, j):
					totalBlackCount += 1

		#print "cellCount ", totalCellCount
		#print "blackCount " , totalBlackCount

		return float(totalBlackCount / float(totalCellCount))

	def signCellAs(self, i, j, mark):
		self.matrix[i][j] = mark

	def ignSquareAsMarked(self, startRow, startColumn, squareRadius):
		for i in range(startRow, startRow + squareRadius):
			for j in range (startColumn, startColumn + squareRadius):
				self.signCellAs(i, j, '-')

	def iterateFromPoint(self, i, j):
		#print "Starting from ", i, j

		everySquareList = []

		foundRow, foundColumn, bestFoundRadius = -1, -1, -1

		for squareRadius in range(1, min(self.row, self.column) + 1, 2):
			if i + squareRadius > self.row or j + squareRadius > self.column:
				continue

			everySquareList.append((i, j, squareRadius))

			if self.percentageOfBlackInSquare(i, j, squareRadius) > 0.7:
				if squareRadius > bestFoundRadius:
					foundRow, foundColumn, bestFoundRadius = i, j, squareRadius

		if bestFoundRadius != -1:
			print "FOUND ", foundRow, foundColumn, bestFoundRadius
			self.signSquareAsMarked(foundRow, foundColumn, bestFoundRadius)

		#print everySquareList
