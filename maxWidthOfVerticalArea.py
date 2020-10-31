# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/ 

class Solution(object):
	def maxWidthOfVerticalArea(self, points):
		xs = sorted(p[0] for p in points)
		return max(xs[i] - xs[i - 1] for i in range(1, len(xs)))
