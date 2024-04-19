# https://leetcode.com/problems/number-of-islands/description/

class Solution:
	def numIslands(self, grid):
		seen = set()
		nislands = 0
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == "0" or (i, j) in seen:
					continue

				nislands += 1

				seen.add((i, j))
				stack = [(i, j)]
				while stack:
					k, l = stack.pop()

					for m, n in [(k + 1, l), (k - 1, l), (k, l + 1), (k, l - 1)]:
						if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[i]):
							continue
						if (m, n) not in seen and grid[m][n] == "1":
							seen.add((m, n))
							stack.append((m, n))

		return nislands

# Modify grid directly to keep track of visited lands
class Solution(object):
	def numIslands(self, grid):
		M = len(grid)
		N = len(grid[0])
		deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

		def mark(i, j):
			grid[i][j] = '0'

			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj
				if ni >= 0 and ni < M and nj >= 0 and nj < N and grid[ni][nj] == '1':
					mark(ni, nj)

		res = 0
		for i in range(M):
			for j in range(N):
				if grid[i][j] == '1':
					res += 1
					mark(i, j)

		return res

# Store coordinates of visited lands in a set
class Solution(object):
	def numIslands(self, grid):
		M = len(grid)
		N = len(grid[0])
		deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

		seen = set()
		def mark(i, j):
			seen.add((i, j))

			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj
				if (ni, nj) not in seen and ni >= 0 and ni < M and nj >= 0 and nj < N and grid[ni][nj] == '1':
					mark(ni, nj)

		res = 0
		for i in range(M):
			for j in range(N):
				if (i, j) not in seen and grid[i][j] == '1':
					res += 1
					mark(i, j)

		return res
