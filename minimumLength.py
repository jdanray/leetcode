# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution(object):
	def minimumLength(self, s):
		i = 0
		j = len(s) - 1
		while i < j and s[i] == s[j]:
			i += 1
			j -= 1

			while i <= j and s[i] == s[i - 1]:
				i += 1
			while i <= j and s[j] == s[j + 1]:
				j -= 1

		return j - i + 1
