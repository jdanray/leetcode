# https://leetcode.com/problems/best-sightseeing-pair/

class Solution(object):
	def maxScoreSightseeingPair(self, values):
		m = 0
		res = 0
		for j, v in enumerate(values):
			if j > 0:
				res = max(res, m + v - j)
			m = max(m, v + j)
		return res