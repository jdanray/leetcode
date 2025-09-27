# https://leetcode.com/problems/largest-triangle-area/

class Solution(object):
	def largestTriangleArea(self, points):
		res = 0
		for i in range(2, len(points)):
			for j in range(i):
				for k in range(j):
					x1, y1 = points[i]
					x2, y2 = points[j]
					x3, y3 = points[k]

					a = float(abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))) / 2

					res = max(res, a)

		return res