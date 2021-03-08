# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/ 

class Solution(object):
	def nearestValidPoint(self, x, y, points):
		dist = lambda x2, y2: abs(x - x2) + abs(y - y2)
		mindist = float('inf')
		res = -1
		for i, (x2, y2) in enumerate(points):
			if x == x2 or y == y2:
				d = dist(x2, y2)
				if d < mindist:
					mindist = d
					res = i
		return res
