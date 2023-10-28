# https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/ 

class Solution(object):
	def minChanges(self, s):
		res = 0
		for i in range(0, len(s) - 1, 2):
			if s[i] != s[i + 1]:
				res += 1

		return res
