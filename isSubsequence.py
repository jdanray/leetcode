# https://leetcode.com/problems/is-subsequence/

class Solution(object):
	def isSubsequence(self, s, t):
		if len(s) > len(t):
			return False

		i = 0
		for c in t:
			if i < len(s) and s[i] == c:
				i += 1

		return i == len(s) 
