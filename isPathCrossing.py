# https://leetcode.com/problems/path-crossing/ 

class Solution(object):
	def isPathCrossing(self, path):
		dx = {'N': 1, 'S': -1, 'W': 0, 'E': 0}
		dy = {'N': 0, 'S': 0, 'W': 1, 'E': -1}

		x = 0
		y = 0
		visited = {(0, 0)}
		for p in path:
			x += dx[p]
			y += dy[p]

			if (x, y) in visited:
				return True
			else:
				visited.add((x, y))

		return False
