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
