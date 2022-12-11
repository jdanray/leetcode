# https://leetcode.com/problems/delete-greatest-value-in-each-row/ 

class Solution(object):
	def deleteGreatestValue(self, grid):
		M = len(grid)
		N = len(grid[0])

		for i in range(M):
			grid[i] = sorted(grid[i], reverse=True)

		res = 0
		for j in range(N):
			res += max(grid[i][j] for i in range(M))

		return res
