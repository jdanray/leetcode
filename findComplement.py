# https://leetcode.com/problems/number-complement/description/

class Solution:
	def findComplement(self, num):
		c = 0
		i = 0
		while num > 0:
			b = num & 1
			r = b ^ 1
			c += (r << i)
			i += 1
			num >>= 1
		return c

class Solution:
	def findComplement(self, num):
		c = 0
		m = 1
		while num > 0:
			if num & 1 == 0:
				c += m
			num >>= 1
			m <<= 1
		return c
