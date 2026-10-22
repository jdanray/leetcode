# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/ 

class Solution(object):
	def maxSumOfSquares(self, n, s):
		L = 9
		res = ''
		for _ in range(n):
			if s > L:
				res += str(L)
				s -= L
			else:
				res += str(s)
				s = 0

		return res if s == 0 else ''
