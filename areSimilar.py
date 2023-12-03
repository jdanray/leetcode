# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/ 

class Solution(object):
	def areSimilar(self, mat, k):
		M = len(mat)
		N = len(mat[0])
		return all(mat[i][j] == mat[i][(j + k) % N] for i in range(M) for j in range(N))

class Solution(object):
	def areSimilar(self, mat, k):
		M = len(mat)
		N = len(mat[0])

		for i in range(M):
			for j in range(N):
				if i % 2 == 0:
					s = (j + k) % N
				else:
					s = (j - k) % N

				if mat[i][j] != mat[i][s]:
					return False

		return True
