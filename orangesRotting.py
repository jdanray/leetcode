# https://leetcode.com/problems/rotting-oranges/

class Solution(object):
	def orangesRotting(self, grid):
		old = -1
		ndays = 0
		while old < ndays:
			change = set()
			for i in range(len(grid)):
				for j in range(len(grid[i])):
					if grid[i][j] == 1:
						if j - 1 >= 0 and grid[i][j - 1] == 2:
							change.add((i, j))
						elif j + 1 < len(grid[i]) and grid[i][j + 1] == 2:
							change.add((i, j))
						elif i - 1 >= 0 and grid[i - 1][j] == 2:
							change.add((i, j))
						elif i + 1 < len(grid) and grid[i + 1][j] == 2:
							change.add((i, j))

			old = ndays
			if change:
				for (i, j) in change:
					grid[i][j] = 2
				ndays += 1

		if all(grid[i][j] == 0 or grid[i][j] == 2 for i in range(len(grid)) for j in range(len(grid[i]))):
			return ndays
		else:
			return -1
