# 

class Solution(object):
	def maxMoves(self, grid):
		deltas = [-1, 0, 1]

		M = len(grid)
		N = len(grid[0])

		memo = {}
		def dp(i, j):
			if j + 1 == N:
				return 0

			if (i, j) in memo:
				return memo[i, j]

			res = 0
			for di in deltas:
				if i + di >= 0 and i + di < M and grid[i + di][j + 1] > grid[i][j]:
					res = max(res, 1 + dp(i + di, j + 1))

			memo[i, j] = res
			return memo[i, j]

		return max(dp(i, 0) for i in range(M)) 

class Solution(object):
	def maxMoves(self, grid):
		deltas = [-1, 0, 1]

		M = len(grid)
		N = len(grid[0])

		memo = {}
		def dp(i, j):
			if j + 1 == N:
				return 0

			if (i, j) not in memo:
				memo[i, j] = max([1 + dp(i + di, j + 1) for di in deltas if i + di >= 0 and i + di < M and grid[i + di][j + 1] > grid[i][j]] or [0])

			return memo[i, j]

		return max(dp(i, 0) for i in range(M)) 

# Py3
class Solution(object):
	def maxMoves(self, grid):
		@functools.lru_cache(None)
		def dp(i, j): return 0 if j + 1 == len(grid[0]) else max([1 + dp(i + di, j + 1) for di in [-1, 0, 1] if i + di >= 0 and i + di < len(grid) and grid[i + di][j + 1] > grid[i][j]] or [0])
		return max(dp(i, 0) for i in range(len(grid))) 