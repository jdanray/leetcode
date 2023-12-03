# https://leetcode.com/problems/minimum-time-visiting-all-points/ 

class Solution(object):
	def minTimeToVisitAllPoints(self, points):
		res = 0
		for i in range(1, len(points)):
			dx = abs(points[i][0] - points[i - 1][0]) 
			dy = abs(points[i][1] - points[i - 1][1])

			res += min(dx, dy) + abs(dx - dy)

		return res
