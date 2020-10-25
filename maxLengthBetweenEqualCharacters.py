# https://leetcode.com/problems/largest-substring-between-two-equal-characters/ 

class Solution(object):
	def maxLengthBetweenEqualCharacters(self, s):
		seen = {}
		res = -1
		for i, c in enumerate(s):
			if c in seen:
				d = i - seen[c] - 1
				res = max(res, d)

			if c not in seen:
				seen[c] = i

		return res
