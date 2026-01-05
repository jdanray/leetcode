# https://leetcode.com/problems/largest-even-number/

class Solution(object):
	def largestEven(self, s):
		i = len(s)
		while i > 0 and s[i - 1] == '1':
			i -= 1
		return s[:i]