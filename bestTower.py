# https://leetcode.com/problems/best-reachable-tower/

class Solution(object):
	def bestTower(self, towers, center, radius):
		m = [-1, -1, float('-inf')]
		for (x, y, q) in towers:
			d = abs(center[0] - x) + abs(center[1] - y)
			if d <= radius:
				if q > m[2] or (q == m[2] and (x < m[0] or (x == m[0] and y < m[1]))):
					m = [x, y, q]
		return m[:2]