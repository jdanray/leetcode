# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
	def lengthOfLastWord(self, s):
		i = len(s) - 1
		while i >= 0 and s[i] == ' ':
			i -= 1

		n = 0
		while i >= 0 and s[i] != ' ':
			i -= 1
			n += 1

		return n
