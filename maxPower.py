# https://leetcode.com/problems/consecutive-characters/ 

class Solution(object):
	def maxPower(self, s):
		m = 1
		p = 1
		for i in range(1, len(s)):
			if s[i] == s[i - 1]:
				p += 1
			else:
				p = 1
			m = max(m, p)

		return m
