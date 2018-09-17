# https://leetcode.com/problems/max-area-of-island/description/

class Solution:
	def maxAreaOfIsland(self, grid):
		seen = set()
		maxarea = 0
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == 0 or (i, j) in seen:
					continue

				area = 0
				stack = [(i, j)]
				while stack:
					k, l = stack.pop()

					if (k, l) in seen:
						continue

					seen.add((k, l))
					area += 1

					if (k + 1, l) not in seen and k + 1 < len(grid) and grid[k + 1][l] == 1:
						stack.append((k + 1, l))
					if (k - 1, l) not in seen and k - 1 >= 0 and grid[k - 1][l] == 1:
						stack.append((k - 1, l))
					if (k, l + 1) not in seen and l + 1 < len(grid[i]) and grid[k][l + 1] == 1:
						stack.append((k, l + 1))
					if (k, l - 1) not in seen and l - 1 >= 0 and grid[k][l - 1] == 1:
						stack.append((k, l - 1))

				maxarea = max(area, maxarea)

		return maxarea
