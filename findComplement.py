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
