# https://leetcode.com/problems/minimum-path-sum/

class Solution(object):
	def minPathSum(self, grid):
		M = len(grid)
		N = len(grid[0])

		dp = [[0 for _ in range(N)] for _ in range(M)]
		for i in range(M):
			for j in range(N):
				dp[i][j] = grid[i][j]
				if i - 1 >= 0 and j - 1 >= 0:
					dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
				elif i - 1 >= 0:
					dp[i][j] += dp[i - 1][j]
				elif j - 1 >= 0:
					dp[i][j] += dp[i][j - 1] 

		return dp[M - 1][N - 1]

class Solution(object):
	def minPathSum(self, grid):
		M = len(grid)
		N = len(grid[0])

		memo = {}
		def dp(i, j):
			if i == M - 1 and j == N - 1:
				return grid[i][j]

			if (i, j) in memo:
				return memo[i, j]

			memo[i, j] = grid[i][j]

			if i + 1 < M and j + 1 < N:
				memo[i, j] += min(dp(i + 1, j), dp(i, j + 1))
			elif i + 1 < M: 
				memo[i, j] += dp(i + 1, j)
			elif j + 1 < N:
				memo[i, j] += dp(i, j + 1)

			return memo[i, j]

		return dp(0, 0)
