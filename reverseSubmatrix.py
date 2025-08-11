# https://leetcode.com/problems/flip-square-submatrix-vertically/

class Solution(object):
	def reverseSubmatrix(self, grid, x, y, k):
		for j in range(k):
			for i in range(k // 2):
				l = x + k - i - 1
				grid[x + i][y + j], grid[l][y + j] = grid[l][y + j], grid[x + i][y + j]
                
		return grid