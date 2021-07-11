# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution(object):
	def nearestExit(self, maze, entrance):
		M = len(maze)
		N = len(maze[0])

		onBorder = lambda x, y: x == 0 or y == 0 or x == M - 1 or y == N - 1
		withinMaze = lambda x, y: x >= 0 and y >= 0 and x < M and y < N

		entrance = tuple(entrance)
		seen = {entrance}
		queue = [[entrance, 0]]
		while queue:
			loc, dist = queue.pop(0)
			x, y = loc
 
			if onBorder(x, y) and loc != entrance:
				return dist

			deltas = [[0, -1], [0, 1], [1, 0], [-1, 0]]
			for dx, dy in deltas:
				newx = x + dx
				newy = y + dy
				if withinMaze(newx, newy) and maze[newx][newy] == '.' and (newx, newy) not in seen:
					queue.append([(newx, newy), dist + 1])
					seen.add((newx, newy))

		return -1
