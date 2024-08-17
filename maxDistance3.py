# https://leetcode.com/problems/maximum-distance-in-arrays/ 

class Solution(object):
	def maxDistance(self, arrays):
		if not arrays:
			return 0

		minim = arrays[0][0]
		maxim = arrays[0][-1]
		res = 0
		for i in range(1, len(arrays)):
			res = max(res, abs(arrays[i][-1] - minim), abs(arrays[i][0] - maxim))
			maxim = max(maxim, arrays[i][-1])
			minim = min(minim, arrays[i][0])

		return res
