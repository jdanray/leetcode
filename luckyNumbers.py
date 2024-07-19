# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution(object):
	def luckyNumbers(self, matrix):
		M = len(matrix)
		N = len(matrix[0])

		minim = set(min(matrix[i][j] for j in range(N)) for i in range(M))
		maxim = set(max(matrix[i][j] for i in range(M)) for j in range(N))

		return list(minim & maxim)

class Solution(object):
	def luckyNumbers(self, matrix):
		M = len(matrix)
		N = len(matrix[0])

		res = []
		for i in range(M):
			minJ = min(list(range(N)), key=lambda j: matrix[i][j])
			maxi = max(matrix[k][minJ] for k in range(M))
			if maxi == matrix[i][minJ]:
				res.append(maxi)

		return res
