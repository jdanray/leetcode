# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/ 

class Solution(object):
	def longestIncreasingPath(self, matrix):
		deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		M = len(matrix)
		N = len(matrix[0])

		memo = {}
		def dp(i, j):
			if (i, j) in memo:
				return memo[i, j]

			res = 1
			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj

				if ni >= 0 and ni < M and nj >= 0 and nj < N and matrix[ni][nj] > matrix[i][j]:
					res = max(res, 1 + dp(ni, nj))

			memo[i, j] = res
			return memo[i, j]

		return max(dp(i, j) for i in range(M) for j in range(N))
