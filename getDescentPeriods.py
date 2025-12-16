# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution(object):
	def getDescentPeriods(self, prices):
		prev = -float('inf')
		d = 0
		res = 0
		for p in prices:
			if prev == p + 1:
				d += 1
			else:
				d = 1

			res += d
			prev = p

		return res

class Solution(object):
	def getDescentPeriods(self, prices):
		d = 0
		res = 0
		for i, p in enumerate(prices):
			if i - 1 >= 0 and p == prices[i - 1] - 1:
				d += 1
			else:
				d = 1

			res += d

		return res