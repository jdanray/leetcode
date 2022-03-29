# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ 

class Solution(object):
	def maxProfit(self, prices):
		m = prices[0]
		res = 0
		for i in range(1, len(prices)):
			m = min(m, prices[i])
			res = max(res, prices[i] - m)
		return res
