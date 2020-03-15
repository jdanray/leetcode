# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution(object):
	def luckyNumbers(self, matrix):
		M = len(matrix)
		N = len(matrix[0])
		colmaxs = set(max(matrix[i][j] for i in range(M)) for j in range(N))
		rowmins = set(min(row) for row in matrix)
		return list(colmaxs & rowmins)
