# https://leetcode.com/problems/check-if-matrix-is-x-matrix/ 

class Solution(object):
	def checkXMatrix(self, grid):
		N = len(grid)

		for i in range(N):
			for j in range(N):
				if j == i or j == N - 1 - 1:
					if grid[i][j] == 0:
						return False
				elif grid[i][j] != 0:
					return False

		return True
