# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
	def trailingZeroes(self, n):
		z = 0
		while n > 0:
			n //= 5
			z += n
		return z
