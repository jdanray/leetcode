# https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution(object):
	def maxDistinct(self, s):
		seen = set()
		res = 0
		for c in s:
			if c not in seen:
				res += 1
				seen.add(c)
		return res