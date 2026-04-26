# https://leetcode.com/problems/valid-digit-number/

class Solution(object):
	def validDigit(self, n, x):
		n, x = str(n), str(x)
		return n[0] != x and x in n