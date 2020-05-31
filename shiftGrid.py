# https://leetcode.com/problems/shift-2d-grid/ 

class Solution(object):
	def shiftGrid(self, grid, k):
		M = len(grid)
		N = len(grid[0])
		for _ in range(k):
			prev = grid[M - 1][N - 1]
			for i in range(M):
				for j in range(N):
					prev, grid[i][j] = grid[i][j], prev

		return grid
