# https://leetcode.com/problems/minimum-rectangles-to-cover-points/ 

class Solution(object):
	def minRectanglesToCoverPoints(self, points, w):
		points = sorted(points)
		start = None
		res = 0
		for (x, _) in points:
			if start == None or x - start > w:
				start = x
				res += 1
                
		return res
