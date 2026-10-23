# https://leetcode.com/problems/find-the-original-typed-string-i/

class Solution(object):
	def possibleStringCount(self, word):
		i = 0
		res = 1
		while i < len(word):
			while i + 1 < len(word) and word[i] == word[i + 1]:
				res += 1
				i += 1
			i += 1
		return res