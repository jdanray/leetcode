# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/ 

class Solution(object):
	def findTheLongestBalancedSubstring(self, s):
		ones = 0
		zeros = 0
		res = 0
		for c in s:
			if c == '1':
				ones += 1
				if ones <= zeros:
					res = max(res, 2 * ones)
			elif c == '0':
				if ones > 0:
					ones = 0
					zeros = 0
				zeros += 1
		return res
