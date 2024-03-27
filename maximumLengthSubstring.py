# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/ 

class Solution(object):
	def maximumLengthSubstring(self, s):
		M = 2
		i = 0
		count = collections.Counter()
		res = 0
		for j, c in enumerate(s):
			count[c] += 1

			while count[c] > M:
				count[s[i]] -= 1
				i += 1

			res = max(res, j - i + 1)

		return res
