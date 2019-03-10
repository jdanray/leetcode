# https://leetcode.com/problems/minimum-path-sum/

class Solution:
	def minPathSum(self, grid):
		M = len(grid)
		N = len(grid[0])

		memo = {}
		def helper(i, j):
			if (i, j) not in memo:
				memo[(i, j)] = grid[i][j]
				if i + 1 < M and j + 1 < N:
					memo[(i, j)] += min(helper(i + 1, j), helper(i, j + 1))
				elif i + 1 < M:
					memo[(i, j)] += helper(i + 1, j)
				elif j + 1 < N:
					memo[(i, j)] += helper(i, j + 1)

			return memo[(i, j)]

		return helper(0, 0)

class Solution:
	def minPathSum(self, grid):
		if not grid:
			return 0

		M = len(grid)
		N = len(grid[0])

		memo = {}
		def helper(i, j):
			if (i, j) in memo:
				return memo[(i, j)]

			m = grid[i][j]
			k = i + 1
			l = j + 1

			if k < M and l < N:
				m += min(helper(k, j), helper(i, l))
			elif k < M:
				m += helper(k, j)
			elif l < N:
				m += helper(i, l)

			memo[(i, j)] = m
			return memo[(i, j)]

		return helper(0, 0)

class Solution(object):
	memo = {}

	def minPathSum(self, grid):
		self.memo = {}
		return self.RminPathSum(grid, 0, 0)

	def RminPathSum(self, grid, i, j):
		m = len(grid)
		n = len(grid[0])
		if i == m - 1 and j == n - 1:
			return grid[i][j]
		if (i, j) not in self.memo:
			dirs = []
			if i + 1 < m:
				dirs.append((i + 1, j))
			if j + 1 < n:
				dirs.append((i, j + 1))
			self.memo[(i, j)] = grid[i][j] + min(self.RminPathSum(grid, *d) for d in dirs)
		return self.memo[(i, j)]
