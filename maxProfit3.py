# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/ 

class Solution(object):
	def maxProfit(self, k, prices):
		N = len(prices)

		memo = {}
		def dp(i, k, holding):
			if i >= N or k == 0:
				return 0

			if (i, k, holding) in memo:
				return memo[i, k, holding]

			notrans = dp(i + 1, k, holding)
			if holding:
				trans = dp(i + 1, k - 1, False) + prices[i]
			else:
				trans = dp(i + 1, k, True) - prices[i]

			memo[i, k, holding] = max(notrans, trans)
			return memo[i, k, holding]

		return dp(0, k, False)
