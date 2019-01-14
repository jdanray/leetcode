# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution(object):
	def kClosest(self, points, K):
		return sorted(points, key=lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2))[:K]
