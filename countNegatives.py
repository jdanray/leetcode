# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/ 

class Solution(object):
	def countNegatives(self, grid):
		n = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] < 0:
					n += 1
		return n
