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

# a version that doesn't do any multiplication
class Solution:
	def reverseBits(self, n):
		nbits = 32
		r = 0
		for i in range(nbits):
			b = n & 1
			m = nbits - i - 1
			r += (b << m)
			n >>= 1
		return r
