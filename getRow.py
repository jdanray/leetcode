# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
	def getRow(self, rowIndex):
		row = [1]
		for _ in range(rowIndex):
			row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]            
		return row

class Solution(object):
	def getRow(self, rowIndex):
		if rowIndex == 0:
			return [1]

		prev = self.getRow(rowIndex - 1)
		return [1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1]
