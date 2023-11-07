# https://leetcode.com/problems/find-champion-i/ 

class Solution(object):
	def findChampion(self, grid):
		N = len(grid)
		for i in range(N):
			if all(grid[j][i] == 0 for j in range(N)):
				return i
