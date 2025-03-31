# https://leetcode.com/problems/minimum-cost-to-reach-every-position/

class Solution(object):
	def minCosts(self, cost):
		m = float('inf')
		res = []
		for c in cost:
			m = min(m, c)
			res.append(m)
		return res