# https://leetcode.com/problems/buy-two-chocolates/ 

class Solution(object):
	def buyChoco(self, prices, money):
		prices = sorted(prices)
		s = prices[0] + prices[1]
		return money if s > money else money - s
