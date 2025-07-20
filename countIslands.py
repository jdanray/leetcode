# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

class Solution(object):
	def countIslands(self, grid, k):
		M = len(grid)
		N = len(grid[0])
		deltas = [[0, -1], [0, 1], [1, 0], [-1, 0]]

		seen = set()
		# pre: 
		# grid[i][j] is an actual cell in grid
		# grid[i][j] is positive
		# grid[i][j] hasn't been visited before
		# post:
		# the total value of the island
		def dfs(i, j):
			seen.add((i, j))

			res = grid[i][j]
			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj
				if (ni, nj) not in seen and ni < M and ni >= 0 and nj < N and nj >= 0 and grid[ni][nj] > 0:
					res += dfs(ni, nj)
			return res

		res = 0
		for i in range(M):
			for j in range(N):
				if (i, j) not in seen and grid[i][j] > 0:
					val = dfs(i, j)
					if val % k == 0:
						res += 1
		return res