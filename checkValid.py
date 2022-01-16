# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/ 

class Solution(object):
	def checkValid(self, matrix):
		N = len(matrix)
		for i in range(N):
			row = {matrix[i][j] for j in range(N)}
			col = {matrix[j][i] for j in range(N)}

			if not all(n in row and n in col for n in range(1, N + 1)):
				return False

		return True
