# https://leetcode.com/problems/unique-paths-ii/submissions/ 

class Solution(object):
	def uniquePathsWithObstacles(self, grid):
		M = len(grid)
		N = len(grid[0])

		dp = [[0 for _ in range(N)] for _ in range(M)]
		dp[0][0] = 1 - grid[0][0]
        
		for i in range(M):
			for j in range(N):
				if grid[i][j] == 1:
					continue

				if i - 1 >= 0:
					dp[i][j] += dp[i - 1][j]

				if j - 1 >= 0:
					dp[i][j] += dp[i][j - 1]

		return dp[-1][-1]
