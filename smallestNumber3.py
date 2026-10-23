# https://leetcode.com/problems/smallest-divisible-digit-product-i/

class Solution(object):
	def smallestNumber(self, n, t):
		x = 0
		p = 0
		while x < n or p % t != 0:
			x += 1
			y = x
			p = 1
			while y > 0:
				p *= y % 10
				y //= 10
            
		return x
