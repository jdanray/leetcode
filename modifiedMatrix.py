# https://leetcode.com/problems/modify-the-matrix/ 

class Solution(object):
	def modifiedMatrix(self, matrix):
		M = len(matrix)
		N = len(matrix[0])

		res = [[0 for _ in range(N)] for _ in range(M)]
		for j in range(N):
			m = -1
			for i in range(M):
				m = max(m, matrix[i][j])
				res[i][j] = matrix[i][j]

			for i in range(M):
				if res[i][j] == -1:
					res[i][j] = m

		return res
