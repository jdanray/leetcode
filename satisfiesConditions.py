# https://leetcode.com/problems/check-if-grid-satisfies-conditions/ 

class Solution(object):
	def satisfiesConditions(self, grid):
		M = len(grid)
		N = len(grid[0])

		for i in range(M):
			for j in range(N):
				if i + 1 < M and grid[i][j] != grid[i + 1][j]:
					return False
				elif j + 1 < N and grid[i][j] == grid[i][j + 1]:
					return False

		return True
