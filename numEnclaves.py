# https://leetcode.com/problems/number-of-enclaves/

class Solution(object):
	def numEnclaves(self, A):
		N = len(A)
		M = len(A[0])

		def zero(i, j):
			if i >= 0 and j >= 0 and i < N and j < M and A[i][j] == 1:
				A[i][j] = 0

				zero(i + 1, j)
				zero(i - 1, j)
				zero(i, j + 1)
				zero(i, j - 1)

		for i in range(N):
			zero(A[i][0])
			zero(A[i][M - 1])

		for j in range(M):
			zero(A[0][j])
			zero(A[N - 1][j])

		n = 0
		for i in range(N):
			for j in range(M):
				if A[i][j] == 1:
					n += 1

		return n
