# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/ 

class Solution(object):
	def maxProfit(self, prices):
		buy = -prices[0]
		sell = 0
		for i in range(1, len(prices)):
			buy, sell = max(buy, sell - prices[i]), max(sell, buy + prices[i])
		return max(buy, sell)
