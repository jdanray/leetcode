# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/  

class Solution(object):
	def countGoodSubstrings(self, s):
		res = 0
		for i in range(2, len(s)):
			if s[i] != s[i - 1] and s[i] != s[i - 2] and s[i - 1] != s[i - 2]:
				res += 1
		return res
