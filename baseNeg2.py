# https://leetcode.com/problems/convert-to-base-2/ 

class Solution:
	def baseNeg2(self, N):
		if N == 0:
			return '0'

		r = []
		while N != 0:
			b = N & 1
			r = [b] + r
			N //= 2
			N = -N

		return ''.join(str(b) for b in r)
