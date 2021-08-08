# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/ 

class Solution(object):
	def isPrefixString(self, s, words):
		concat = ""
		for w in words:
			concat += w
			if concat == s:
				return True

		return False
