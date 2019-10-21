# https://leetcode.com/problems/check-if-it-is-a-straight-line/ 

class Solution(object):
	def checkStraightLine(self, coordinates):
		x0, y0 = coordinates[0]
		x1, y1 = coordinates[1]
		for coord in coordinates:
			x2, y2 = coord
			if (x2 - x0) * (y2 - y1) != (x2 - x1) * (y2 - y0):
				return False
		return True

