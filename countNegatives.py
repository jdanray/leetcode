# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/ 

# O(M + N)
class Solution(object):
	def countNegatives(self, grid):
		M = len(grid)
		N = len(grid[0])

		j = 0
		res = 0
		for i in range(M - 1, -1, -1):
			while j < N and grid[i][j] >= 0:
				j += 1

			res += N - j

		return res

# O(M * N)
class Solution(object):
	def countNegatives(self, grid):
		return sum(grid[i][j] < 0 for i in range(len(grid)) for j in range(len(grid[0])))

# O(M * N)
class Solution(object):
	def countNegatives(self, grid):
		n = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] < 0:
					n += 1
		return n
