# https://leetcode.com/problems/minimum-falling-path-sum-ii/ 

class Solution(object):
	def minFallingPathSum(self, grid):
		N = len(grid)

		dp = [[float('inf') for _ in range(N)] for _ in range(N)]
		for j in range(N):
			dp[0][j] = grid[0][j]

		for i in range(1, N):
			for j in range(N):
				for k in range(N):
					if k != j:
						dp[i][j] = min(dp[i][j], dp[i - 1][k] + grid[i][j])

		return min(dp[-1])
