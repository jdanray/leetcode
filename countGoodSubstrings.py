# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/  

class Solution(object):
	def countGoodSubstrings(self, s):
		res = 0
		for i in range(2, len(s)):
			if s[i] != s[i - 1] and s[i] != s[i - 2] and s[i - 1] != s[i - 2]:
				res += 1
		return res

class Solution(object):
	def countGoodSubstrings(self, s):
		def atMost(s, limit):
			i = 0
			res = 0
			count = collections.Counter()
			for j, c in enumerate(s):
				count[c] += 1

				while count[c] > 1 or j - i + 1 > limit:
					count[s[i]] -= 1
					i += 1

				res += j - i + 1

			return res

		limit = 3
		return atMost(s, limit) - atMost(s, limit - 1)
