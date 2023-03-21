# https://leetcode.com/problems/check-knight-tour-configuration/ 

class Solution(object):
	def checkValidGrid(self, grid):
		N = len(grid)

		coord = collections.defaultdict(tuple)
		for i in range(N):
			for j in range(N):
				u = grid[i][j]
				coord[u] = (i, j)

		if coord[0] != (0, 0):
			return False

		visited = set()
		for u in range(N * N):
			v = u + 1

			if v not in coord and v < N * N:
				return False

			if coord[v] in visited:
				return False

			i, j = coord[u]
			jump = {(i - 2, j - 1), (i - 2, j + 1), (i + 2, j - 1), (i + 2, j + 1), (i - 1, j - 2), (i + 1, j - 2), (i - 1, j + 2), (i + 1, j + 2)}
			if coord[v] not in jump and v < N * N:
				return False

			visited.add(coord[u])

		return len(visited) == N * N 
