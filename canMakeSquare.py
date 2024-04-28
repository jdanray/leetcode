# https://leetcode.com/problems/make-a-square-with-the-same-color/ 

class Solution(object):
	def canMakeSquare(self, grid):
		N = 3

		for i in range(N - 1):
			for j in range(N - 1):
				w = 0
                
				if grid[i][j] == 'W':
					w += 1
				if grid[i][j + 1] == 'W':
					w += 1
				if grid[i + 1][j] == 'W':
					w += 1
				if grid[i + 1][j + 1] == 'W':
					w += 1

				if w != 2:
					return True

		return False
