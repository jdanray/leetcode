# https://leetcode.com/problems/coloring-a-border/

class Solution(object):
	def colorBorder(self, grid, r0, c0, color):
		ogcolor = grid[r0][c0]
		stack = [(r0, c0)]
		seen = set()
		border = set()
		while stack:
			r, c = stack.pop()

			for dr, dc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
				if dr < 0 or dr >= len(grid) or dc < 0 or dc >= len(grid[0]) or grid[dr][dc] != ogcolor:
					border.add((r, c))
				elif (dr, dc) not in seen:
					stack.append((dr, dc))
					seen.add((dr, dc))

		for (r, c) in border:
			grid[r][c] = color

		return grid
