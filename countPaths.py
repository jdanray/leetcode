# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/ 

class Solution(object):
	def countPaths(self, grid):
		MOD = 10**9 + 7
		deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		M = len(grid)
		N = len(grid[0])

		memo = {}
		def dp(i, j):
			if (i, j) in memo:
				return memo[i, j]

			res = 1
			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj

				if ni >= 0 and ni < M and nj >= 0 and nj < N and grid[ni][nj] > grid[i][j]:
					res += dp(ni, nj)

			memo[i, j] = res
			return memo[i, j]

		return sum(dp(i, j) for i in range(M) for j in range(N)) % MOD
