# https://leetcode.com/problems/surrounded-regions/description/

class Solution:
	def solve(self, grid):
		seen = set()
		flipover = set()
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if grid[i][j] == 'X' or (i, j) in seen:
					continue

				stack = [(i, j)]
				seen.add((i, j))
				checked = {(i, j)}
				flip = True
				while stack:
					k, l = stack.pop()

					if k == 0 or l == 0 or k == len(grid) - 1 or l == len(grid[i]) - 1:
						flip = False
				
					for m, n in [(k + 1, l), (k - 1, l), (k, l + 1), (k, l - 1)]:
						if m < 0 or n < 0 or m >= len(grid) or n >= len(grid[i]):
							continue 
						if (m, n) not in seen and grid[m][n] == 'O':
							stack.append((m, n))
							seen.add((m, n))
							checked.add((m, n))

				if flip:
					flipover |= checked

		for i, j in flipover:
			grid[i][j] = 'X'
