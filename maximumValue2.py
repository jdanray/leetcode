# https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

class Solution(object):
	def maximumValue(self, n, s, m):
		return s + (m * (n // 2)) - (n // 2 - (n > 1))