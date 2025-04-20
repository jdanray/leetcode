# https://leetcode.com/problems/design-spreadsheet/

class Spreadsheet(object):
	def __init__(self, rows):
		self.value = dict()

	def setCell(self, cell, value):
		self.value[cell] = value

	def resetCell(self, cell):
		self.value[cell] = 0

	def getValue(self, formula):
		x, y = formula[1:].split('+')

		if x[0].isalpha():
			xval = self.value[x] if x in self.value else 0
		else:
			xval = int(x)

		if y[0].isalpha():
			yval = self.value[y] if y in self.value else 0
		else:
			yval = int(y)

		return xval + yval