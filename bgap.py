# https://leetcode.com/problems/binary-gap/description/

class Solution(object):
	def binaryGap(self, N):
		s = -1
		i = 0
		m = 0
		while N > 0:
			b = N & 1
			if b == 1:
				if s != -1 and i - s > m:
					m = i - s
				s = i
			i += 1
			N >>= 1
		return m
