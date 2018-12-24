# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

# O(m * n) time
# O(m + n) space
class Solution:
	def maxIncreaseKeepingSkyline(self, grid):
		m, n = len(grid), len(grid[0])

		cmax = []
		for j in range(n):
			cmax.append(max(grid[i][j] for i in range(m)))

		rmax = []
		for i in range(m):
			rmax.append(max(grid[i]))

		s = sum(grid[i] for i in range(m))
		snew = sum(min(rmax[i], cmax[j]) for i in range(m) for j in range(n))

		return snew - s

# O(m**2 * n) time
# O(1) space
class Solution:
	def maxIncreaseKeepingSkyline(self, grid):
		d = 0
		for i in range(len(grid)):
			rmax = max(grid[i])
			for j in range(len(grid[i])):
				cmax = max(grid[i][j] for i in range(len(grid)))
				d += min(rmax, cmax) - grid[i][j]
		return d

# Leetcode's program
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        col_maxes = [max(col) for col in zip(*grid)]

        return sum(min(row_maxes[r], col_maxes[c]) - val
                   for r, row in enumerate(grid)
                   for c, val in enumerate(row))
