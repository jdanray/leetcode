# https://leetcode.com/problems/equal-row-and-column-pairs/ 

class Solution(object):
	def equalPairs(self, grid):
		N = len(grid)

		res = 0
		for i in range(N):
			for j in range(N):
				k = 0
				while k < N and grid[i][k] == grid[k][j]:
					k += 1

				if k == N:
					res += 1

		return res
