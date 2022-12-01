# https://leetcode.com/problems/determine-if-string-halves-are-alike/ 

class Solution(object):
	def halvesAreAlike(self, s):
		N = len(s)

		vchars = "aeiouAEIOU"
		nvowels = lambda half: sum(1 if c in vchars else 0 for c in half)

		a = s[:N//2]
		b = s[N//2:]

		return nvowels(a) == nvowels(b)

class Solution(object):
	def halvesAreAlike(self, s):
		vowels = set('aeiouAEIOU')
		M = len(s) // 2

		count = [0, 0]
		for i, c in enumerate(s):
			if c in vowels:
				count[i >= M] += 1

		return count[0] == count[1]
