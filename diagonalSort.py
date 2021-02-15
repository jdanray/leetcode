# https://leetcode.com/problems/sort-the-matrix-diagonally/

# O((M * N) * (M + M*lg(M)))
# O(M**2 * lg(M) * N)
class Solution(object):
	def diagonalSort(self, mat):
		M = len(mat)
		N = len(mat[0])
		for i in range(M):
			for j in range(N):
				k = i
				l = j
				diag = []
				while k < M and l < N:
					diag += [mat[k][l]]
					k += 1
					l += 1

				diag = sorted(diag)
				k = i
				l = j
				while k < M and l < N:
					mat[k][l] = diag[k - i]
					k += 1
					l += 1

		return mat
