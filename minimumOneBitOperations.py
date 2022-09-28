# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

class Solution(object):
	def minimumOneBitOperations(self, n):
		if n == 0:
			return 0

		num = n
		left = 1
		p = 1
		while num > 0:
			b = num & 1

			if b == 1:
				left = p

			p <<= 1
			num >>= 1

		return left + self.minimumOneBitOperations(left >> 1) - self.minimumOneBitOperations(n - left)
