# https://leetcode.com/problems/maximum-ice-cream-bars/ 


class Solution(object):
	def maxIceCream(self, costs, coins):
		costs = sorted(costs)
		res = 0
		for c in costs:
			coins -= c
			if coins < 0:
				return res
			res += 1
		return res
