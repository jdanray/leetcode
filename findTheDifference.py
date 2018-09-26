# https://leetcode.com/problems/find-the-difference/description/

from collections import Counter

class Solution(object):
	def findTheDifference(self, s, t):
		scount = Counter(s)
		tcount = Counter(t)
		for c in tcount:
			if c not in scount or tcount[c] > scount[c]:
				return c
