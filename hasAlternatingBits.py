# https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
	def hasAlternatingBits(self, n):
		b = n & 1
		while n > 0:
			n >>= 1
			c = n & 1
			if c == b:
				return False
			b = c
		return True
