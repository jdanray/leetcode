# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
	def maxProfit(self, prices, fee):
		if len(prices) < 2:
			return 0

		hold = -prices[0]
		sold = 0
		for p in prices:
			hold = max(hold, sold - p)
			sold = max(sold, hold + p - fee)

		return sold
