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

class Solution(object):
	def numSpecial(self, mat):
		M = len(mat)
		N = len(mat[0])

		row = {}
		for i in range(M):
			row[i] = sum(mat[i])

		col = {}
		for j in range(N):
			col[j] = sum(mat[k][j] for k in range(M))

		res = 0
		for i in range(M):
			for j in range(N):
				if mat[i][j] == 1 and row[i] == 1 and col[j] == 1:
					res += 1

		return res
