# https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution(object):
	def maxProduct(self, n):
		a = float('-inf')
		b = float('-inf')
		while n > 0:
			d = n % 10

			if d >= a:
				a, b = d, a
			elif d > b:
				b = d

			n //= 10

		return a * b