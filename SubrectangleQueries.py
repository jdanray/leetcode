# https://leetcode.com/problems/subrectangle-queries/ 

class SubrectangleQueries(object):
	def __init__(self, rectangle):
		self.rect = rectangle
		self.subrects = []
	
	def updateSubrectangle(self, row1, col1, row2, col2, newValue):
		self.subrects = [[row1, col1, row2, col2, newValue]] + self.subrects

	def getValue(self, row, col):
		for (r1, c1, r2, c2, val) in self.subrects:
			if r1 <= row <= r2 and c1 <= col <= c2:
				return val

		return self.rect[row][col]
