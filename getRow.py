# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution:
	def getRow(self, n):
		if n < 0:
			return []
		elif n == 0:
			return [1]
		row = [1, 1]
		for _ in range(n - 1):
			row = [1] + [row[j - 1] + row[j] for j in range(1, len(row))] + [1]
		return row
