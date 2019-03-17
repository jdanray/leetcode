# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import Counter

class Solution:
	def findAnagrams(self, s, p):
		if len(s) < len(p):
			return []

		pcount = Counter(p)
		scount = Counter(s[:len(p) - 1])

		indices = []
		for i in range(len(s) - len(p) + 1):
			scount[s[i + len(p) - 1]] += 1

			if scount == pcount:
				indices.append(i)

			scount[s[i]] -= 1
			if scount[s[i]] == 0:
				del scount[s[i]]

		return indices
