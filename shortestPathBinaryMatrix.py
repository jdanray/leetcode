# https://leetcode.com/problems/shortest-path-in-binary-matrix/

class Solution(object):
	def shortestPathBinaryMatrix(self, grid):
		N = len(grid)
		queue = [(0, 0, 1)]
		seen = {(0, 0)}
		while queue:
			i, j, d = queue.pop(0)

			if grid[i][j] == 1:
				continue

			if i == N - 1 and j == N - 1:
				return d

			dij = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]
			for di, dj in dij:
				k = i + di
				l = j + dj

				if k >= N or k < 0 or l >= N or l < 0:
					continue

				if (k, l) in seen:
					continue

				seen.add((k, l))
				queue.append((k, l, 1 + d))

		return -1
