# https://leetcode.com/problems/number-of-closed-islands/ 

class Solution(object):
	def closedIsland(self, grid):
		def dfs(i, j):
			if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
				return False

			if grid[i][j] == 1:
				return True

			grid[i][j] = 1

			res = True
			for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
				res &= dfs(i + di, j + dj)
			return res

		isles = 0
		for i in range(len(grid)):
			for  j in range(len(grid[i])):
				if grid[i][j] == 0 and dfs(i, j):
					isles += 1
		return isles
