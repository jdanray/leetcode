# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution(object):
	def hasSameDigits(self, s):
		while len(s) > 2:
			ns = ""
			for i in range(len(s) - 1):
				ns += str((int(s[i]) + int(s[i + 1])) % 10)
			s = ns
            
		return s[0] == s[1]