# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution(object):
	def finalPrices(self, prices):
		N = len(prices)
		res = [p for p in prices]
		for i in range(N):
			for j in range(i + 1, N):
				if prices[j] <= prices[i]:
					res[i] -= prices[j]
					break
		return res
