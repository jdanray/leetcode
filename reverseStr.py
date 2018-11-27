# https://leetcode.com/problems/reverse-string-ii/description/

class Solution(object):
	def reverseStr(self, s, k, i=0):
		if i >= len(s):
			return ''

		r = ''
		for j in range(i, min(i + k, len(s))):
			r = s[j] + r
		for j in range(i + k, min(i + k + k, len(s))):
			r += s[j]

		return r + self.reverseStr(s, k, i + k + k)
