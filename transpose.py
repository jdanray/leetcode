# https://leetcode.com/problems/transpose-matrix/

class Solution(object):
	def transpose(self, A):
		m = len(A)
		n = len(A[0])
		B = [[0 for _ in range(n)] for _ in range(m)]
		for i in range(m):
			for j in range(n):
				B[j][i] = A[i][j]

		return B
