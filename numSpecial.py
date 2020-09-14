# https://leetcode.com/problems/special-positions-in-a-binary-matrix/ 

class Solution(object):
	def numSpecial(self, mat):
		M = len(mat)
		N = len(mat[0])

		res = 0
		for i in range(M):
			for j in range(N):
				if mat[i][j] == 0:
					continue

				if any(mat[i][k] == 1 and k != j for k in range(N)):
					continue

				if any(mat[k][j] == 1 and k != i for k in range(M)):
					continue

				res += 1

		return res
