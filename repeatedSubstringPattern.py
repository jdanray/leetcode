# https://leetcode.com/problems/repeated-substring-pattern/description/

class Solution:
	def repeatedSubstringPattern(self, s):
		sub = ''
		for i in range(len(sub) // 2):
			sub += s[i]
			m = len(s) // len(sub)
			if sub * m == s:
				return True
		return False
