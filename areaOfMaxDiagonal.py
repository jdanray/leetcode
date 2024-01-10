# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/ 

class Solution(object):
	def areaOfMaxDiagonal(self, dimensions):
		maxDiag = 0
		res = 0
		for (h, w) in dimensions:
			d = math.sqrt(h * h + w * w)
			if d > maxDiag or (d == maxDiag and h * w > res):
				maxDiag = d
				res = h * w
                
		return res
