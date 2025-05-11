# https://leetcode.com/problems/equal-sum-grid-partition-i/

class Solution(object):
	def canPartitionGrid(self, grid):
		M = len(grid)
		N = len(grid[0])

		totalSum = sum(grid[i][j] for i in range(M) for j in range(N))

		s = 0
		for i in range(M):
			for j in range(N):
				s += grid[i][j]

			if s == totalSum - s:
				return True

		s = 0
		for j in range(N):
			for i in range(M):
				s += grid[i][j]

			if s == totalSum - s:
				return True

		return False