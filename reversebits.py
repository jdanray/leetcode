# https://leetcode.com/problems/reverse-bits/description/

class Solution:
	def reverseBits(self, n):
		nbits = 32
		p = 2 ** nbits
		r = 0
		for _ in range(nbits):
			b = n & 1
			p >>= 1
			n >>= 1
			r += p * b
		return r
