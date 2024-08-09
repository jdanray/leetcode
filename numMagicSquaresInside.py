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

class Solution(object):
	def numMagicSquaresInside(self, grid):
		K = 3
		M = len(grid)
		N = len(grid[0])

		res = 0
		for i in range(M - K + 1):
			for j in range(N - K + 1):
				nums = {grid[i + r][j + c] for r in range(K) for c in range(K)}
				if nums != set(range(1, K * K + 1)):
					continue

				s = sum(grid[i][j + l] for l in range(K))
				fail = False

				for k in range(K):
					r = sum(grid[i + k][j + l] for l in range(K))
					if r != s:
						fail = True
						break

				if fail:
					continue

				for l in range(K):
					c = sum(grid[i + k][j + l] for k in range(K))
					if c != s:
						fail = True
						break

				if fail:
					continue

				d1 = sum(grid[i + k][j + k] for k in range(K))
				if d1 != s:
					continue

				d2 = sum(grid[i + k][j + K - 1 - k] for k in range(K))
				if d2 != s:
					continue

				res += 1

		return res
