# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution(object):
	def countUnguarded(self, m, n, guards, walls):
		deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

		guards = set((i, j) for (i, j) in guards)
		walls = set((i, j) for (i, j) in walls)
		seen = set()
		for (i, j) in guards:
			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj
				while ni >= 0 and ni < m and nj >= 0 and nj < n and (ni, nj) not in walls and (ni, nj) not in guards:
					seen.add((ni, nj))
					ni += di
					nj += dj

		return (m * n) - len(seen) - len(walls) - len(guards)