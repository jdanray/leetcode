# https://leetcode.com/problems/shortest-bridge/ 

class Solution(object):
	def shortestBridge(self, grid):
		M = len(grid)
		N = len(grid[0])

		def dist(i, j, k, l):
			return abs(i - k) + abs(j - l) - 1

		def discover():
			for i in range(M):
				for j in range(N):
					if grid[i][j] == 1:
						return dfs(i, j)			

		def dfs(i, j):
			if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] == 0:
				return set()

			grid[i][j] = 0

			res = {(i, j)}
			res |= dfs(i + 1, j)
			res |= dfs(i - 1, j)
			res |= dfs(i, j + 1)
			res |= dfs(i, j - 1)

			return res 

		island1 = discover()
		island2 = discover()

		return min(dist(i, j, k, l) for (i, j) in island1 for (k, l) in island2)
