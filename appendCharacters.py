# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/ 

class Solution(object):
	def appendCharacters(self, s, t):
		i = 0
		for c in s:
			if i < len(t) and t[i] == c:
				i += 1

		return len(t) - i
