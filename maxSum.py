# https://leetcode.com/problems/maximum-sum-of-an-hourglass/ 

class Solution(object):
	def maxSum(self, grid):
		M = len(grid)
		N = len(grid[0])

		res = 0
		for i in range(M - 2):
			for j in range(N - 2):
				s = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
				s += grid[i + 1][j + 1]
				s += grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]

				res = max(res, s)
                
		return res	
