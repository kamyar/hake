class Matrix():
	def __init__(self, x, y):
		self.row = x
		self.column = y
		self.matrix = []
		self.firstPointer = -1
		self.secondPointer = -1
		self.HorizontalLines = []
		self.VerticalLines = []

	def addLine(self, line):
		self.matrix.append(list(line))

	def __repr__(self):
		return str(self.matrix)

	def cell(self, x, y):
		if x < self.row and y < self.column:
			return self.matrix[x][y]
		else:
			return '-'


	def startSearchingVertical(self):
		push = False
		for i in range(self.column):
			for j in range(self.row):
				if self.isCellBlack(j, i):
					self.markingVert(i, j)
				if self.isCellBlack(j, i) == False:
					push = True
				if j == self.row - 1 or push == True:
					t = (i, self.firstPointer, self.secondPointer)
					if self.firstPointer != -1 and self.secondPointer != -1:
						self.VerticalLines.append(t)
					self.firstPointer = -1
					self.secondPointer = -1
					push = False
		#print self.VerticalLines
		#print len(self.VerticalLines)
	
	def markingVert(self, i, j):
		if self.firstPointer == -1:
				self.firstPointer = j
				self.secondPointer = j
		else:
				self.secondPointer = j

	

	def startSearchingHorizontal(self):
		push = False
		for i in range(self.row):
			for j in range(self.column):
				if self.isCellBlack(i, j):
					self.markingHor(i, j)
				if self.isCellBlack(i, j) == False:
					push = True
				if j == self.column - 1 or push == True:
					t = (i, self.firstPointer, self.secondPointer)
					if self.firstPointer != -1 and self.secondPointer != -1:
						self.HorizontalLines.append(t)
					self.firstPointer = -1
					self.secondPointer = -1
					push = False
		#print self.HorizontalLines
		#print len(self.HorizontalLines)

	
	def markingHor(self, i, j):
		if self.firstPointer == -1:
				self.firstPointer = j
				self.secondPointer = j
		else:
				self.secondPointer = j


	def isCellBlack(self, i, j):
		if self.cell(i, j) == '#':
			return True
		else:
			return False
