# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution(object):
	def hasValidPath(self, grid):
		M = len(grid)
		N = len(grid[0])
		dest = (M - 1, N - 1)
		
		dirs = {}
		dirs[1] = [[0, -1], [0, 1]]
		dirs[2] = [[-1, 0], [1, 0]]
		dirs[3] = [[0, -1], [1, 0]]
		dirs[4] = [[0, 1], [1, 0]]
		dirs[5] = [[0, -1], [-1, 0]]
		dirs[6] = [[0, 1], [-1, 0]]

		seen = {(0, 0)}
		queue = [(0, 0)]
		while queue:
			x, y = queue.pop(0)

			if (x, y) == dest:
				return True

			for dx, dy in dirs[grid[x][y]]:
				nx = x + dx
				ny = y + dy
				if nx < 0 or nx >= M or ny < 0 or ny >= N or (nx, ny) in seen:
					continue

				if any(nx + dnx == x and ny + dny == y for dnx, dny in dirs[grid[nx][ny]]):
					queue.append((nx, ny)) 
					seen.add((nx, ny))

		return False
