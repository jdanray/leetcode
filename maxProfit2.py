# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution(object):
	def maxProfit(self, prices):
		memo = {}
		def helper(i, bought):
			if i >= len(prices):
				return 0

			if (i, bought) in memo:
				return memo[i, bought]

			notrans = helper(i + 1, bought)
			if bought:
				memo[i, bought] = max(notrans, helper(i + 2, False) + prices[i])
			else:
				memo[i, bought] = max(notrans, helper(i + 1, True) - prices[i])
			return memo[i, bought]

		return helper(0, False)
