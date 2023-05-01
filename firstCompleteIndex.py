# https://leetcode.com/problems/first-completely-painted-row-or-column/ 

class Solution(object):
	def firstCompleteIndex(self, arr, mat):
		M = len(mat)
		N = len(mat[0])

		cell = dict()
		for r in range(M):
			for c in range(N):
				n = mat[r][c]
				cell[n] = (r, c)

		rows = collections.Counter()
		cols = collections.Counter()
		for i, n in enumerate(arr):
			r, c = cell[n]

			rows[r] += 1
			cols[c] += 1

			if rows[r] == N or cols[c] == M:
				return i
