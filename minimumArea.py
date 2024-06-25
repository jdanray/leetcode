# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/ 

class Solution(object):
	def minimumArea(self, grid):
		top = float('inf')
		bot = 0
		left = float('inf')
		right = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					top = min(top, i)
					bot = max(bot, i)
					left = min(left, j)
					right = max(right, j)

		return (bot - top + 1) * (right - left + 1)
