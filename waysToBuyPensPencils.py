# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/ 

class Solution(object):
	def waysToBuyPensPencils(self, total, cost1, cost2):
		res = 0
		while total >= 0:
			res += total // cost2 + 1
			total -= cost1
		return res
