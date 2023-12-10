# https://leetcode.com/problems/transpose-matrix/

class Solution(object):
	def transpose(self, matrix):
		return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

class Solution(object):
	def transpose(self, matrix):
		M = len(matrix)
		N = len(matrix[0])

		res = [[-1 for _ in range(M)] for _ in range(N)]
		for i in range(M):
			for j in range(N):
				res[j][i] = matrix[i][j]

		return res
