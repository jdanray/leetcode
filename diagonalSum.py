# https://leetcode.com/problems/matrix-diagonal-sum/

class Solution(object):
	def diagonalSum(self, mat):
		N = len(mat)
		s = 0
		for i in range(N):
			s += mat[i][i]
			s += mat[i][N - 1 - i]

		if N % 2 == 1:
			s -= mat[N // 2][N // 2]

		return s
