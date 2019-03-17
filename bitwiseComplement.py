# https://leetcode.com/problems/complement-of-base-10-integer/ 

class Solution:
	def bitwiseComplement(self, N):
		if N == 0:
			return 1

		C = 0
		p = 1
		while N > 0:
			b = N & 1
			c = b ^ 1
			C += p * c

			N >>= 1
			p <<= 1

		return C
