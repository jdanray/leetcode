# https://leetcode.com/problems/spiral-matrix/ 

class Solution(object):
	def spiralOrder(self, matrix):
		if not matrix:
			return []

		if not matrix[0]:
			return []

		rowstart = 0
		rowend = len(matrix) - 1
		colstart = 0
		colend = len(matrix[0]) - 1
		i = rowstart
		j = colstart
		res = []
		op = 0
		while rowstart <= i <= rowend and colstart <= j <= colend:
			res.append(matrix[i][j])

			if op == 0:
				if j < colend:
					j += 1
				else:
					op = 1
					i += 1
					rowstart += 1
			elif op == 1:
				if i < rowend:
					i += 1
				else:
					op = 2
					j -= 1
					colend -= 1
			elif op == 2:
				if j > colstart:
					j -= 1
				else:
					op = 3
					i -= 1
					rowend -= 1
			elif op == 3:
				if i > rowstart:
					i -= 1
				else:
					op = 0
					j += 1
					colstart += 1

		return res
