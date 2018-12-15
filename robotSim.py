# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
	def robotSim(self, commands, obstacles):
		obstacles = set(tuple(obs) for obs in obstacles)
		delta = [[0, 1], [1, 0], [0, -1], [-1, 0]]
		angle = 0
		coords = (0, 0)
		m = 0
		for c in commands:
			if c == -1:
				angle = (angle + 1) % len(delta)
				continue
			elif c == -2:
				angle = (angle - 1) % len(delta)
				continue

			for _ in range(c):
				newcoords = (coords[0] + delta[angle][0], coords[1] + delta[angle][1])
				if newcoords in obstacles:
					break
				coords = newcoords

			m = max(m, coords[0] ** 2 + coords[1] ** 2)

		return m
