# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

class Solution(object):
	def minimumOperations(self, grid):
		M = len(grid)
		N = len(grid[0])

		res = 0
		for j in range(N):
			prev = grid[0][j]
			for i in range(1, M):
				d = max(0, prev - grid[i][j] + 1)
				res += d
				prev = grid[i][j] + d

		return res