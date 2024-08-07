# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/ 

class Solution(object):
	def minFlips(self, grid):
		M = len(grid)
		N = len(grid[0])

		rows = 0
		for i in range(M):
			for j in range(N // 2):
				if grid[i][N - j - 1] != grid[i][j]:
					rows += 1

		cols = 0
		for j in range(N):
			for i in range(M // 2):
				if grid[M - i - 1][j] != grid[i][j]:
					cols += 1

		return min(rows, cols)
