# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

class Solution(object):
	def findMinArrowShots(self, points):
		if not points:
			return 0

		n = 1
		o = 0
		points = sorted(points, key=lambda p: p[1])
		for i in range(1, len(points)):
			if points[i][0] > points[o][1]:
				o = i
				n += 1

		return n

# A simpler solution

class Solution(object):
	def findMinArrowShots(self, points):
		last = None
		res = 0
		points = sorted(points, key=lambda p: p[1])
		for p in points:
			if last == None or last < p[0]:
				res += 1
				last = p[1]

		return res
