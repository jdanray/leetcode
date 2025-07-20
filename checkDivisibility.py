# https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

class Solution(object):
	def checkDivisibility(self, n):
		oldn = n
		s = 0
		p = 1
		while n > 0:
			d = n % 10

			s += d
			p *= d

			n //= 10

		return oldn % (s + p) == 0