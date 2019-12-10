# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution(object):
	def subtractProductAndSum(self, n):
		d = 0
		p = 1
		s = 0
		while n > 0:
			d = n % 10
			s += d
			p *= d
			n //= 10
		return p - s
