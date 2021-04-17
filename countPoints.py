# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/ 

class Solution(object):
	def countPoints(self, points, queries):
		def dist(x1, y1, x2, y2):
			return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

		res = []
		for (xq, yq, r) in queries:
			res.append(0)
			for (xp, yp) in points:
				if dist(xq, yq, xp, yp) <= r:
					res[-1] += 1

		return res 
