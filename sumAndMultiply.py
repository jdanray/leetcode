# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution(object):
	def sumAndMultiply(self, n):
		p = 1
		x = 0
		s = 0
		while n > 0:
			d = n % 10

			if d != 0:
				x += d * p
				s += d
				p *= 10

			n //= 10

		return x * s