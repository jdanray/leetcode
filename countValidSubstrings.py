# https://leetcode.com/problems/count-valid-substrings-i/ 

class Solution(object):
	def countValidSubstrings(self, s):
		pattern = 'abc'
		p = len(pattern) - 1

		i = 0
		res = 0
		for j, c in enumerate(s):
			if j >= p and s[j - p:j + 1] == pattern:
				i = j - p + 1

			res += j - i + 1

		return res
