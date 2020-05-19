# https://leetcode.com/problems/magic-squares-in-grid/

class Solution(object):
	def numMagicSquaresInside(self, grid):
		M = len(grid)
		N = len(grid[0])
		res = 0
		for i in range(M - 2):
			for j in range(N - 2):
				nums = {grid[i + r][j + c] for r in range(3) for c in range(3)}
				if nums != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
					continue

				row1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
				row2 = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
				row3 = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
	
				col1 = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
				col2 = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
				col3 = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]

				diag1 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
				diag2 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]

				if row1 == row2 == row3 == col1 == col2 == col3 == diag1 == diag2:
					res += 1

		return res
