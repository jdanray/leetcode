# https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution:
	def prefixesDivBy5(self, A):
		pre = []
		N = 0
		for a in A:
			N *= 2
			N += a
			pre.append(N % 5 == 0)
		return pre
