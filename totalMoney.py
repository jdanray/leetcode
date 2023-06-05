# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution(object):
	def totalMoney(self, n):
		W = 7

		res = 0
		pay = 0
		start = 0
		for d in range(n):
			if d % W == 0:
				start += 1
				pay = start

			res += pay
			pay += 1

		return res
