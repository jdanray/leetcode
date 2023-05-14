# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/ 

class Solution(object):
	def maxMoves(self, grid):
		M = len(grid)
		N = len(grid[0])
		deltas = [(-1, 1), (0, 1), (1, 1)]

		memo = {}
		def dp(i, j):
			if (i, j) in memo:
				return memo[i, j]

			res = 0
			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj
				if ni >= 0 and ni < M and nj >= 0 and nj < N and grid[ni][nj] > grid[i][j]:
					res = max(res, 1 + dp(ni, nj))

			memo[i, j] = res
			return memo[i, j]

		return max(dp(i, 0) for i in range(M))
