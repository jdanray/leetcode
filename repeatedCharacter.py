# https://leetcode.com/problems/first-letter-to-appear-twice/ 

class Solution(object):
	def repeatedCharacter(self, s):
		seen = set()
		for c in s:
			if c in seen:
				return c
			else:
				seen.add(c)
