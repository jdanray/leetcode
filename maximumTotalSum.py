# https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/ 

class Solution(object):
	def maximumTotalSum(self, height):
		height = sorted(height, reverse=True)

		prev = -1
		res = 0
		for h in height:
			if prev == -1:
				res += h
				prev = h
			else:
				x = min(prev - 1, h)
				if x > 0:
					res += x
				else:
					return -1
				prev = x

		return res
