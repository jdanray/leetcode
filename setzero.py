# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
	def setZeroes(self, matrix):
		changed = set()
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if matrix[i][j] == 0 and (i, j) not in changed:
					for k in range(len(matrix[i])):
						if matrix[i][k] != 0:
							matrix[i][k] = 0
							changed.add((i, k))
					for k in range(len(matrix)):
						if matrix[k][j] != 0:
							matrix[k][j] = 0
							changed.add((k, j))
