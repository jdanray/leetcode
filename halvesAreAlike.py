# https://leetcode.com/problems/determine-if-string-halves-are-alike/ 

class Solution(object):
	def halvesAreAlike(self, s):
		N = len(s)

		vchars = "aeiouAEIOU"
		nvowels = lambda half: sum(1 if c in vchars else 0 for c in half)

		a = s[:N//2]
		b = s[N//2:]

		return nvowels(a) == nvowels(b)
