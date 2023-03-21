# https://leetcode.com/problems/number-of-even-and-odd-bits/ 

class Solution(object):
	def evenOddBit(self, n):
		res = [0, 0]
		i = 0
		while n > 0:
			res[i] += (n & 1)
			i = 1 - i
			n >>= 1
		return res
