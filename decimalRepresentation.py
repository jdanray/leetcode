# https://leetcode.com/problems/compute-decimal-representation/

class Solution(object):
	def decimalRepresentation(self, n):
		p = 1
		res = []
		while n > 0:
			d = n % 10
			c = d * p

			if c > 0:
				res.append(c)

			p *= 10
			n //= 10

		return res[::-1]