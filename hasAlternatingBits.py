# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

class Solution:
	def hasAlternatingBits(self, n):
		b = n & 1
		n >>= 1
		while n > 0:
			b1 = n & 1
			if b1 == b:
				return False
			b = b1
			n >>= 1
		return True
