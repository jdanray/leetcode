# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

class Solution(object):
	def concatenatedBinary(self, n):
		MOD = 10**9 + 7
		s = 0
		for x in range(1, n + 1):
			newx = x
			i = 0
			while newx > 0:
				newx >>= 1
				i += 1

			s <<= i
			s = (s + x) % MOD

		return s
