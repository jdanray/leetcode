# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution(object):
	def countGoodRectangles(self, rectangles):
		m = max(min(r) for r in rectangles)
		return len([r for r in rectangles if min(r) == m])
