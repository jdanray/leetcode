# https://leetcode.com/problems/assign-cookies/description/

class Solution(object):
	def findContentChildren(self, g, s):
		i = 0
		j = 0
		g = sorted(g, reverse=True)
		s = sorted(s, reverse=True)
		while i < len(g) and j < len(s):
			if s[j] >= g[i]:
				j += 1
			i += 1
		return j
